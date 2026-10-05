# 1. What is a module? - it's same as components and packages in react.
# A module is a Python file containing reusable code, such as functions and variables.
# For example, you could create `calculator.py` containing calculation functions and use them in `main.py`.
# It’s similar to importing code from another file in JavaScript.
# Unlike JavaScript, you don’t need to export each function. Functions defined at module level are available through the module.



# 2. Using modules that come with Python
# Python includes a standard library: modules you can use without installing anything like fs in nodejs.
# For example, math provides mathematical functions:
import math   # math is the module.

print(math.sqrt(25))   # 5.0    ---   sqrt is a function inside it. 25 is the argument.
print(math.floor(4.9)) # 4
print(math.ceil(4.1))  # 5
print(math.pi)        # 3.141592653589793



# 3. Different ways to import
import math                             # Import the whole module:
from math import sqrt                   # Import a specific function:
import math as m                        # Give the module an alias:
from math import sqrt as square_root    # Give a function an alias:



# 4. Create your own module - see in files
# Create two files in the same folder:
# File                            Purpose 
# `calculator.py`               Contains reusable functions
# `main.py                      Imports and uses them #



# 5. What is a package?
# A package organizes related modules together.
# For a simple example, create a folder named utils containing these files:
# File path                             Contents 
#| `utils/__init__.py`                   Leave empty 
#| `utils/calculator.py`                 Your `add()` and `subtract()` functions 
#| `main.py`                             Your main program, outside `utils` 

# In main.py:
# from utils.calculator import add
# print(add(10, 20))  # 30
# Here:
# - utils is the package.
# - calculator is the module.
# - add is the function.



# 6. What is pip?
# pip installs third-party Python packages. It plays a similar role to npm install.
# commands
# Install a package
# python -m pip install requests

# List installed packages
# python -m pip list

# Show package details
# python -m pip show requests

# Uninstall a package
# python -m pip uninstall requests

# Node.js                                                           # Python
# A JavaScript module                                               # A Python module, usually a .py file
# import ... from ...                                               # import ... or from ... import ...
# npm install axios                                                 # python -m pip install requests
# node_modules holds project dependencies                           # .venv contains an isolated Python environment and its packages
# package.json declares dependencies and project metadata           # pyproject.toml can declare dependencies and project metadata
# package-lock.json records dependency resolution                   # pip freeze records installed versions, but isn’t a full equivalent



# 7. Virtual environments
# A virtual environment is an isolated Python environment that allows you to manage dependencies for a specific project 
# without affecting other projects or the system Python installation. It’s similar to using virtual environments in Node.js with tools like nvm or virtualenv.
# Commands to create and activate a virtual environment:
# Create a virtual environment
# python -m venv myenv  
# Activate the virtual environment
# Windows: myenv\Scripts\activate
# macOS/Linux: source myenv/bin/activate
# Deactivate the virtual environment
# deactivate


# see in Readme file