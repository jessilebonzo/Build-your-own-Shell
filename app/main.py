import sys

def main():
    valid_commands = []

    while True:
        # Print the prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        try:
            # Read user input
            user_command = input().strip()

            # Check if the command is in the list of valid commands
            if user_command not in valid_commands:
                # Print the error message with a newline character
                print(f"{user_command}: command not found")
        except EOFError:
            # Handle end-of-file gracefully
            break

if __name__ == "__main__":
    main()
