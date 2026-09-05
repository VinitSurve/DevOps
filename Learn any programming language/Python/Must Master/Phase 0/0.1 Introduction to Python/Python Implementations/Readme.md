# Python Mini Project — Python Environment Diagnostic Tool

This is a very good next step after the **System Health Checker**.

The previous project asked:

> "Is this machine/environment healthy?"

This one asks:

> **"Exactly what Python environment is my application running inside?"**

That distinction matters in DevOps because the same Python application can behave differently depending on the Python interpreter, executable, operating system, and architecture.

We'll keep this version **small and beginner-friendly**. No external packages, no JSON, no CLI frameworks, and no Docker detection yet.

---

# 1. Understand the Project

## What are we building?

We're creating a command-line Python script that reports details about the Python environment currently running the program.

When you run:

```bash
python environment_check.py
```

you'll get something like:

```text
=====================================
     PYTHON ENVIRONMENT CHECK
=====================================

Implementation : CPython
Version        : 3.14.0
Executable     : C:\Python314\python.exe
OS             : Windows
Architecture   : 64-bit

=====================================
```

The actual values will depend on your machine.

---

## Why is this useful in DevOps?

Suppose your application works on one machine but doesn't work on another.

You might discover:

```text
Machine A
Python 3.12
CPython
64-bit
Windows

Machine B
Python 3.10
CPython
64-bit
Linux
```

Now you have a clue.

Python environment information becomes particularly useful when troubleshooting:

* CI/CD failures
* deployment problems
* virtual environments
* Docker containers
* server configurations
* Python version incompatibilities

We're basically creating a tiny **environment diagnostic command**.

---

# 2. Requirements

You need:

* Python 3
* VS Code or another code editor
* Terminal / Command Prompt

### External packages?

**None.**

We'll use only Python's standard library:

```python
platform
sys
```

The `platform` module provides access to information about the underlying platform, while `sys` provides information and functionality related to the Python interpreter.

---

# 3. Project Structure

Keep it simple:

```text
python-environment-diagnostic/
│
└── environment_check.py
```

That's all we need.

### `environment_check.py`

This will:

1. Import the required modules.
2. Collect environment information.
3. Store the values in variables.
4. Display a formatted report.

No need for multiple files.

---

# 4. Build It Step-by-Step

## Step 1 — Create the project

Create:

```text
python-environment-diagnostic
```

Inside it create:

```text
environment_check.py
```

---

# Step 2 — Import the modules

At the top of the file:

```python
import platform
import sys
```

We're importing two standard-library modules.

---

## Why `platform`?

We'll use it for:

* Python implementation
* operating system
* machine architecture

For example:

```python
platform.python_implementation()
```

might return:

```text
CPython
```

and:

```python
platform.system()
```

might return:

```text
Windows
```

The `platform` module is specifically designed to retrieve identifying information about the platform on which Python is running.

---

## Why `sys`?

We'll use `sys` to find:

* Python version
* Python executable

For example:

```python
sys.version
```

and:

```python
sys.executable
```

`sys.executable` gives the path to the executable binary of the Python interpreter currently running the program.

---

# Step 3 — Get the Python implementation

Add:

```python
python_implementation = platform.python_implementation()
```

For most normal Python installations, you'll get:

```text
CPython
```

There are different Python implementations, such as:

```text
CPython
PyPy
IronPython
```

So this tells us **which implementation** is running our code.

---

# Step 4 — Get the Python version

Add:

```python
python_version = platform.python_version()
```

For example:

```text
3.14.0
```

Notice we're using:

```python
platform.python_version()
```

instead of manually trying to extract the version from a string.

That's easier for this project.

---

# Step 5 — Get the Python executable

Add:

```python
python_executable = sys.executable
```

This is particularly useful.

Suppose you have:

```text
Python 3.12
Python 3.13
Python 3.14
```

installed on the same computer.

You run:

```bash
python environment_check.py
```

and the program tells you:

```text
Executable : C:\Python314\python.exe
```

Now you know **which Python installation actually executed your program**.

That's very useful when troubleshooting Python environment problems.

---

# Step 6 — Get the operating system

Add:

```python
operating_system = platform.system()
```

Possible results include:

```text
Windows
Linux
Darwin
```

For example:

```text
OS : Windows
```

---

# Step 7 — Get machine architecture

Add:

```python
architecture = platform.architecture()[0]
```

This may return:

```text
64bit
```

or:

```text
32bit
```

We'll clean the output slightly later.

---

# Step 8 — Create the heading

Now add:

```python
print("=====================================")
print("     PYTHON ENVIRONMENT CHECK")
print("=====================================")
print()
```

This creates:

```text
=====================================
     PYTHON ENVIRONMENT CHECK
=====================================
```

---

# Step 9 — Display the information

Add:

```python
print("Implementation :", python_implementation)
print("Version        :", python_version)
print("Executable     :", python_executable)
print("OS             :", operating_system)
print("Architecture   :", architecture)
```

The spacing after the labels makes the output easier to read.

---

# Step 10 — Add the closing line

Finally:

```python
print()
print("=====================================")
```

Our report now looks like:

```text
=====================================
     PYTHON ENVIRONMENT CHECK
=====================================

Implementation : CPython
Version        : 3.14.0
Executable     : C:\Python314\python.exe
OS             : Windows
Architecture   : 64bit

=====================================
```

---

# 5. Complete Working Code

Your first complete version is:

```python
import platform
import sys


# Get Python environment information
python_implementation = platform.python_implementation()
python_version = platform.python_version()
python_executable = sys.executable
operating_system = platform.system()
architecture = platform.architecture()[0]


# Display the report
print("=====================================")
print("     PYTHON ENVIRONMENT CHECK")
print("=====================================")
print()

print("Implementation :", python_implementation)
print("Version        :", python_version)
print("Executable     :", python_executable)
print("OS             :", operating_system)
print("Architecture   :", architecture)

print()
print("=====================================")
```

That's already a complete working project.

---

# 6. How to Run

Open your terminal inside:

```text
python-environment-diagnostic
```

Your structure:

```text
python-environment-diagnostic/
└── environment_check.py
```

Then run:

### Windows

```bash
python environment_check.py
```

or:

```bash
py environment_check.py
```

### Linux/macOS

```bash
python3 environment_check.py
```

No `pip install` is required.

---

# 7. Example Run

On a Windows machine, you could see:

```text
=====================================
     PYTHON ENVIRONMENT CHECK
=====================================

Implementation : CPython
Version        : 3.14.0
Executable     : C:\Python314\python.exe
OS             : Windows
Architecture   : 64bit

=====================================
```

On Linux:

```text
=====================================
     PYTHON ENVIRONMENT CHECK
=====================================

Implementation : CPython
Version        : 3.12.3
Executable     : /usr/bin/python3
OS             : Linux
Architecture   : 64bit

=====================================
```

Your output will depend on your actual Python installation.

---

# 8. Let's Understand the Code

Now let's break down the important pieces.

## `import`

```python
import platform
import sys
```

This is your first important concept.

`import` lets your program use functionality provided by another module.

Think:

```text
Python
 │
 ├── platform
 │     └── system information
 │
 └── sys
       └── Python interpreter information
```

---

# `platform.python_implementation()`

```python
python_implementation = platform.python_implementation()
```

This asks:

> "Which Python implementation is running?"

Usually:

```text
CPython
```

---

# `platform.python_version()`

```python
python_version = platform.python_version()
```

This gives the Python version as a string.

Example:

```text
3.14.0
```

So:

```python
python_version
```

contains:

```text
"3.14.0"
```

---

# `sys.executable`

```python
python_executable = sys.executable
```

This is one of the most useful pieces in this project.

It tells you the executable that is actually running your script.

For example:

```text
C:\Users\Vinit\AppData\Local\Programs\Python\Python314\python.exe
```

or:

```text
/usr/bin/python3
```

This is especially useful when you have multiple Python installations or virtual environments.

---

# `platform.system()`

```python
operating_system = platform.system()
```

Possible results:

```text
Windows
Linux
Darwin
```

---

# `platform.architecture()`

```python
architecture = platform.architecture()[0]
```

This one looks slightly weird:

```python
platform.architecture()[0]
```

because `platform.architecture()` returns multiple pieces of information.

Conceptually:

```text
platform.architecture()
        ↓
("64bit", "WindowsPE")
```

The `[0]` means:

> Give me the first item.

So:

```python
platform.architecture()[0]
```

returns:

```text
64bit
```

This is your first practical example of accessing an item by its position.

---

# 9. Improve the Output

The original example uses:

```text
64-bit
```

instead of:

```text
64bit
```

We can easily fix that.

Change:

```python
architecture = platform.architecture()[0]
```

to:

```python
architecture = platform.architecture()[0].replace("bit", "-bit")
```

Now:

```text
64bit
```

becomes:

```text
64-bit
```

But honestly, **don't add this yet if you're not comfortable with string methods**.

The simpler version:

```python
architecture = platform.architecture()[0]
```

is perfectly fine for this stage.

---

# 10. Better Version Using Functions

Your project requirements mention basic Python concepts, and you're going to eventually use functions heavily in DevOps scripts.

So let's make a slightly more organized version.

We'll create:

```python
def get_environment_info():
```

This function collects everything.

---

## Step 1 — Create the function

```python
def get_environment_info():
    python_implementation = platform.python_implementation()
    python_version = platform.python_version()
    python_executable = sys.executable
    operating_system = platform.system()
    architecture = platform.architecture()[0]
```

But now we need to return the information.

---

## Step 2 — Return a dictionary

```python
def get_environment_info():
    python_implementation = platform.python_implementation()
    python_version = platform.python_version()
    python_executable = sys.executable
    operating_system = platform.system()
    architecture = platform.architecture()[0]

    return {
        "implementation": python_implementation,
        "version": python_version,
        "executable": python_executable,
        "os": operating_system,
        "architecture": architecture
    }
```

Now:

```python
environment = get_environment_info()
```

gives us:

```text
environment
    ↓
{
    implementation: CPython,
    version: 3.14.0,
    executable: ...,
    os: Windows,
    architecture: 64bit
}
```

This is a nice example of combining:

```text
Functions
   +
Variables
   +
Dictionary
```

---

# 11. Final Recommended Version

I recommend you actually build **this version**, because it gives you a little more practice without becoming complicated.

```python
import platform
import sys


def get_environment_info():
    """Collect information about the current Python environment."""

    python_implementation = platform.python_implementation()
    python_version = platform.python_version()
    python_executable = sys.executable
    operating_system = platform.system()
    architecture = platform.architecture()[0]

    return {
        "implementation": python_implementation,
        "version": python_version,
        "executable": python_executable,
        "os": operating_system,
        "architecture": architecture
    }


def display_report(environment):
    """Display the Python environment information."""

    print("=====================================")
    print("     PYTHON ENVIRONMENT CHECK")
    print("=====================================")
    print()

    print("Implementation :", environment["implementation"])
    print("Version        :", environment["version"])
    print("Executable     :", environment["executable"])
    print("OS             :", environment["os"])
    print("Architecture   :", environment["architecture"])

    print()
    print("=====================================")


def main():
    environment = get_environment_info()
    display_report(environment)


main()
```

This is still beginner-level.

We're simply separating:

```text
Collect information
       ↓
get_environment_info()

Display information
       ↓
display_report()

Run program
       ↓
main()
```

---

# 12. Program Flow

The entire program works like this:

```text
main()
  │
  ↓
get_environment_info()
  │
  ├── Python implementation
  ├── Python version
  ├── Python executable
  ├── Operating system
  └── Architecture
  │
  ↓
return dictionary
  │
  ↓
display_report()
  │
  ↓
Print information
  │
  ↓
End
```

That's a clean little program.

---

# 13. Why `sys.executable` Is Particularly Important

This deserves extra attention because it has real DevOps value.

Imagine you have:

```text
Python 3.12
Python 3.13
Python 3.14
```

on your computer.

You type:

```bash
python environment_check.py
```

Your shell resolves `python` to some executable.

Your program then reports:

```text
Executable : C:\Python314\python.exe
```

Now you know which interpreter actually executed the script.

This becomes even more useful with virtual environments.

For example:

```text
my-project/
└── .venv/
    └── Scripts/
        └── python.exe
```

If your script reports:

```text
Executable : C:\Projects\my-project\.venv\Scripts\python.exe
```

you know that you're running inside the virtual environment.

That's a very practical troubleshooting technique.

---

# 14. Common Beginner Mistakes

## Mistake 1 — Using the wrong module

Correct:

```python
import platform
```

Not:

```python
import platforms
```

---

## Mistake 2 — Forgetting `()`

Correct:

```python
platform.system()
```

Not:

```python
platform.system
```

You want to **call** the function.

---

## Mistake 3 — Thinking `sys.executable` is the Python version

These are different:

```python
sys.executable
```

→ path to Python executable

while:

```python
platform.python_version()
```

→ Python version

For example:

```text
Executable → C:\Python314\python.exe
Version    → 3.14.0
```

---

## Mistake 4 — Installing `platform`

Don't do:

```bash
pip install platform
```

or:

```bash
pip install sys
```

They're part of Python's standard library.

---

## Mistake 5 — Assuming every Python is CPython

Most people encounter CPython, but Python is an implementation/specification ecosystem rather than one single implementation.

That's precisely why we're checking:

```python
platform.python_implementation()
```

instead of assuming:

```text
CPython
```

---

# 15. Practice Tasks

Now modify the project yourself.

## Task 1 — Add the machine name

Add:

```text
Machine        : MY-PC
```

Hint:

```python
platform.node()
```

Create a variable for it and display it.

**Difficulty: Easy**

---

## Task 2 — Add the processor

Add:

```text
Processor      : Intel64 Family...
```

Hint:

```python
platform.processor()
```

Don't worry if the exact output is different between operating systems.

**Difficulty: Easy**

---

## Task 3 — Add the Python build

Find a way to display something like:

```text
Build          : ...
```

Look into:

```python
platform.python_build()
```

Don't copy an implementation from somewhere immediately. First inspect what it returns.

**Difficulty: Medium**

---

## Task 4 — Add Python major/minor/patch versions

Investigate:

```python
sys.version_info
```

Try to display:

```text
Major Version  : 3
Minor Version  : 14
Patch Version  : 0
```

This is good practice for accessing information from an object/structure.

**Difficulty: Medium**

---

## Task 5 — DevOps challenge: JSON report

Once you've learned JSON, modify the program so:

```bash
python environment_check.py
```

can eventually produce:

```json
{
    "implementation": "CPython",
    "version": "3.14.0",
    "executable": "...",
    "os": "Windows",
    "architecture": "64bit"
}
```

**Do not implement this yet if JSON isn't part of what you've learned.**

When you reach JSON in your Python learning path, come back and upgrade this project.

---

# 16. Stretch Goal Roadmap

Eventually this project can evolve from:

```text
Simple Python script
```

into:

```text
Python Environment Diagnostic CLI
```

A sensible progression is:

```text
V1
Python environment information
        ↓
V2
More system information
        ↓
V3
JSON output
        ↓
V4
Save report to file
        ↓
V5
Command-line arguments
        ↓
V6
Exit codes
        ↓
V7
Environment-variable checks
        ↓
V8
Virtual-environment detection
        ↓
V9
Docker/container detection
        ↓
V10
CI/CD diagnostic mode
```

For example, eventually:

```bash
python envcheck.py --json
```

could produce machine-readable output, while:

```bash
python envcheck.py
```

could produce the human-readable report.

Then CI/CD could consume the exit code:

```text
Environment check
       ↓
Healthy?
   ↙       ↘
 YES       NO
  ↓         ↓
exit 0    exit 1
  ↓         ↓
pipeline  pipeline
continues stops
```

That's where this becomes a legitimate DevOps utility rather than just a Python exercise.

---

# 17. What You Learned

## Python concepts

You practiced:

* `import`
* Modules
* `platform`
* `sys`
* Variables
* Strings
* Function calls
* Functions
* Dictionaries
* `return`
* Output formatting
* Indexing with `[0]`

---

## System concepts

You learned how Python can identify:

```text
Python implementation
Python version
Python executable
Operating system
Machine architecture
```

---

## DevOps relevance

The biggest lesson is **environment awareness**.

A Python application doesn't run in a vacuum:

```text
Application
     ↓
Python interpreter
     ↓
Operating system
     ↓
Machine
```

If something goes wrong, knowing exactly which environment executed your application is often the first step toward diagnosing it.

And there's a useful connection between your last two projects:

```text
System Health Checker
        +
Python Environment Diagnostic
        ↓
DevOps Environment Diagnostic Tool
        ↓
JSON / CLI / Exit Codes
        ↓
CI/CD Integration
```

So **keep these projects instead of treating them as disposable exercises**. As you learn more Python concepts, we can progressively upgrade them into more realistic DevOps utilities rather than rebuilding everything from zero.
