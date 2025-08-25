import os
from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    full_abs_path = os.path.abspath(full_path)
    abs_path_working = os.path.abspath(working_directory)
    if not full_abs_path.startswith(abs_path_working):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory.'
    elif not os.path.isfile(full_abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    else:
        try:
            with open(full_abs_path, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                if len(file_content_string) == 10000:
                    file_content_string += "\n" + (f'[...File "{file_path}" truncated at 10000 characters]')
                return file_content_string
        except Exception as e:
            return f"Error: {e}"