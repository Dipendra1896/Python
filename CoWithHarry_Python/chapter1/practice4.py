import os

def print_directory_contents(path):
    # Check if the path is a directory
    if os.path.isdir(path):
        # List all files and directories within the specified path
        contents = os.listdir(path)
        for item in contents:
            print(item)
    else:
        print(f"{path} is not a valid directory.")

# Example usage:
directory_path = '/home/dipendra/Documents/4th sem'  # Replace with your directory path
print(f"Contents of directory: {directory_path}")
print_directory_contents(directory_path)
