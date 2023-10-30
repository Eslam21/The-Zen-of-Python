import subprocess

# Compile the C++ code
subprocess.call(["g++", "hello.cpp", "-o", "hello"])

# # Run the compiled C++ program
# subprocess.call(["./hello"])


# Run the compiled C++ program and capture the output
output = subprocess.check_output(["./hello"], text=True) # if text = False it will output b'Hello, World!\r\n'

# Print the output
print(output)

# Now 'output' contains the output of the C++ program, which you can use as needed in your Python script
