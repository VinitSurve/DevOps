Absolutely. Since your Python learning is aimed toward **DevOps**, we’ll build this like a small real-world automation script rather than a random beginner exercise. We’ll keep the first version simple and only use concepts you’ve already covered.

# Python Mini Project — System Information Reporter

## 1. Understand the Project

### What are we building?

We are going to create a Python script that asks the operating system for some basic information and prints it nicely.

The program will report:

* Operating system
* Python version
* Current username
* Current working directory

Think of it as a **very small DevOps diagnostic script**.

For example, when you're troubleshooting a server, you might want to quickly know:

```text
Which OS am I on?
Which Python version is installed?
Which user is running this script?
Which directory am I currently in?
```

Instead of manually checking everything, Python can collect it for us.

### How does this connect to DevOps?

This is actually a useful pattern in DevOps:

```text
Python Script
     ↓
Collect system information
     ↓
Process information
     ↓
Display useful output
```

Later, the same idea can become:

```text
System Information
       ↓
CPU / RAM / Disk
       ↓
Running Processes
       ↓
Network Information
       ↓
Logs
       ↓
JSON Report
       ↓
CLI Tool
```

That's how a simple Python script can gradually become an actual **DevOps automation utility**.

---

# 2. Requirements

## Software

You need:

* Python 3
* A code editor such as VS Code
* Terminal / Command Prompt

You don't need any external Python packages for this version.

We'll use Python's **built-in modules**.

### Python version

Python **3.8+** is more than enough.

Check your Python installation:

### Windows

```bash
python --version
```

If that doesn't work:

```bash
py --version
```

### Linux/macOS

```bash
python3 --version
```

You should see something like:

```text
Python 3.12.5
```

---

# 3. Project Structure

Keep the project extremely simple:

```text
system-information-reporter/
│
└── system_info.py
```

That's it.

### `system_info.py`

This is our main Python program.

It will:

1. Import required modules
2. Collect system information
3. Store the information in variables
4. Display the information

We don't need multiple files yet.

For a beginner project, creating 10 files for a 30-line script would just be over-engineering.

---

# 4. Build It Step-by-Step

## Step 1 — Create the project folder

Create a folder called:

```text
system-information-reporter
```

Open that folder in VS Code.

Then create:

```text
system_info.py
```

---

# Step 2 — Import the modules

At the top of `system_info.py`, write:

```python
import os
import platform
import getpass
import sys
```

### What are these?

We are importing Python's built-in modules.

### `os`

Used for interacting with the operating system.

We'll use it to get the current working directory.

```python
os.getcwd()
```

### `platform`

Used to get information about the operating system and Python environment.

We'll use:

```python
platform.system()
```

### `getpass`

We'll use it to find the username running the program.

```python
getpass.getuser()
```

### `sys`

Provides information about the Python interpreter.

We'll use:

```python
sys.version
```

So we're already practicing one of the important Python concepts:

**Importing modules.**

---

# Step 3 — Get the operating system

Add:

```python
operating_system = platform.system()
```

Now `operating_system` contains something like:

```text
Linux
```

or:

```text
Windows
```

or:

```text
Darwin
```

for macOS.

### Why a variable?

Instead of repeatedly calling:

```python
platform.system()
```

we store the result:

```python
operating_system
```

Now we can easily use it later.

---

# Step 4 — Get the Python version

Add:

```python
python_version = platform.python_version()
```

This might return:

```text
3.12.5
```

We store that value inside:

```python
python_version
```

---

# Step 5 — Get the current username

Add:

```python
current_user = getpass.getuser()
```

For example:

```text
vinit
```

The exact result depends on which user is running the script.

---

# Step 6 — Get the current working directory

Add:

```python
working_directory = os.getcwd()
```

This returns the directory from which the Python program is currently running.

For example:

```text
/home/vinit/system-information-reporter
```

On Windows, you might see something like:

```text
C:\Users\Vinit\system-information-reporter
```

This is particularly useful in scripting and automation because **the current working directory matters a lot when dealing with files and commands**.

---

# Step 7 — Display a heading

Now let's make the output readable.

Add:

```python
print("==============================")
print("   SYSTEM INFORMATION")
print("==============================")
```

This gives us:

```text
==============================
   SYSTEM INFORMATION
==============================
```

---

# Step 8 — Display the information

Now add:

```python
print()
print("Operating System :", operating_system)
print("Python Version   :", python_version)
print("Current User     :", current_user)
print("Working Directory:", working_directory)
```

The `print()` by itself creates an empty line.

---

# Step 9 — Put everything together

Your first working version should now look like this:

```python
import os
import platform
import getpass
import sys

operating_system = platform.system()
python_version = platform.python_version()
current_user = getpass.getuser()
working_directory = os.getcwd()

print("==============================")
print("   SYSTEM INFORMATION")
print("==============================")

print()
print("Operating System :", operating_system)
print("Python Version   :", python_version)
print("Current User     :", current_user)
print("Working Directory:", working_directory)
```

But there's one small issue.

We imported `sys`, but we aren't actually using it.

That's unnecessary.

So let's remove it.

---

# 5. Complete Working Code

Create `system_info.py` with this code:

```python
import os
import platform
import getpass

# Get system information
operating_system = platform.system()
python_version = platform.python_version()
current_user = getpass.getuser()
working_directory = os.getcwd()

# Display system information
print("==============================")
print("   SYSTEM INFORMATION")
print("==============================")

print()
print("Operating System :", operating_system)
print("Python Version   :", python_version)
print("Current User     :", current_user)
print("Working Directory:", working_directory)
```

That's our complete beginner version.

Notice that we're deliberately **not** using:

* classes
* decorators
* external packages
* complex error handling
* command-line frameworks
* JSON
* logging
* advanced functions

Those can come later.

Right now, the goal is to understand:

```text
import
   ↓
module
   ↓
function call
   ↓
variable
   ↓
print()
```

---

# 6. How to Run

Open your terminal inside the project folder.

You should be inside:

```text
system-information-reporter
```

## Windows

Run:

```bash
python system_info.py
```

If necessary:

```bash
py system_info.py
```

## Linux/macOS

Run:

```bash
python3 system_info.py
```

---

# 7. Example Run

On a Linux machine, you might get:

```text
==============================
   SYSTEM INFORMATION
==============================

Operating System : Linux
Python Version   : 3.12.5
Current User     : vinit
Working Directory: /home/vinit/system-information-reporter
```

On Windows, the output could be:

```text
==============================
   SYSTEM INFORMATION
==============================

Operating System : Windows
Python Version   : 3.12.5
Current User     : Vinit
Working Directory: C:\Users\Vinit\system-information-reporter
```

Your values will obviously be different.

---

# 8. Code Explanation

Let's understand the program properly.

## 1. Importing modules

```python
import os
import platform
import getpass
```

We're telling Python:

> "I want to use functionality provided by these built-in modules."

This is extremely common in real Python programs.

---

## 2. Getting OS information

```python
operating_system = platform.system()
```

Here:

```text
platform
   ↓
system()
   ↓
"Windows" / "Linux" / "Darwin"
   ↓
operating_system
```

`system()` is a **function call**.

The returned value gets stored inside the variable:

```python
operating_system
```

---

## 3. Getting Python version

```python
python_version = platform.python_version()
```

The function returns the Python version.

Example:

```text
3.12.5
```

Then:

```python
python_version
```

contains that value.

---

## 4. Getting username

```python
current_user = getpass.getuser()
```

Python asks the operating system for the username of the account running the program.

For example:

```text
vinit
```

---

## 5. Getting working directory

```python
working_directory = os.getcwd()
```

`getcwd()` means:

**Get Current Working Directory**

So:

```python
os.getcwd()
```

might return:

```text
C:\Users\Vinit\system-information-reporter
```

This is very important for DevOps and automation scripts.

For example, imagine a script does:

```python
open("config.txt")
```

Python will look for `config.txt` relative to the current working directory.

So understanding the current directory becomes important when writing automation scripts.

---

## 6. Printing the results

```python
print("Operating System :", operating_system)
```

Python prints both the label and the variable.

For example:

```text
Operating System : Linux
```

The colon is simply part of the text we're printing.

---

# Where are the Python concepts being practiced?

| Python Concept          | Where we use it          |
| ----------------------- | ------------------------ |
| Running Python programs | `python system_info.py`  |
| Importing modules       | `import os`              |
| Variables               | `operating_system = ...` |
| Function calls          | `platform.system()`      |
| Printing                | `print()`                |
| Strings                 | `"SYSTEM INFORMATION"`   |
| Basic program flow      | Top-to-bottom execution  |

The important thing is that we're not just memorizing:

> "A function is something that does something."

We're actually doing:

```python
platform.system()
```

and seeing the result.

---

# Common Beginner Mistakes

## Mistake 1 — Forgetting parentheses

Wrong:

```python
platform.system
```

Correct:

```python
platform.system()
```

The first refers to the function itself.

The second **calls** the function.

---

## Mistake 2 — Wrong module name

Wrong:

```python
import platforms
```

Correct:

```python
import platform
```

Python module names must be correct.

---

## Mistake 3 — Running from the wrong directory

Suppose your file is:

```text
C:\Projects\system-information-reporter\system_info.py
```

But your terminal is somewhere else.

You might get:

```text
can't open file
```

Move into the project directory first:

```bash
cd system-information-reporter
```

Then:

```bash
python system_info.py
```

---

## Mistake 4 — Thinking the working directory is always the script's directory

This is an important one.

These are **not necessarily the same thing**:

```text
Location of Python file
```

and

```text
Current Working Directory
```

`os.getcwd()` tells you the **current working directory**, not simply "where the Python file is located."

That's a useful distinction to understand early because it will matter a lot in automation.

---

# 9. Practice Tasks

Don't immediately move on after copying the code. Modify it yourself.

## Task 1 — Add the hostname

Find a way to display the computer's hostname.

Hint:

```python
platform.
```

Search the Python documentation or use:

```python
dir(platform)
```

Try to figure it out yourself first.

Expected output:

```text
Hostname         : MY-PC
```

---

## Task 2 — Add the processor

Add information about the processor.

Expected:

```text
Processor        : ...
```

Hint:

```python
platform.processor()
```

This one should be easy.

---

## Task 3 — Create a function

Currently our program directly executes everything.

Try moving the display logic into:

```python
def display_information():
    ...
```

Then call:

```python
display_information()
```

This introduces a useful programming habit:

```text
collect information
       ↓
function
       ↓
display information
```

---

## Task 4 — Add system architecture

Try displaying whether the machine is 32-bit or 64-bit.

Hint:

```python
platform.architecture()
```

---

## Task 5 — Your first DevOps upgrade

Create a new section:

```text
==============================
   ENVIRONMENT CHECK
==============================
```

Then display:

```text
Python Installed : Yes
Current User     : ...
Operating System : ...
```

Later, this could evolve into a real **environment validation script** used before deploying an application.

---

# 10. What You Learned

### Python concepts

You practiced:

* Running Python scripts
* Importing modules
* Built-in modules
* Variables
* Strings
* Function calls
* `print()`
* Basic program flow

### Programming concepts

You also practiced the basic pattern:

```text
Get data
   ↓
Store data
   ↓
Display data
```

That's a fundamental programming pattern.

### DevOps relevance

More importantly, you've started learning a pattern you'll repeatedly use in DevOps:

```text
Python
  ↓
Interact with operating system
  ↓
Collect information
  ↓
Automate a task
  ↓
Produce useful output
```

Today's script is tiny, but its **direction is correct**.

A realistic evolution could be:

```text
VERSION 1
System information
       ↓
VERSION 2
CPU + RAM + Disk
       ↓
VERSION 3
Network information
       ↓
VERSION 4
Process monitoring
       ↓
VERSION 5
JSON output
       ↓
VERSION 6
Logging
       ↓
VERSION 7
Command-line arguments
       ↓
VERSION 8
Reusable DevOps CLI tool
```

That is the mindset I’ll use for your future projects too: **start at your current Python level, build something that works, then evolve it toward an actual DevOps use case.**
