from flask import Flask, render_template, request, redirect, session, flash
import pymysql
from database_connection import connect_to_database, hash_password, verify_password
import os
import google.generativeai as genai
import pymysql
from werkzeug.utils import secure_filename
import pdf2image
import re


app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a random secret key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_type = request.form.get('user_type')
        name = request.form.get('name')
        password = hash_password(request.form.get('password'))

        if not user_type or not name or not password:
            flash("All fields are required!")
            return redirect('/register')

        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            if user_type == 'student':
                roll_no = request.form.get('roll_no')
                if not roll_no:
                    flash("Roll number is required for student registration.")
                    return redirect('/register')

                sql = "INSERT INTO students (roll_no, name, password) VALUES (%s, %s, %s)"
                cursor.execute(sql, (roll_no, name, password))

            elif user_type == 'teacher':
                teacher_id = request.form.get('teacher_id')
                if not teacher_id:
                    flash("Teacher ID is required for teacher registration.")
                    return redirect('/register')

                sql = "INSERT INTO teachers (teacher_id, name, password) VALUES (%s, %s, %s)"
                cursor.execute(sql, (teacher_id, name, password))
            
            else:
                flash("Invalid user type selected.")
                return redirect('/register')

            conn.commit()
            flash('Registration successful!')
            return redirect('/')

        except pymysql.IntegrityError as ie:
            flash('User already exists. Please try again with a different ID.')
        except Exception as e:
            flash(f"An error occurred: {str(e)}")
        finally:
            if conn:
                conn.close()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_type = request.form['user_type']
        
        # Student login
        if user_type == 'student':
            roll_no = request.form['username']
            password = request.form['password']
            
            conn = connect_to_database()
            try:
                with conn.cursor() as cursor:
                    sql = "SELECT * FROM students WHERE roll_no = %s"
                    cursor.execute(sql, (roll_no,))
                    student = cursor.fetchone()
                    
                    if student and verify_password(student['password'], password):
                        session['user_type'] = 'student'
                        session['roll_no'] = roll_no
                        session['name'] = student['name']
                        return redirect('/student_dashboard')
                    else:
                        flash('Invalid credentials!')
            finally:
                conn.close()
        
        # Teacher login
        elif user_type == 'teacher':
            teacher_id = request.form['username']
            password = request.form['password']
            
            conn = connect_to_database()
            try:
                with conn.cursor() as cursor:
                    sql = "SELECT * FROM teachers WHERE teacher_id = %s"
                    cursor.execute(sql, (teacher_id,))
                    teacher = cursor.fetchone()
                    
                    if teacher and verify_password(teacher['password'], password):
                        session['user_type'] = 'teacher'
                        session['teacher_id'] = teacher_id
                        session['name'] = teacher['name']
                        return redirect('/teacher_dashboard')
                    else:
                        flash('Invalid credentials!')
            finally:
                conn.close()
    
    return render_template('login.html')

@app.route('/student_dashboard')
def student_dashboard():
    if 'user_type' not in session or session['user_type'] != 'student':
        return redirect('/login')
    
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            # Get student's classes
            sql = """
            SELECT c.class_id, c.class_name 
            FROM classes c
            JOIN class_students cs ON c.class_id = cs.class_id
            WHERE cs.roll_no = %s
            """
            cursor.execute(sql, (session['roll_no'],))
            classes = cursor.fetchall()
            
            # Get assignments for these classes with submission details
            assignments = []
            for cls in classes:
                sql = """
                SELECT a.*, 
                       sa.submission_id IS NOT NULL AS is_submitted,
                       sa.feedback,
                       sa.grade
                FROM assignments a
                LEFT JOIN submitted_assignments sa 
                ON a.assignment_id = sa.assignment_id 
                AND sa.roll_no = %s
                WHERE a.class_id = %s
                """
                cursor.execute(sql, (session['roll_no'], cls['class_id']))
                class_assignments = cursor.fetchall()
                assignments.extend(class_assignments)
            
            return render_template('student_dashboard.html', 
                                   student_name=session['name'], 
                                   classes=classes, 
                                   assignments=assignments)
    finally:
        conn.close()


@app.route('/teacher_dashboard')
def teacher_dashboard():
    if 'user_type' not in session or session['user_type'] != 'teacher':
        return redirect('/login')
    
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            # Get teacher's classes with student count
            sql = """
            SELECT c.class_id, c.class_name, 
                   (SELECT COUNT(DISTINCT roll_no) 
                    FROM class_students 
                    WHERE class_id = c.class_id) as students_count
            FROM classes c
            WHERE c.teacher_id = %s
            """
            cursor.execute(sql, (session['teacher_id'],))
            classes = cursor.fetchall()
            
            # Get all assignments created by the teacher
            sql = """
            SELECT a.*, c.class_name 
            FROM assignments a
            JOIN classes c ON a.class_id = c.class_id
            WHERE c.teacher_id = %s
            ORDER BY a.due_date
            """
            cursor.execute(sql, (session['teacher_id'],))
            all_assignments = cursor.fetchall()
            
            return render_template('teacher_dashboard.html', 
                                   teacher_name=session['name'], 
                                   classes=classes,
                                   all_assignments=all_assignments)
    finally:
        conn.close()

@app.route('/assignment_details/<int:assignment_id>')
def assignment_details(assignment_id):
    if 'user_type' not in session or session['user_type'] != 'teacher':
        return redirect('/login')
    
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            # Get assignment details
            sql = """
            SELECT a.*, c.class_name 
            FROM assignments a
            JOIN classes c ON a.class_id = c.class_id
            WHERE a.assignment_id = %s
            """
            cursor.execute(sql, (assignment_id,))
            assignment = cursor.fetchone()
            
            # Get total students in the class
            sql = """
            SELECT COUNT(DISTINCT roll_no) as total_students
            FROM class_students
            WHERE class_id = %s
            """
            cursor.execute(sql, (assignment['class_id'],))
            total_students = cursor.fetchone()['total_students']
            
            # Get submitted students
            sql = """
            SELECT s.roll_no, s.name, sa.submission_date, sa.grade
            FROM submitted_assignments sa
            JOIN students s ON sa.roll_no = s.roll_no
            WHERE sa.assignment_id = %s
            """
            cursor.execute(sql, (assignment_id,))
            submitted_students = cursor.fetchall()
            
            # Get non-submitted students
            sql = """
            SELECT s.roll_no, s.name
            FROM students s
            JOIN class_students cs ON s.roll_no = cs.roll_no
            WHERE cs.class_id = %s AND s.roll_no NOT IN (
                SELECT roll_no 
                FROM submitted_assignments 
                WHERE assignment_id = %s
            )
            """
            cursor.execute(sql, (assignment['class_id'], assignment_id))
            non_submitted_students = cursor.fetchall()
            
            return render_template('assignment_details.html', 
                                   assignment=assignment,
                                   total_students=total_students,
                                   submitted_students=submitted_students,
                                   non_submitted_students=non_submitted_students)
    finally:
        conn.close()
        
@app.route('/create_class', methods=['POST'])
def create_class():
    if 'user_type' not in session or session['user_type'] != 'teacher':
        return redirect('/login')
    
    class_name = request.form['class_name']
    
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO classes (class_name, teacher_id) VALUES (%s, %s)"
            cursor.execute(sql, (class_name, session['teacher_id']))
        conn.commit()
        flash('Class created successfully!')
    finally:
        conn.close()
    
    return redirect('/teacher_dashboard')

@app.route('/add_student_to_class', methods=['POST'])
def add_student_to_class():
    if 'user_type' not in session or session['user_type'] != 'teacher':
        return redirect('/login')
    
    class_id = request.form['class_id']
    roll_no = request.form['roll_no']
    
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            # Check if student exists
            sql = "SELECT * FROM students WHERE roll_no = %s"
            cursor.execute(sql, (roll_no,))
            student = cursor.fetchone()
            
            if student:
                # Add student to class
                sql = "INSERT INTO class_students (class_id, roll_no) VALUES (%s, %s)"
                cursor.execute(sql, (class_id, roll_no))
                conn.commit()
                flash('Student added to class successfully!')
            else:
                flash('Student not found!')
    except pymysql.IntegrityError:
        flash('Student already in this class!')
    finally:
        conn.close()
    
    return redirect('/teacher_dashboard')

@app.route('/create_assignment', methods=['POST'])
def create_assignment():
    if 'user_type' not in session or session['user_type'] != 'teacher':
        return redirect('/login')
    
    class_id = request.form['class_id']
    title = request.form['title']
    description = request.form['description']
    due_date = request.form['due_date']
    
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO assignments (class_id, title, description, due_date) 
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (class_id, title, description, due_date))
        conn.commit()
        flash('Assignment created successfully!')
    finally:
        conn.close()
    
    return redirect('/teacher_dashboard')

@app.route('/class_details/<int:class_id>')
def class_details(class_id):
    if 'user_type' not in session or session['user_type'] != 'teacher':
        return redirect('/login')
    
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            # Get class details
            sql = "SELECT * FROM classes WHERE class_id = %s AND teacher_id = %s"
            cursor.execute(sql, (class_id, session['teacher_id']))
            class_info = cursor.fetchone()
            
            if not class_info:
                flash('Class not found!')
                return redirect('/teacher_dashboard')
            
            # Get all assignments for this class
            sql = """
            SELECT a.*, 
                   COUNT(DISTINCT cs.roll_no) AS total_students,
                   COUNT(DISTINCT sa.roll_no) AS submitted_students
            FROM assignments a
            LEFT JOIN class_students cs ON cs.class_id = a.class_id
            LEFT JOIN submitted_assignments sa ON sa.assignment_id = a.assignment_id
            WHERE a.class_id = %s
            GROUP BY a.assignment_id
            """
            cursor.execute(sql, (class_id,))
            assignments = cursor.fetchall()
            
            # Detailed assignment submission analysis
            detailed_assignments = []
            for assignment in assignments:
                # Get students who haven't submitted
                sql = """
                SELECT s.roll_no, s.name
                FROM students s
                JOIN class_students cs ON s.roll_no = cs.roll_no
                WHERE cs.class_id = %s AND s.roll_no NOT IN (
                    SELECT roll_no 
                    FROM submitted_assignments 
                    WHERE assignment_id = %s
                )
                """
                cursor.execute(sql, (class_id, assignment['assignment_id']))
                non_submitted_students = cursor.fetchall()
                
                # Get students who have submitted
                sql = """
                SELECT s.roll_no, s.name, sa.submission_date, sa.feedback, sa.grade
                FROM submitted_assignments sa
                JOIN students s ON sa.roll_no = s.roll_no
                WHERE sa.assignment_id = %s
                """
                cursor.execute(sql, (assignment['assignment_id'],))
                submitted_students = cursor.fetchall()
                
                # Compile assignment details
                assignment_details = dict(assignment)
                assignment_details['non_submitted_students'] = non_submitted_students
                assignment_details['submitted_students'] = submitted_students
                detailed_assignments.append(assignment_details)
            
            return render_template('class_details.html', 
                                   class_info=class_info, 
                                   assignments=detailed_assignments)
    finally:
        conn.close()


@app.route('/class_analysis/<int:class_id>')
def class_analysis(class_id):
    if 'user_type' not in session or session['user_type'] != 'teacher':
        return redirect('/login')
    
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            # Get class details
            sql = "SELECT * FROM classes WHERE class_id = %s AND teacher_id = %s"
            cursor.execute(sql, (class_id, session['teacher_id']))
            class_info = cursor.fetchone()
            
            if not class_info:
                flash('Class not found!')
                return redirect('/teacher_dashboard')
            
            # Get assignments with submission details
            sql = """
            SELECT a.assignment_id, a.title, a.due_date,
                   COUNT(DISTINCT cs.roll_no) AS total_students,
                   COUNT(DISTINCT sa.roll_no) AS submitted_students
            FROM assignments a
            LEFT JOIN class_students cs ON cs.class_id = a.class_id
            LEFT JOIN submitted_assignments sa ON sa.assignment_id = a.assignment_id
            WHERE a.class_id = %s
            GROUP BY a.assignment_id
            """
            cursor.execute(sql, (class_id,))
            assignments = cursor.fetchall()
            
            # Tableau dashboard URLs
            # Replace these with your actual Tableau dashboards
            tableau_class_dashboard_url = "https://public.tableau.com/views/ClassOverview/ClassDashboard"
            tableau_base_url = "https://public.tableau.com/views/AssignmentAnalysis/AssignmentDashboard"
            
            return render_template('class_analysis.html', 
                                   class_info=class_info, 
                                   assignments=assignments,
                                   tableau_class_dashboard_url=tableau_class_dashboard_url,
                                   tableau_base_url=tableau_base_url)
    finally:
        conn.close()



@app.route('/submit_assignment', methods=['POST'])
def submit_assignment():
    if 'user_type' not in session or session['user_type'] != 'student':
        return redirect('/login')
    
    # Handle file upload
    if 'assignment_file' not in request.files:
        flash('No file part')
        return redirect('/student_dashboard')
    
    file = request.files['assignment_file']
    
    # If no file is selected
    if file.filename == '':
        flash('No selected file')
        return redirect('/student_dashboard')
    
    # Ensure upload directory exists
    upload_folder = 'submissions'
    os.makedirs(upload_folder, exist_ok=True)
    
    # Secure filename and save file
    filename = secure_filename(f"{session['roll_no']}_{file.filename}")
    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)
    
    # Extract text from PDF using Gemini
    try:
        extracted_text = extract_text_from_pdf_with_gemini(file_path)
    except Exception as e:
        flash(f'Error extracting text: {str(e)}')
        return redirect('/student_dashboard')
    
    # Generate feedback and grade using Gemini
    try:
        # Configure Gemini API
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("Missing GEMINI_API_KEY environment variable")
            
        genai.configure(api_key=api_key)
        
        # Create the model for grading
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Prompt for feedback and grading
        prompt = f"""
        Evaluate the following student assignment text:
        
        {extracted_text}
        
        Please provide:
        2. A precised feedback report
        3. A grade out of 100
        4. Specific strengths and areas of improvement
        
        
        Format your response as:
        Feedback: [Detailed Feedback]
        Grade: [Numeric Grade out of 100]
        Strengths: [List of Strengths]
        Improvements: [List of Improvement Areas]
        """
        
        # Generate response
        response = model.generate_content(prompt)
        
        # Parse the response
        full_response = response.text
        
        # Extract grade
        grade_match = re.search(r'Grade:\s*(\d+)', full_response)
        grade = float(grade_match.group(1)) if grade_match else 0
        
        # Extract feedback
        feedback_match = re.search(r'Feedback:\s*(.+?)(?=\n\w+:|\Z)', full_response, re.DOTALL)
        feedback = feedback_match.group(1).strip() if feedback_match else "Plagarism or other Students Assignment"
    
    except Exception as e:
        flash(f'Error generating feedback: {str(e)}')
        return redirect('/student_dashboard')
    
    # Save submission to database
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            # Insert submission details
            sql = """
            INSERT INTO submitted_assignments
            (assignment_id, roll_no, submission_date, file_path, extracted_text, feedback, grade)
            VALUES (%s, %s, NOW(), %s, %s, %s, %s);
            """
            cursor.execute(sql, (
                request.form['assignment_id'], 
                session['roll_no'], 
                file_path, 
                extracted_text, 
                feedback, 
                grade
            ))
        conn.commit()
        flash('Assignment submitted successfully!')
    except Exception as e:
        flash(f'Database error: {str(e)}')
    finally:
        conn.close()
    
    return redirect('/student_dashboard')

def extract_text_from_pdf_with_gemini(pdf_path):
    """
    Extract text from PDF using Gemini vision model
    
    Args:
        pdf_path (str): Path to the PDF file
    
    Returns:
        str: Extracted text from the PDF
    """
    # Get API key from environment variable
    api_key = "AIzaSyBFJi_RhIbNND7FvvqYE28uEkpPqO00Lys"
    if not api_key:
        raise ValueError("Missing GEMINI_API_KEY environment variable")
    
    # Configure Gemini API
    genai.configure(api_key=api_key)
    
    # Create the model with multimodal capabilities
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Set image format and MIME type
    intermediate_image_format = "png"
    intermediate_mime_type = "image/png"
    
    all_pages_text = []
    
    try:
        # Import PyMuPDF
        import pymupdf
        
        # Open the PDF document using PyMuPDF
        doc = pymupdf.open(pdf_path)
        total_pages = len(doc)
        
        # Iterate through each page
        for page_num in range(total_pages):
            current_page_index = page_num + 1  # 1-based index for display
            
            try:
                # Get the page
                page = doc[page_num]
                
                # Render page to an image with higher resolution for better OCR
                pix = page.get_pixmap(dpi=150)
                # Convert pixmap to image bytes
                img_data = pix.tobytes(output=intermediate_image_format)
                
                # Prepare the content parts for the API request
                image_part = {
                    "mime_type": intermediate_mime_type,
                    "data": img_data
                }
                # Prompt for text extraction
                prompt_part = "Extract all handwritten and printed text visible in this image. Preserve the general layout if possible, but focus on accurate transcription. Provide only the extracted text."
                
                # Make the API call
                contents = [prompt_part, image_part]
                request_options = {"timeout": 120}  # 120 seconds timeout
                response = model.generate_content(contents, request_options=request_options)
                
                # Extract text from the response
                if response.candidates and response.candidates[0].content.parts:
                    extracted_text = response.candidates[0].content.parts[0].text
                    page_separator = f"\n\n--- Page {current_page_index} ---\n\n"
                    all_pages_text.append(page_separator + extracted_text.strip())
                elif hasattr(response, 'text') and response.text:
                    # Fallback for simpler response structure
                    page_separator = f"\n\n--- Page {current_page_index} ---\n\n"
                    all_pages_text.append(page_separator + response.text.strip())
                else:
                    # Log that a page was skipped but continue processing others
                    page_separator = f"\n\n--- Page {current_page_index} (Error extracting text) ---\n\n"
                    all_pages_text.append(page_separator)
                
            except Exception as page_e:
                # Continue to the next page if there's an error
                page_separator = f"\n\n--- Page {current_page_index} (Error processing page: {str(page_e)}) ---\n\n"
                all_pages_text.append(page_separator)
        
        # Close the document
        doc.close()
        
        # Combine text from all pages
        final_text = "".join(all_pages_text).strip()
        
        if not final_text:
            raise ValueError("No text could be extracted from the PDF")
        
        return final_text
        
    except Exception as e:
        # Ensure document is closed if it was opened
        if 'doc' in locals():
            try:
                doc.close()
            except:
                pass
        raise e

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
