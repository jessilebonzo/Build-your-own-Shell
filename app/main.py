import sys
import os

def search_executable(command, path_directories):
    for directory in path_directories:
        executable_path = os.path.join(directory, command)
        if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
            return executable_path
    return None

def type_command(command, path_directories):
    executable_path = search_executable(command, path_directories)
    if executable_path:
        print(f"{command} is {executable_path}")
    else:
        print(f"{command}: not found")

def main():
    # Get the value of the PATH environment variable and split it into individual directories
    path_env = os.getenv("PATH")
    path_directories = path_env.split(":") if path_env else []

    # Test the type command with sample commands
    type_command("ls", path_directories)
    type_command("abcd", path_directories)
    type_command("missing_cmd", path_directories)

if __name__ == "__main__":

    main()
