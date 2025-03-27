
def read_file_with_error_handling():
    filename = "file55"  # Updated filename to 'file55'

    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' not exist.")
    except PermissionError:
        print(f"Error: You do not have permission'{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_file_with_error_handling()
