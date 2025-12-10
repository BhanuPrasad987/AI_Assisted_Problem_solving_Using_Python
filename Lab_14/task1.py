#generate a simple HTML homepage for a "Student Info Portal" with a header, navigation menu, and footer.
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Info Portal</title>
</head>
<body>
    <header>
        <h1>Student Info Portal</h1>
    </header>
    <nav>
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">Students</a></li>
            <li><a href="#">Courses</a></li>
            <li><a href="#">About</a></li>
        </ul>
    </nav>
    <footer>
        <p>&copy; 2024 Student Info Portal</p>
    </footer>
</body>
</html>
"""
with open("student_info_portal.html", "w") as file:
    file.write(html_content)
# This code creates a simple HTML file for a Student Info Portal with a header, navigation menu, and footer.
# The HTML content is stored in the variable `html_content` and then written to a file named "student_info_portal.html".
