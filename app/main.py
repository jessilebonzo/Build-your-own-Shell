import sys

def main():

    while True:

        sys.stdout.write("$ ")
        sys.stdout.flush()
        if bulletin_commands := input().strip():
            if bulletin_commands == "exit 0":
                sys.exit(0)
        if bulletin_commands in bulletin_commands:
            print(f"{bulletin_commands} is a {bulletin_commands[bulletin_commands]}")
    else:
        print(f"{bulletin_commands}: not found")

                
if __name__ == "__main__":
    main()