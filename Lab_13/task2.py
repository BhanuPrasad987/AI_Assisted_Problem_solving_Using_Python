#Refactor the following legacy Python function to include proper error handling.
#Use with open() for safe file handling and add try-except blocks to handle missing files, permission issues
# or read errors.

'''def read_file(filename):
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data'''
def read_file(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
        return data
    except FileNotFoundError:
        return "Error: The file was not found."
    except PermissionError:
        return "Error: You do not have permission to read this file."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
# Example usage:
print(read_file(r"C:\Users\H P\OneDrive\Desktop\AI Assisted Python Lab\AIAP_LAB_13\example.txt")) 
