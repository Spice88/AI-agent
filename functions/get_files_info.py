import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    full_abs_path = os.path.abspath(full_path)
    abs_path_working = os.path.abspath(working_directory)
    print(f"Result for {directory} directory:")
    if not full_abs_path.startswith(abs_path_working):
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory.')
    elif not os.path.isdir(full_abs_path):
        print(f'Error: "{directory}" is not a directory')
    else:
        try:
            dir_contents = os.listdir(full_abs_path)
            output_string_list = []
            for element in dir_contents:
                info_string = f"{element}: file_size={os.path.getsize(os.path.join(full_abs_path, element))}, is_dir={os.path.isdir(os.path.join(full_abs_path, element))}"
                output_string_list.append(info_string)
            final_output_string = "\n".join(output_string_list)
            print(final_output_string)
        except Exception as e:
            print(f"Error: {e}")
