import sys

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    while True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input()
        if command == "exit 0":
            break
        print(f"{command}: command not found")
        
if __name__ == "__main__":
    main()