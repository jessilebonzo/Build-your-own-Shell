import os
import sys
def main():
    builtin_cmds = ["echo", "exit", "type"]
    PATH = os.environ.get("PATH", "")
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
            else:
                print(f"{evaled_command} not found")
        else:
                sys.stdout.write(
                    f"{cmd}: not found\n"
                    if cmd_path is None
                    else f"{cmd} is {cmd_path}\n")
        sys.stdout.flush()
        continue

        sys.stdout.write(f"{user_input}: command not found\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
