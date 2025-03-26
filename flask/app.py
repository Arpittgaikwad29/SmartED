# app.py
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, ClassRoom, ClassEnrollment
from forms import RegistrationForm, LoginForm, CreateClassForm, JoinClassForm
from config import Config
from flask_mysqldb import MySQL
import uuid

app = Flask(__name__)
app.config.from_object(Config)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'teams_clone_db'
mysql = MySQL(app)

# Initialize extensions
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data, 
            email=form.email.data,
            role=form.role.data
        )
        new_user.set_password(form.password.data)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            print("Error while registering user:", e)  # Debug print
            flash('An error occurred. Please try again.', 'error')
    
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'error')
    
    return render_template('login.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'admin':
        # Show classes created by admin
        created_classes = ClassRoom.query.filter_by(creator_id=current_user.id).all()
        return render_template('admin_dashboard.html', classes=created_classes)
    else:
        # Show classes student is enrolled in
        enrolled_classes = [enrollment.classroom for enrollment in current_user.enrolled_classes]
        return render_template('student_dashboard.html', classes=enrolled_classes)

@app.route('/create-class', methods=['GET', 'POST'])
@login_required
def create_class():
    if current_user.role != 'admin':
        flash('Only admins can create classes', 'error')
        return redirect(url_for('dashboard'))
    
    form = CreateClassForm()
    if form.validate_on_submit():
        # Generate unique team code
        team_code = str(uuid.uuid4())[:8].upper()
        
        # Ensure team code is unique
        while ClassRoom.query.filter_by(team_code=team_code).first():
            team_code = str(uuid.uuid4())[:8].upper()
        
        new_class = ClassRoom(
            name=form.name.data,
            description=form.description.data,
            team_code=team_code,
            creator_id=current_user.id
        )
        
        try:
            db.session.add(new_class)
            db.session.commit()
            flash(f'Class created successfully! Team Code: {team_code}', 'success')
            return redirect(url_for('dashboard'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while creating the class.', 'error')
    
    return render_template('create_class.html', form=form)

@app.route('/join-class', methods=['GET', 'POST'])
@login_required
def join_class():
    if current_user.role != 'student':
        flash('Only students can join classes', 'error')
        return redirect(url_for('dashboard'))
    
    form = JoinClassForm()
    if form.validate_on_submit():
        # Find class by team code
        classroom = ClassRoom.query.filter_by(team_code=form.team_code.data.upper()).first()
        
        if not classroom:
            flash('Invalid team code', 'error')
            return render_template('join_class.html', form=form)
        
        # Check if already enrolled
        existing_enrollment = ClassEnrollment.query.filter_by(
            student_id=current_user.id, 
            classroom_id=classroom.id
        ).first()
        
        if existing_enrollment:
            flash('You are already enrolled in this class', 'warning')
            return redirect(url_for('dashboard'))
        
        # Create enrollment
        enrollment = ClassEnrollment(
            student_id=current_user.id,
            classroom_id=classroom.id
        )
        
        try:
            db.session.add(enrollment)
            db.session.commit()
            flash(f'Successfully joined class: {classroom.name}', 'success')
            return redirect(url_for('dashboard'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while joining the class.', 'error')
    
    return render_template('join_class.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)