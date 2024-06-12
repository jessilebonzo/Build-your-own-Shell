import sys

def main():
    builtins = ["echo", "exit", "type"]
    
    while True:
        
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        # Wait for user input
        full_command = input()
        command_array = full_command.split()
        command = command_array[0]
        
        if command == "exit":
            break
        elif command == "echo":
            print(" ".join(command_array[1:]))
        elif command == "type":
            evaled_command = command_array[1]
            if evaled_command in builtins:
                print(f"{evaled_command} is a shell builtin")
            else:
                print(f"{evaled_command} not found")
        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
