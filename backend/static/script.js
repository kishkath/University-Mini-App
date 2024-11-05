document.addEventListener('DOMContentLoaded', function() {
    const issueForm = document.getElementById('issueForm');
    const issuesList = document.getElementById('issuesList');

    // Load existing issues
    fetchIssues();

    // Handle form submission
    issueForm.addEventListener('submit', async function(e) {
        e.preventDefault();

        const formData = {
            name: document.getElementById('name').value,
            studentId: document.getElementById('studentId').value,
            email: document.getElementById('email').value,
            problem: document.getElementById('problem').value,
            solution: document.getElementById('solution').value
        };

        try {
            const response = await fetch('/submit_issue', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            if (response.ok) {
                alert('Issue submitted successfully!');
                issueForm.reset();
                fetchIssues();
            } else {
                alert('Error submitting issue');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error submitting issue');
        }
    });

    // Fetch and display issues
    async function fetchIssues() {
        try {
            const response = await fetch('/get_issues');
            const issues = await response.json();
            
            issuesList.innerHTML = issues.map(issue => `
                <div class="issue-card">
                    <h3>Issue by ${issue.name}</h3>
                    <p><strong>Student ID:</strong> ${issue.student_id}</p>
                    <p><strong>Email:</strong> ${issue.email}</p>
                    <p><strong>Problem:</strong> ${issue.problem}</p>
                    <p><strong>Suggested Solution:</strong> ${issue.solution}</p>
                    <p class="timestamp">Submitted on: ${new Date(issue.created_at).toLocaleString()}</p>
                </div>
            `).join('');
        } catch (error) {
            console.error('Error:', error);
            issuesList.innerHTML = '<p>Error loading issues</p>';
        }
    }
}); 