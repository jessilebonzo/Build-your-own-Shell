import subprocess

def execute_program(program, arguments):
  """Executes a program with arguments.

  Args:
    program: The name of the program to execute.
    arguments: A list of arguments to pass to the program.

  Returns:
    The output of the program, or None if there was an error.
  """
  try:
    # Build the complete command list
    command = [program] + arguments
    # Use subprocess.run to execute the program with arguments
    # Capture the output and decode it as utf-8 for easier handling
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()
  except subprocess.CalledProcessError:
    return None

# Simulate the tester's behavior
program_name = "program_1234"
arguments = ["alice"]
output = execute_program(program_name, arguments)

# Print the output, simulating the shell's behavior
if output:
  print(output)
else:
  print("Error executing program.")
