import os
import subprocess
from typing import Optional

def find_executable(program: str) -> Optional[str]:
  
  for directory in os.environ['PATH'].split(":"):
    if os.path.isfile(os.path.join(directory, program)):
      return os.path.join(directory, program)
  return None

def execute_program(program: str, *args):
  
  try:
    result = subprocess.run([program, *args], capture_output=True, text=True)
    return result.stdout.strip()
  except subprocess.CalledProcessError:
    return None

def main():
  while True:
    print("$ ", end="")
    command = input().strip()
    if not command:
      continue

    # Built-in commands
    if command in ("exit", "0"):
      exit(0)
    elif command.startswith("echo"):
      print(command.split()[1:])
    elif command.startswith("type"):
      program = command.split()[1]
      if program in ("echo", "exit", "type"):
        print(f"${program} is a shell builtin")
      else:
        location = find_executable(program)
        if location:
          print(f"${program} is {location}")
        else:
          print(f"${program} not found")

    # External programs
    else:
      executable = find_executable(command.split()[0])
      if executable:
        output = execute_program(executable, *command.split()[1:])
        if output:
          print(output)
      else:
        print(f"{command}: command not found")

if __name__ == "__main__":
  main()
