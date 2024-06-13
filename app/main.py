import os
import sys

def main():
    builtin_cmds = ["echo", "exit", "type", "cd"]
    PATH = os.environ.get("PATH", "")
    
    while True:
        
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_input = input().strip()

        if user_input == "exit 0":
            break

        if user_input.startswith("echo"):
            content = user_input.split(" ", 1)
            sys.stdout.write(content[1] + "\n" if len(content) > 1 else "\n")
            sys.stdout.flush()
            continue

        if user_input.startswith("type"):
            cmd = user_input.split(" ")[1]
            cmd_path = next(
                (
                    f"{path}/{cmd}"
                    for path in PATH.split(":")
                    if os.path.isfile(f"{path}/{cmd}")
                ),
                None,
            )
            if cmd in builtin_cmds:
                sys.stdout.write(f"{cmd} is a shell builtin\n")
            elif cmd_path:
                sys.stdout.write(f"{cmd} is {cmd_path}\n")
            else:
                sys.stdout.write(f"{cmd}: not found\n")
            sys.stdout.flush()
            continue

        if user_input.startswith("cd"):
            directory = user_input.split(" ", 1)[1]
            try:
                os.chdir(os.path.expanduser(directory))
            except OSError:
                sys.stdout.write(f"cd: {directory}: No such file or directory\n")
            sys.stdout.flush()
            continue

        # Check if the command is a file in the current directory or PATH and execute it
        cmd_parts = user_input.split(" ")
        cmd = cmd_parts[0]
        cmd_path = next(
            (
                path
                for path in (['.'] + PATH.split(":"))
                if os.path.isfile(f"{path}/{cmd}")
            ),
            None
        )
        if cmd_path:
            os.system(user_input)
        else:
            sys.stdout.write(f"{user_input}: command not found\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
