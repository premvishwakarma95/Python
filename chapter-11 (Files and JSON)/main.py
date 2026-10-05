# In Node.js, you use the fs module. In Python, basic file operations use the built-in open() function.
# Writing a text file
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Hello Prem!\n")
    file.write("I am learning Python.")
# Important: "w" creates the file if it does not exist. If it already exists, it clears its contents when opened.
# The "with" statement automatically closes the file when you leave its block, including when an exception occurs.



# Reading a text file
# Read the entire file: read()
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
# You can open and close a file manually:
file = open("notes.txt", "r", encoding="utf-8")
content = file.read()
file.close()



# Read one line: readline()
with open("notes.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    second_line = file.readline()
print(first_line, end="")
print(second_line, end="")
# Read all lines into a list: readlines()
with open("notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
print(lines)
# Output: ['Hello Prem!\n', 'I am learning Python.']



# 5. File modes - see in the Readme.md file
# "r" is the default mode:
# For binary files such as images, add "b": "rb" or "wb". Binary mode works with bytes and does not use encoding.



# 6. Appending to a file
# Use "a" to add content without clearing existing text:
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("\nNext, I will learn JSON.")
# write() does not add a newline automatically. You must include \n where needed.




# 10. Saving and reading JSON files
# Save Python data: json.dump()
import json

user = {
    "name": "Prem",
    "skills": ["React", "Node.js", "Python"],
    "is_learning": True
}

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, indent=4)
    # indent=4 formats the JSON with indentation so it is easier to read.

# Read saved data: json.load()
import json
with open("user.json", "r", encoding="utf-8") as file:
    user = json.load(file)
print(user["name"])
print(user["skills"])


# built-in modules - pathlib, json