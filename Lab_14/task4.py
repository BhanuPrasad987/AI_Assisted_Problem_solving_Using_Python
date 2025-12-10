# Generate a Flask application that:
# - Serves the HTML login form from task3.html
# - The form must contain username & password fields
# - Validate fields with JavaScript before submitting
# - On successful login, POST the form to Flask
# - Flask should print "Welcome <username>" after submission
# - Use templates/login.html for the form page

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')  # Fetch username
        return f"<h2>Welcome {username}</h2>"     # Display welcome message
    return render_template('task3.html')          # Load the form

if __name__ == '__main__':
    app.run(debug=True)
