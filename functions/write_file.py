import os

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    full_abs_path = os.path.abspath(full_path)
    abs_path_working = os.path.abspath(working_directory)
    if not full_abs_path.startswith(abs_path_working):
        print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory.')
    elif not os.path.exists(full_abs_path):
        final_path_to_create = os.path.join(abs_path_working, os.path.dirname(file_path))
        os.makedirs(final_path_to_create, exist_ok = True)
    try:
        with open(full_abs_path, "w") as f:
            f.write(content)
            print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    except Exception as e:
        print(f"Error: {e}")