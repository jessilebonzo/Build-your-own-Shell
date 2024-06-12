import sys


def main():

    valid_commands = []
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    #print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")
    # sys.stdout.flush()
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
    # Wait for user input
        user_command = input()
        if user_command not in valid_commands:
            output = "$invalid_command_1: command not found\n"
            print(output, end='')



if __name__ == "__main__":
    main()
