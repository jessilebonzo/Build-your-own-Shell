import sys
import os

def find_in_path(param):
  """
  Searches for a given parameter in the system's PATH environment variable.

  Args:
      param (str): The parameter to search for.

  Returns:
      str: The full path to the parameter if found, otherwise None.
  """
  path = os.environ.get('PATH', '')  # Handle missing PATH environment variable
  print("Path:", path)
  print(f"Param: {param}")

  for directory in path.split(":"):
    try:
      for (dirpath, dirnames, filenames) in os.walk(directory):
        if param in filenames:
          return os.path.join(dirpath, param)  # Use os.path.join for safer path construction
    except OSError as e:
      print(f"Error accessing directory: {directory} ({e})")  # Handle directory access errors

  return None

def main():
  """
  Simple interactive shell that allows users to enter commands.
  """
  while True:
    sys.stdout.write("$ ")
    sys.stdout.flush()

    command = input()
    args = command.split()  # Split into command and arguments for better handling

    if not args:
      continue  # Skip empty lines

    match args[0]:
      case "exit" | "0":
        exit(0)
      case "echo":
        print(" ".join(args[1:]))  # Print remaining arguments
      case "type":
        if len(args) == 1:
          print(f"{args[0]}: command not found")  # Handle 'type' without arguments
        else:
          location = find_in_path(args[1])
          if location:
            print(f"{args[1]} is {location}")
          else:
            print(f"{args[0]} not found")  # More accurate message for 'type'
      case _:
        location = find_in_path(args[0])  # Search for executables with arguments
        if location:
          try:
            os.execv(location, [location] + args[1:])  # Use os.execv for better process replacement
          except OSError as e:
            print(f"Error executing {location}: {e}")  # Handle execution errors
        else:
          print(f"{command}: command not found")

if __name__ == "__main__":
  main()



