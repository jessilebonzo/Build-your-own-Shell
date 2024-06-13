import sys
import os

def find_in_path(param):
    for directory in os.environ['PATH'].split(":"):
        if os.path.isdir(directory):  # Ensure the directory exists
            for root, _, files in os.walk(directory):
                if param in files:
                    return os.path.join(root, param)
    return None

def main():

    
    while True:
        command = input("$ ").strip().split()
        if not command:
            continue
        cmd, *args = command

        if cmd == "exit" and args == ["0"]:
            exit(0)
        elif cmd == "echo":
            print(" ".join(args))
        elif cmd == "type":
            if args and args[0] in ["echo", "exit", "type"]:
                print(f"{args[0]} is a shell builtin")
            else:
                location = find_in_path(args[0])
                print(f"{args[0]} is {location}" if location else f"{' '.join(args)} not found")
        else:
            if os.path.isfile(cmd):
                os.system(" ".join(command))
            else:
                print(f"{cmd}: command not found")

if __name__ == "__main__":
    main()
