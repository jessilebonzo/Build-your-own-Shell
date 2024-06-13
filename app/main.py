import os
import subprocess
import sys
from typing import Optional

def locate_executable(command: str) -> Optional[str]:
    for directory in os.environ['PATH'].split(os.pathsep):
        if os.path.isdir(directory):
            executable_path = os.path.join(directory, command)
            if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                return executable_path
    return None

def main():
    builtins = {
        "echo": lambda args: print(" ".join(args)),
        "exit": lambda args: exit(int(args[0]) if args else 0),
        "type": lambda args: print(f"{args[0]} is a shell builtin" if args[0] in builtins else (f"{args[0]} is {locate_executable(args[0])}" if locate_executable(args[0]) else f"{args[0]} not found"))
    }

    while True:
        command_line = input("$ ").strip().split()
        if not command_line:
            continue
        command, *args = command_line

        if command in builtins:
            builtins[command](args)
        elif executable := locate_executable(command):
            subprocess.run([executable, *args])
        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
