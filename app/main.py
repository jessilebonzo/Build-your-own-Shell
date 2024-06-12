import sys


def main():

    #valid_commands = []
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    #print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")
    # sys.stdout.flush()
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
    # Wait for user input
        user_input = input()
        # user_input not in valid_commands:
        print(f"${user_input}: command not found")


if __name__ == "__main__":
    main()
