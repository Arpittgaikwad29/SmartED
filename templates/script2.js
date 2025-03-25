// Function to update content dynamically
function showSection(section) {
    const contentArea = document.getElementById("content-area");

    // Clear previous content
    contentArea.innerHTML = "";

    if (section === "Dashboard") {
        contentArea.innerHTML = `
        <h1>Dashboard Overview</h1>
        <div class="dashboard-stats">
            <div class="stat-card">
                <div>Total Assignments</div>
                <div style="font-size: 24px; color: #2563eb;">25</div>
            </div>
            <div class="stat-card">
                <div>Average Grade</div>
                <div style="font-size: 24px; color: #16a34a;">85% <small>B+</small></div>
            </div>
            <div class="stat-card">
                <div>Pending Reviews</div>
                <div style="font-size: 24px; color: #dc2626;">4 <small>Due this week</small></div>
            </div>
        </div>
        
        <div class="quick-actions">
            <button class="upload-btn">📤 Upload Assignment</button>
            <button class="feedback-btn">💬 Show Feedback</button>
            <button class="analytics-btn">📊 View Analytics</button>
        </div>
        
        
        <div class="content-grid">
            <div class="assignments-list">
                <h2>Recent Assignments</h2>
                <div class="assignment-item">
                    <div>
                        <div>Mathematics Quiz #3</div>
                        <small>Due Mar 15, 2025</small>
                    </div>
                    <div class="status-badge status-pending">Pending</div>
                </div>
                <div class="assignment-item">
                    <div>
                        <div>History Essay</div>
                        <small>Due Mar 18, 2025</small>
                    </div>
                    <div class="status-badge status-progress">In Progress</div>
                </div>
                <div class="assignment-item">
                    <div>
                        <div>Science Project</div>
                        <small>Due Mar 20, 2025</small>
                    </div>
                    <div class="status-badge status-not-started">Not Started</div>
                </div>
            </div>
            
            <div class="feedback-section">
                <h2>History Essay Feedback</h2>
                <div>
                    <h3 style="color: #16a34a;">Strengths</h3>
                    <ul>
                        <li>Clear thesis statement</li>
                        <li>Good use of primary sources</li>
                    </ul>
                    
                    <h3 style="color: #dc2626;">Areas for Improvement</h3>
                    <ul>
                        <li>Expand on counterarguments</li>
                        <li>Proofread for grammatical errors</li>
                    </ul>
                    
                    <h3 style="color: #2563eb;">Suggestions</h3>
                    <ul>
                        <li>Revise conclusion</li>
                        <li>Add additional references</li>
                    </ul>
                </div>
            </div>
        </div>
        `;
    } 
    else if (section === "Feedback") {
        contentArea.innerHTML = `
        <h1>Personalized Student Feedback</h1>
            <div class="feedback-container">
                <div class="feedback-form">
                    <select>
                        <option>Select a student...</option>
                    </select>
                    <select>
                        <option>Select an assignment...</option>
                    </select>
                </div>
                
                <div class="text-formatting">
                    <button>B</button>
                    <button>I</button>
                    <button>=</button>
                </div>
                
                <textarea placeholder="Type your feedback here..." rows="6"></textarea>
                
                <div class="rating">
                    <span>☆</span>
                    <span>☆</span>
                    <span>☆</span>
                    <span>☆</span>
                    <span>☆</span>
                </div>
                
                <div>
                    <span>📎 Attach Files</span>
                    <button class="submit-btn">Submit Feedback</button>
                </div>
            </div>
            
            <div class="previous-feedback">
                <div class="previous-feedback-header">
                    <h2>Previous Feedback</h2>
                    <div>
                        <input type="text" placeholder="Search...">
                        <select>▼</select>
                    </div>
                </div>
                
                <table class="previous-feedback-table">
                    <thead>
                        <tr>
                            <th>Student Name</th>
                            <th>Assignment</th>
                            <th>Feedback</th>
                            <th>Date</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <img src="https://via.placeholder.com/30" alt="Profile" style="border-radius: 50%; margin-right: 10px;">
                                Sarah Johnson
                            </td>
                            <td>Math Quiz #3</td>
                            <td>Excellent work on the problem-solving...</td>
                            <td>Mar 15, 2025</td>
                            <td>
                                <div class="table-actions">
                                    <span>✏️</span>
                                    <span>🗑️</span>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>   
        `;
    } 
    else if (section === "Course") {
        contentArea.innerHTML = `
            <div class="course-card">
                <div class="course-header">
                    <div class="course-code ml-code">ML</div>
                    <div class="course-title">MachineLearning</div>
                    <div class="more-options">
                        <i class="fas fa-ellipsis-h"></i>
                    </div>
                </div>
                <div class="course-actions">
                    <div class="action-button">
                        <i class="fas fa-video action-button-icon"></i>
                    </div>
                    <div class="action-button">
                        <i class="fas fa-file-alt action-button-icon"></i>
                    </div>
                    <div class="action-button">
                        <i class="fas fa-folder action-button-icon"></i>
                    </div>
                </div>
            </div>

            <!-- Course Card 2 -->
            <div class="course-card">
                <div class="course-header">
                    <div class="course-code cc-code">CC</div>
                    <div class="course-title">CloudComputing</div>
                    <div class="more-options">
                        <i class="fas fa-ellipsis-h"></i>
                    </div>
                </div>
                <div class="course-actions">
                    <div class="action-button">
                        <i class="fas fa-video action-button-icon"></i>
                    </div>
                    <div class="action-button">
                        <i class="fas fa-file-alt action-button-icon"></i>
                    </div>
                    <div class="action-button">
                        <i class="fas fa-folder action-button-icon"></i>
                    </div>
                </div>
            </div>

            <!-- Course Card 3 -->
            <div class="course-card">
                <div class="course-header">
                    <div class="course-code dv-code">DV</div>
                    <div class="course-title">Devops</div>
                    <div class="more-options">
                        <i class="fas fa-ellipsis-h"></i>
                    </div>
                </div>
                <div class="course-actions">
                    <div class="action-button">
                        <i class="fas fa-video action-button-icon"></i>
                    </div>
                    <div class="action-button">
                        <i class="fas fa-file-alt action-button-icon"></i>
                    </div>
                    <div class="action-button">
                        <i class="fas fa-folder action-button-icon"></i>
                    </div>
                </div>
            </div>

            <!-- Course Card 4 -->
            <div class="course-card">
                <div class="course-header">
                    <div class="course-code cl-code">CL</div>
                    <div class="course-title">CyberLaw</div>
                    <div class="more-options">
                        <i class="fas fa-ellipsis-h"></i>
                    </div>
                </div>
                <div class="course-actions">
                    <div class="action-button">
                        <i class="fas fa-video action-button-icon"></i>
                    </div>
                    <div class="action-button">
                        <i class="fas fa-file-alt action-button-icon"></i>
                    </div>
                    <div class="action-button">
                        <i class="fas fa-folder action-button-icon"></i>
                    </div>
                </div>
            </div>

            <!-- Course Card 5 -->
            <div class="course-card">
                <div class="course-header">
                    <div class="course-code df-code">DF</div>
                    <div class="course-title">DigitalForensica</div>
                    <div class="more-options">
                        <i class="fas fa-ellipsis-h"></i>
                    </div>
                </div>
                <div class="course-actions">
                    <div class="action-button">
                        <i class="fas fa-video action-button-icon"></i>
                    </div>
                    <div class="action-button">
                        <i class="fas fa-file-alt action-button-icon"></i>
                    </div>
                    <div class="action-button">
                        <i class="fas fa-folder action-button-icon"></i>
                    </div>
                </div>
            </div>
            `;
    } 
    else if (section === "drive") {
        contentArea.innerHTML = `
            <h2>Drive</h2>
            <p>Access your uploaded files here.</p>
        `;
    } 
    else if (section === "settings") {
        contentArea.innerHTML = `
            <h2>Settings</h2>
            <p>Change your account preferences.</p>
        `;
    }
}
