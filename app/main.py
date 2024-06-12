import sys


def main():

    #valid_commands = []
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    #print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")
    # sys.stdout.flush()
    #while True:
    sys.stdout.write("$ ")
    sys.stdout.flush()
    # Wait for user input
    command = input()
    match command:
        case "Jessile":
            print("hello, Jessile!")
        case _:
        #if user_command not in valid_commands:
            print(f"${command}: command not found")
            #continue
    main()

if __name__ == "__main__":
    main()
