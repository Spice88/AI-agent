import os
import subprocess
import sys

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    full_abs_path = os.path.abspath(full_path)
    abs_path_working = os.path.abspath(working_directory)
    if not full_abs_path.startswith(abs_path_working):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory.'
    if not os.path.exists(full_abs_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run([sys.executable, full_abs_path, *args], capture_output=True, cwd=abs_path_working, timeout=30, text=True)
        std_out = str(result.stdout)
        std_err = str(result.stderr)
        if result.returncode != 0:
            return f'Process exited with code {str(result.returncode)}\nSTDOUT: {std_out}\nSTDERR: {std_err}'
        elif not result.stderr and not result.stdout:
            return "No output produced."
        else:
            return f'STDOUT: \n{std_out}\nSTDERR: \n{std_err}'
    except Exception as e:
        return f"Error: executing Python file: {e}"
