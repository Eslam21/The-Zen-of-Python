Here's a simple "Hello, World!" example in C++ that you can run from Python using the `subprocess` module:

C++ code (hello.cpp):

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

Python code to compile and run the C++ code:

```python
import subprocess

# Compile the C++ code
subprocess.call(["g++", "hello.cpp", "-o", "hello"])

# Run the compiled C++ program
subprocess.call(["./hello"])
```

Make sure you have a C++ compiler (such as g++) installed on your system. This Python code will compile the "hello.cpp" program and execute it, displaying "Hello, World!" in the output.

Save the C++ code in a file named "hello.cpp," and the Python code in a file named "run_hello.py." Then, run the Python script:

```bash
python run_hello.py
```

The output should be "Hello, World!" from the C++ program.