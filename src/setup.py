import os
import shutil
import stat
import sys

def make_executable(file_path):
    """Make the file executable."""
    st = os.stat(file_path)
    os.chmod(file_path, st.st_mode | stat.S_IEXEC)

def move_to_usr_local_bin(script_path, keyword_name):
    """Move the script to /usr/local/bin and rename it."""
    destination = f"/usr/local/bin/{keyword_name}"
    
    try:
        # Copy the script to /usr/local/bin
        shutil.copy(script_path, destination)
        print(f"Copied {script_path} to {destination}")

        # Make the script executable
        make_executable(destination)
        print(f"Made {destination} executable.")

    except PermissionError:
        print("Permission denied! Try running the script with `sudo`.")
        sys.exit(1)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    print(f"Keyword '{keyword_name}' is now ready to use.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python setup_keyword.py <path_to_script> <keyword_name>")
        sys.exit(1)

    script_path = sys.argv[1]
    keyword_name = sys.argv[2]

    if not os.path.isfile(script_path):
        print(f"Error: {script_path} does not exist.")
        sys.exit(1)

    if not os.access("/usr/local/bin", os.W_OK):
        print("Error: You do not have write permission for /usr/local/bin.")
        print("Try running the script with `sudo`.")
        sys.exit(1)

    move_to_usr_local_bin(script_path, keyword_name)
