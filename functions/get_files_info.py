import os
import time

def get_files_info(working_directory, directory=None):
    
    target_directory = os.path.abspath(os.path.join(working_directory, directory))

    # Check if the directory is within the working directory
    if not target_directory.startswith(os.path.abspath(working_directory)):
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"
    
    # Check if the directory exists
    if not os.path.exists(target_directory):
        return f"Error: '{directory}' does not exist"

    # If the directory argument is not a directory
    if not os.path.isdir(target_directory):
        return f"Error: '{directory}' is not a directory"
    
    try:
        files_info = []
        for entry in os.listdir(target_directory):
            entry_path = os.path.join(target_directory, entry)
            if os.path.isfile(entry_path):
                files_info.append(f"{entry}: file_size={os.path.getsize(entry_path)} bytes, is_dir={False}")
            elif os.path.isdir(entry_path):
                files_info.append(f"{entry}: file_size=0 bytes, is_dir={True}")
            else:
                continue
        return "\n".join(files_info)
    
    except Exception as e:
        return f"Error: {str(e)}"