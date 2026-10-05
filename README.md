# Python
- Python is the language and the Python interpreter runs it.
- Python is a programming language, just like JavaScript. You can use it to build backend APIs, automate tasks, work with data, and create AI applications.

## Chapter -1
- Topic: Setup and first program
- What we will learn - Python installation, terminal shell, `.py` files, `print()`, comments.
- Commands - Reference with JS.
```cmd
sudo apt update
sudo apt install nodejs npm
node --version
npm --version
node                                // this will open the node terminal then can do anything.
node index.js                       // command to run file

sudo apt install python3-full python3-pip
python3 --version
pip --version
python3                             // this will open python terminal
python3 hello.py                    // command to run file
```

## Chapter -2
- Topic: Variables and data types
- What we will learn - Variables, strings, integers, floats, booleans, `None`, and `type()`.
- Commands - Reference with JS.
```cmd
//  In JS
let name = "Prem";
let age = 22;

// In Python
name = "Prem"
age = 22

print(name)  # Prem
print(age)   # 22
```

## Chapter -3
- Topic: Operators and conversions
- What we will learn - Arithmetic, comparison and logical operators, type conversion, and user input.

## Chapter -4
- Topic: Strings
- What we will learn - Indexing, slicing, string methods, and f-strings compared with JavaScript template literals.

## Chapter -5
- Topic: Conditions
- What we will learn - Indentation, `if`, `elif`, `else`, and truthiness compared with JavaScript.

## Chapter -6
- Topic: Loops
- What we will learn - `for`, `while`, `range()`, `break`, and `continue`.

## Chapter -7
- Topic: Collections
- What we will learn - Lists, tuples, dictionaries, and sets compared with JavaScript arrays, objects, Maps, and Sets.
| Feature | List | Tuple | Dictionary |
|---|---|---|---|
| Example | `[10, 20]` | `(10, 20)` | `{"name": "Prem"}` |
| Stores | Items | Items | Key-value pairs |
| Access by | Index | Index | Key |
| Can change contents? | Yes | Items cannot be changed* | Yes |
| Duplicates | Allowed | Allowed | Keys must be unique |
| Typical use | A collection you edit | A fixed sequence | A record with named fields |

## Chapter -8
- Topic: Functions
- What we will learn - Defining functions, parameters, return values, default arguments, scope, `*args`, `**kwargs`, and lambdas.

## Chapter -9
- Topic: Modules and packages
- What we will learn - Imports, creating modules, pip, virtual environments, and dependency management compared with npm.
- Virtual Environment 
```cmd
# Once - .venv is a folder name can be changed.
python3 -m venv .venv

# Each new terminal session
source .venv/bin/activate

# Install whatever the project needs
python -m pip install requests

# Run your code
python main.py

# Run command to know how many packages installed and which version used
pip freeze

# command to store all installed packages with version in file
pip freeze > requirement.txt

# command to install all packages stored inside requirement.txt file
pip install -r requirement.txt
```

## Chapter -10
- Topic: Errors and debugging
- What we will learn - `try`, `except`, `else`, `finally`, raising exceptions, and debugging.
- Common exceptions
| Exception | Common cause | Example |
|---|---|---|
| `ValueError` | Valid type, unsuitable value | `int("hello")` |
| `TypeError` | Operation used with an unsuitable type | `"Age: " + 22` |
| `ZeroDivisionError` | Division by zero | `10 / 0` |
| `NameError` | Name has not been defined | `print(unknown_name)` |
| `IndexError` | Sequence index is out of range | `[10, 20][5]` |
| `KeyError` | Dictionary key is missing | `{"name": "Prem"}["age"]` |
| `ModuleNotFoundError` | Imported module cannot be found | `import missing_module` |

## Chapter -11
- Topic: Files and JSON
- What we will learn - Reading and writing files, working with paths, JSON, and CSV.
- File modes
| Mode | Purpose | If file is missing | If file exists |
|---|---|---|---|
| `"r"` | Read | Raises `FileNotFoundError` | Reads contents |
| `"w"` | Write | Creates file | Clears existing contents |
| `"a"` | Append | Creates file | Writes at the end |
| `"x"` | Create a new file | Creates file | Raises `FileExistsError` |

## Chapter -12
- Topic: Object-oriented programming
- What we will learn - Classes, instances, constructors, inheritance, properties, and composition compared with JavaScript classes.

## Chapter -13
- Topic: Python patterns
- What we will learn - Comprehensions, unpacking, sorting, mutability, and shallow and deep copying.

## Chapter -14
- Topic: Advanced Python
- What we will learn - Iterators, generators, decorators, and context managers.

## Chapter -15
- Topic: Type hints and testing
- What we will learn - Type annotations compared with TypeScript, data classes, unit tests, and mocking.

## Chapter -16
- Topic: Async and concurrency
- What we will learn - `async`/`await`, coroutines compared with JavaScript Promises, tasks, threads, and processes.

## Chapter -17
- Topic: Backend development
- What we will learn - HTTP requests, FastAPI compared with Express.js, request validation, databases, and authentication.

## Chapter -18
- Topic: Practical projects
- What we will learn - Building an automation script, a CRUD API, an AI integration, and deploying a Python application.