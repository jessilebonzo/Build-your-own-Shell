import sys

def main():
    valid_commands = []

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        try:
            # Wait for user input
            user_command = input().strip()
            if user_command not in valid_commands:
                print(f"${user_command}: command not found\n")
        except EOFError:
            break

if __name__ == "__main__":
    main()
