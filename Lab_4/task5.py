#Read a .txt file and return the number of lines it contains.
#Examples:
#“file1.txt” → 12 lines
#“notes.txt” → 5 lines
#“data.txt” → 20 lines
#Write a Python function that performs the above  task.
def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return "File not found" 
#Example Usage:
print(count_lines_in_file("C:\\Users\\H P\\OneDrive\\Desktop\\AI Assisted Python Lab\\LAB_4\\task5_file.txt")) # Replace with your file path