// Function to update content dynamically
function showSection(section) {
    const contentArea = document.getElementById("content-area");

    // Clear previous content
    contentArea.innerHTML = "";

    if (section === "course") {
        contentArea.innerHTML = `
            <!-- Course Card 1 -->
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

            <!-- Course Card 6 -->
            <div class="course-card">
                <div class="course-header">
                    <div class="course-code md-code">MD</div>
                    <div class="course-title">MAD</div>
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

            <!-- Course Card 7 -->
            <div class="course-card">
                <div class="course-header">
                    <div class="course-code ml-code">ML</div>
                    <div class="course-title">ProjectManagement</div>
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

            <!-- Course Card 8 -->
            <div class="course-card">
                <div class="course-header">
                    <div class="course-code cc-code">CC</div>
                    <div class="course-title">ResearchMethlogy</div>
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

            <!-- Course Card 9 -->
            <div class="course-card">
                <div class="course-header">
                    <div class="course-code dv-code">DV</div>
                    <div class="course-title">Nanotechnology</div>
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

            <!-- Additional courses to match the image -->
            <div class="course-card">
                <div class="course-header">
                    <div class="course-code ml-code">ML</div>
                    <div class="course-title">SSEH</div>
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

            <div class="course-card">
                <div class="course-header">
                    <div class="course-code cc-code">CC</div>
                    <div class="course-title">ArtificialIntelligence</div>
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

            <div class="course-card">
                <div class="course-header">
                    <div class="course-code dv-code">DV</div>
                    <div class="course-title">ADSA</div>
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

            <!-- Bottom row courses -->
            <div class="course-card">
                <div class="course-header">
                    <div class="course-code ml-code">ML</div>
                    <div class="course-title">ComputerNetworks</div>
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

            <div class="course-card">
                <div class="course-header">
                    <div class="course-code ml-code">ML</div>
                    <div class="course-title">DBMS</div>
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

            <div class="course-card">
                <div class="course-header">
                    <div class="course-code ml-code">ML</div>
                    <div class="course-title">SSEH</div>
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
        `;
    } 
    else if (section === "assignments") {
        contentArea.innerHTML = `
        <div class="assignmentss">
            <div class="content-header">
                <h1 class="page-title">Assignment</h1>
                <div class="action-buttons">
                    <button class="filter-button">
                        <span class="filter-icon">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"></polygon>
                            </svg>
                        </span>
                        Filter
                    </button>
                    <button class="share-button">
                        <span>Share</span>
                    </button>
                    <div class="view-controls">
                        <div class="view-button active">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <line x1="8" y1="6" x2="21" y2="6"></line>
                                <line x1="8" y1="12" x2="21" y2="12"></line>
                                <line x1="8" y1="18" x2="21" y2="18"></line>
                                <line x1="3" y1="6" x2="3.01" y2="6"></line>
                                <line x1="3" y1="12" x2="3.01" y2="12"></line>
                                <line x1="3" y1="18" x2="3.01" y2="18"></line>
                            </svg>
                        </div>
                        <div class="view-button">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <rect x="3" y="3" width="7" height="7"></rect>
                                <rect x="14" y="3" width="7" height="7"></rect>
                                <rect x="14" y="14" width="7" height="7"></rect>
                                <rect x="3" y="14" width="7" height="7"></rect>
                            </svg>
                        </div>
                    </div>
                </div>
            </div>

            <div class="assignments-list">
                <div class="assignment-card">
                    <div class="subject-icon cc">CC</div>
                    <div class="assignment-details">
                        <div class="assignment-title">Assignment 8</div>
                        <div class="assignment-due">Due at 11:59</div>
                        <div class="assignment-subject">T.E CC</div>
                    </div>
                    <div class="assignment-points">10 points</div>
                </div>
                
                <div class="assignment-card">
                    <div class="subject-icon df">DF</div>
                    <div class="assignment-details">
                        <div class="assignment-title">Exp 10</div>
                        <div class="assignment-due">Due on 24th March</div>
                        <div class="assignment-subject">T.E DF</div>
                    </div>
                </div>
                
                <div class="assignment-card">
                    <div class="subject-icon ml">ML</div>
                    <div class="assignment-details">
                        <div class="assignment-title">Take at home test</div>
                        <div class="assignment-due">Due on sunday</div>
                        <div class="assignment-subject">T.E ML</div>
                    </div>
                </div>
            </div>
        </div>    
        `;
    } 
    else if (section === "messages") {
        contentArea.innerHTML = `
            <h2>Messages</h2>
            <p>No new messages.</p>
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
