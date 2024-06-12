import sys
import os

def main():
    builtin_cmds = ["echo", "exit", "type"]
    PATH = os.environ.get("PATH").split(":")  # Split PATH into individual directories

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        user_input = input()
        
        if user_input == "exit 0":
            break

        if user_input.startswith("echo"):
            content = user_input.split(" ", 1)
            sys.stdout.write(content[1] + "\n" if len(content) > 1 else "\n")
            sys.stdout.flush()
            continue

        if user_input.startswith("type"):
            cmd = user_input.split(" ")[1]

            # Search for command in each directory in PATH
            cmd_path = None
            for directory in PATH:
                if os.path.isfile(f"{directory}/{cmd}") and os.access(f"{directory}/{cmd}", os.X_OK):
                    cmd_path = f"{directory}/{cmd}"
                    break

            # Print result
            if cmd in builtin_cmds:
                sys.stdout.write(f"{cmd} is a shell builtin\n")
            elif cmd_path:
                sys.stdout.write(f"{cmd} is {cmd_path}\n")
            else:
                sys.stdout.write(f"{cmd} not found\n")
            sys.stdout.flush()
            continue

        sys.stdout.write(f"{user_input}: command not found\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
