# Python Mini Project — DevOps System Health Checker

This is the point where our Python projects start looking like **actual DevOps utilities**.

We're going to build a command-line health-check script that answers:

> **"Is this machine/environment ready to run my application?"**

It will check:

* Python version
* Operating system
* Current working directory
* Available disk space
* Required environment variables

And instead of simply printing information, it will make **health decisions**:

```text
OK
MISSING
LOW
```

That's important because DevOps scripts aren't just about collecting information. They often **check conditions and report whether something is healthy or broken**.

For the first version, we'll use only Python's standard library, including `platform`, `os`, and `shutil`. `shutil.disk_usage()` provides filesystem disk-space information, while `os.getenv()`/`os.environ` can be used to access environment variables.

---

# 1. Understand the Project

## What are we building?

We're building:

```text
DevOps System Health Checker
```

When you run:

```bash
python health_checker.py
```

the program will inspect the machine and produce something like:

```text
================================
       SYSTEM HEALTH CHECK
================================

Python Version : 3.12.5
OS             : Windows
Working Dir    : C:\Projects\health-checker

Environment:
DATABASE_URL   : OK
API_KEY        : OK

Disk:
Status         : OK
Free Space     : 178.42 GB
```

If something is wrong:

```text
Environment:
DATABASE_URL   : MISSING
API_KEY        : OK

Disk:
Status         : LOW
Free Space     : 3.25 GB

Overall Status : NOT HEALTHY
```

---

# Why is this a DevOps project?

Imagine you're deploying an application to a server.

Before starting it, you might need:

```text
Python installed?
       ↓
Correct environment?
       ↓
Required variables available?
       ↓
Enough disk space?
       ↓
Everything OK?
       ↓
Start application
```

Instead of manually checking everything, we can run:

```bash
python health_checker.py
```

That's the basic idea behind a **pre-flight check**.

Later, the same script can be used in:

```text
Developer machine
       ↓
Test server
       ↓
Staging
       ↓
Production
       ↓
CI/CD pipeline
```

---

# 2. Requirements

## Software

You need:

* Python 3
* VS Code
* Terminal / Command Prompt

No external packages are required.

We're using Python's standard library.

We'll use:

| Module     | Purpose                                     |
| ---------- | ------------------------------------------- |
| `platform` | OS and Python information                   |
| `os`       | Environment variables and current directory |
| `shutil`   | Disk usage                                  |
| `sys`      | Python interpreter/version information      |

All of these are included with Python.

---

# 3. Project Structure

We'll keep the project small:

```text
devops-system-health-checker/
│
├── health_checker.py
└── README.md
```

For the actual program, the important file is:

```text
health_checker.py
```

The README is optional and can be added later.

We're deliberately **not** creating:

```text
config/
utils/
services/
models/
classes/
...
```

That would be ridiculous for a beginner script this small.

---

# 4. Build It Step-by-Step

# Step 1 — Create the project

Create:

```text
devops-system-health-checker
```

Inside it create:

```text
health_checker.py
```

---

# Step 2 — Import the modules

At the top:

```python
import os
import platform
import shutil
import sys
```

These are all built into Python.

---

# Step 3 — Create the health-check configuration

We need to decide which environment variables our application requires.

We'll start with:

```python
REQUIRED_ENV_VARS = [
    "DATABASE_URL",
    "API_KEY"
]
```

This is a list.

We're saying:

> Our application expects these two environment variables to exist.

This is a realistic DevOps pattern.

For example, an application might need:

```text
DATABASE_URL
API_KEY
SECRET_KEY
AWS_REGION
```

We don't want to hard-code secret values inside the Python program.

Instead, the environment provides them.

---

# Step 4 — Understanding environment variables

An environment variable is basically a value provided by the operating system to a program.

For example:

```text
DATABASE_URL=postgresql://localhost/mydb
API_KEY=some-secret-value
```

Python can read these using:

```python
os.getenv("DATABASE_URL")
```

If it exists, Python gets the value.

If it doesn't exist, `os.getenv()` returns `None` by default.

We don't actually want to print the secret value.

We only care whether it exists.

So:

```python
if os.getenv("DATABASE_URL"):
    print("DATABASE_URL : OK")
else:
    print("DATABASE_URL : MISSING")
```

This is safer than printing:

```text
API_KEY = abc123...
```

Never build a health checker that casually dumps secrets into the terminal or CI logs.

---

# Step 5 — Create the Python version check

Let's create a function.

```python
def get_python_version():
    return platform.python_version()
```

Now we can call:

```python
python_version = get_python_version()
```

The result could be:

```text
3.12.5
```

We're using a function because the project requirements include functions.

---

# Step 6 — Create the OS check

Add:

```python
def get_operating_system():
    return platform.system()
```

Then:

```python
operating_system = get_operating_system()
```

Possible results:

```text
Windows
Linux
Darwin
```

---

# Step 7 — Get the current directory

Create:

```python
def get_working_directory():
    return os.getcwd()
```

Then:

```python
working_directory = get_working_directory()
```

For example:

```text
C:\Projects\devops-system-health-checker
```

---

# Step 8 — Check environment variables

Now create:

```python
def check_environment_variables(required_variables):
    results = {}

    for variable in required_variables:
        if os.getenv(variable):
            results[variable] = "OK"
        else:
            results[variable] = "MISSING"

    return results
```

This is probably the most important function in the project.

Let's understand it.

---

## `results = {}`

We're creating an empty dictionary.

```python
results = {}
```

Eventually it might contain:

```python
{
    "DATABASE_URL": "OK",
    "API_KEY": "OK"
}
```

---

## Loop through required variables

```python
for variable in required_variables:
```

If our list is:

```python
[
    "DATABASE_URL",
    "API_KEY"
]
```

the loop runs twice.

First:

```text
variable = DATABASE_URL
```

Then:

```text
variable = API_KEY
```

---

## Check whether the variable exists

```python
if os.getenv(variable):
```

Python checks whether a value exists.

If it does:

```python
results[variable] = "OK"
```

Otherwise:

```python
results[variable] = "MISSING"
```

---

# Step 9 — Check disk space

Now we'll use `shutil`.

Create:

```python
def check_disk_space():
    total, used, free = shutil.disk_usage("/")
    return free
```

But wait.

There's a problem.

On Linux:

```text
/
```

is the root filesystem.

But Windows doesn't normally use `/` in this way.

So we need a platform-independent approach.

We can use the current working directory:

```python
def check_disk_space():
    total, used, free = shutil.disk_usage(os.getcwd())
    return free
```

This asks Python for the disk usage of the filesystem containing our current working directory.

`shutil.disk_usage(path)` returns total, used, and free space in bytes.

---

# Step 10 — Convert bytes to GB

Disk space comes back in bytes.

For example:

```text
191348432896 bytes
```

That's not friendly to humans.

Let's convert it to GB.

Create:

```python
def bytes_to_gb(bytes_value):
    return bytes_value / (1024 ** 3)
```

So:

```python
bytes_to_gb(free_space)
```

might produce:

```text
178.42
```

---

# Step 11 — Decide whether disk space is healthy

Now we need a rule.

Let's say:

```text
20 GB or more → OK
Less than 20 GB → LOW
```

We'll store the threshold:

```python
MIN_FREE_SPACE_GB = 20
```

Then:

```python
def check_disk_health(free_space_gb):
    if free_space_gb >= MIN_FREE_SPACE_GB:
        return "OK"
    else:
        return "LOW"
```

This is where we're practicing **conditions**.

We're not merely displaying disk space.

We're making a decision based on it.

---

# Step 12 — Create the report

Now let's create:

```python
def display_report(...):
```

The function will print everything in a readable format.

We'll pass the information into it rather than making the function secretly collect everything itself.

That keeps the logic easier to understand.

---

# Step 13 — Display environment results

Inside the report:

```python
print("Environment:")

for variable, status in environment_results.items():
    print(f"{variable:<15}: {status}")
```

This introduces an f-string:

```python
f"{variable:<15}"
```

Don't worry too much about the `<15` yet.

It simply gives the variable names some spacing so the output lines up.

---

# Step 14 — Determine overall health

Our program should have an overall result.

We can check:

```python
environment_healthy = all(
    status == "OK"
    for status in environment_results.values()
)
```

But I'm **not** going to use this in our first version.

Why?

Because you haven't reached enough advanced Python concepts to make this clearer than necessary.

We'll use a simple loop instead:

```python
environment_healthy = True

for status in environment_results.values():
    if status != "OK":
        environment_healthy = False
```

Much easier to understand.

---

# Step 15 — Add error handling

This project requires error handling.

We can use a simple `try/except` around disk checking:

```python
try:
    free_space = get_free_disk_space()
except OSError:
    print("Could not check disk space.")
```

Why `OSError`?

Filesystem operations can fail because of operating-system-level problems. Python's filesystem APIs can raise `OSError` and related exceptions when operations fail.

We'll handle this without making the project overly complicated.

---

# 5. Complete Working Code

Here is the complete version.

Create `health_checker.py`:

```python
import os
import platform
import shutil


# Configuration
REQUIRED_ENV_VARS = [
    "DATABASE_URL",
    "API_KEY"
]

MIN_FREE_SPACE_GB = 20


def get_python_version():
    return platform.python_version()


def get_operating_system():
    return platform.system()


def get_working_directory():
    return os.getcwd()


def check_environment_variables(required_variables):
    results = {}

    for variable in required_variables:
        if os.getenv(variable):
            results[variable] = "OK"
        else:
            results[variable] = "MISSING"

    return results


def get_free_disk_space():
    total, used, free = shutil.disk_usage(os.getcwd())
    return free


def bytes_to_gb(bytes_value):
    return bytes_value / (1024 ** 3)


def check_disk_health(free_space_gb):
    if free_space_gb >= MIN_FREE_SPACE_GB:
        return "OK"
    else:
        return "LOW"


def display_report(
    python_version,
    operating_system,
    working_directory,
    environment_results,
    disk_status,
    free_space_gb
):
    print("================================")
    print("       SYSTEM HEALTH CHECK")
    print("================================")
    print()

    print("Python Version :", python_version)
    print("OS             :", operating_system)
    print("Working Dir    :", working_directory)

    print()
    print("Environment:")

    for variable, status in environment_results.items():
        print(f"{variable:<15}: {status}")

    print()
    print("Disk:")
    print("Status         :", disk_status)
    print(f"Free Space     : {free_space_gb:.2f} GB")

    # Check overall health
    system_healthy = True

    for status in environment_results.values():
        if status != "OK":
            system_healthy = False

    if disk_status != "OK":
        system_healthy = False

    print()

    if system_healthy:
        print("Overall Status : HEALTHY")
    else:
        print("Overall Status : NOT HEALTHY")


def main():
    # Collect basic system information
    python_version = get_python_version()
    operating_system = get_operating_system()
    working_directory = get_working_directory()

    # Check environment variables
    environment_results = check_environment_variables(
        REQUIRED_ENV_VARS
    )

    # Check disk space
    try:
        free_space = get_free_disk_space()
        free_space_gb = bytes_to_gb(free_space)
        disk_status = check_disk_health(free_space_gb)

    except OSError:
        free_space_gb = 0
        disk_status = "ERROR"

    # Display everything
    display_report(
        python_version,
        operating_system,
        working_directory,
        environment_results,
        disk_status,
        free_space_gb
    )


# Start the program
main()
```

This is our **Version 1**.

---

# 6. How to Run

First create the project:

```text
devops-system-health-checker/
│
└── health_checker.py
```

Open your terminal in that directory.

Run:

### Windows

```bash
python health_checker.py
```

or:

```bash
py health_checker.py
```

### Linux/macOS

```bash
python3 health_checker.py
```

There are no packages to install.

---

# 7. Setting Environment Variables

If you simply run the program right now, you'll probably get:

```text
Environment:
DATABASE_URL   : MISSING
API_KEY        : MISSING
```

That's intentional.

We haven't created those environment variables yet.

Let's test them properly.

---

## Windows Command Prompt

Before running the program:

```cmd
set DATABASE_URL=test_database
set API_KEY=test_key
python health_checker.py
```

These values are only for testing.

**Do not use real secrets in this example.**

---

## PowerShell

```powershell
$env:DATABASE_URL="test_database"
$env:API_KEY="test_key"
python health_checker.py
```

---

## Linux/macOS

```bash
export DATABASE_URL=test_database
export API_KEY=test_key
python3 health_checker.py
```

Then run the script.

You should see:

```text
Environment:
DATABASE_URL   : OK
API_KEY        : OK
```

---

# 8. Example Run

Assuming both environment variables exist and you have enough disk space:

```text
================================
       SYSTEM HEALTH CHECK
================================

Python Version : 3.12.5
OS             : Windows
Working Dir    : C:\Projects\devops-system-health-checker

Environment:
DATABASE_URL   : OK
API_KEY        : OK

Disk:
Status         : OK
Free Space     : 178.42 GB

Overall Status : HEALTHY
```

---

# Example — Missing Environment Variable

If `API_KEY` doesn't exist:

```text
================================
       SYSTEM HEALTH CHECK
================================

Python Version : 3.12.5
OS             : Windows
Working Dir    : C:\Projects\devops-system-health-checker

Environment:
DATABASE_URL   : OK
API_KEY        : MISSING

Disk:
Status         : OK
Free Space     : 178.42 GB

Overall Status : NOT HEALTHY
```

This is exactly the kind of information that could be useful before starting an application.

---

# 9. Code Explanation

Now let's understand the important parts.

---

## 1. Configuration

```python
REQUIRED_ENV_VARS = [
    "DATABASE_URL",
    "API_KEY"
]
```

This is our configuration.

Instead of scattering these names throughout the program, we keep them in one list.

Later you can easily change:

```python
REQUIRED_ENV_VARS = [
    "DATABASE_URL",
    "API_KEY",
    "SECRET_KEY",
    "AWS_REGION"
]
```

without rewriting the checking logic.

---

# 2. `platform`

```python
platform.python_version()
```

returns the Python version.

And:

```python
platform.system()
```

returns the operating system.

For example:

```text
Windows
Linux
Darwin
```

This is useful when writing scripts that need to behave differently depending on the OS.

---

# 3. `os.getcwd()`

```python
os.getcwd()
```

returns the current working directory.

Example:

```text
C:\Projects\devops-system-health-checker
```

This is particularly relevant in automation because scripts often interact with files relative to their working directory.

---

# 4. Environment variables

The important line is:

```python
os.getenv(variable)
```

Suppose:

```python
variable = "API_KEY"
```

Python effectively checks:

```python
os.getenv("API_KEY")
```

If there's a value:

```text
OK
```

If there isn't:

```text
MISSING
```

We deliberately **don't print the value**.

That's an important DevOps/security habit.

---

# 5. `shutil.disk_usage()`

This:

```python
shutil.disk_usage(os.getcwd())
```

returns three values:

```text
total
used
free
```

We capture them:

```python
total, used, free = shutil.disk_usage(os.getcwd())
```

Then:

```python
free
```

contains the number of free bytes.

The Python documentation specifies that `disk_usage()` returns total, used, and free space for the given path.

---

# 6. Bytes → GB

The computer gives us:

```text
bytes
```

Humans prefer:

```text
GB
```

So:

```python
def bytes_to_gb(bytes_value):
    return bytes_value / (1024 ** 3)
```

The:

```python
1024 ** 3
```

represents the number of bytes in a GiB.

Technically, we're converting to **GiB**, even though the output label says GB.

If you want to be technically precise, change:

```python
Free Space : 178.42 GB
```

to:

```python
Free Space : 178.42 GiB
```

For a beginner DevOps utility, either is understandable, but **GiB is the technically correct unit for the 1024³ conversion**.

---

# 7. Disk health condition

We set:

```python
MIN_FREE_SPACE_GB = 20
```

Then:

```python
if free_space_gb >= MIN_FREE_SPACE_GB:
    return "OK"
else:
    return "LOW"
```

So:

```text
100 GB → OK
50 GB  → OK
20 GB  → OK
19 GB  → LOW
5 GB   → LOW
```

This is a real programming decision.

We're taking raw system information:

```text
17.2 GB free
```

and turning it into:

```text
LOW
```

---

# 8. Functions

We have several functions:

```text
get_python_version()
get_operating_system()
get_working_directory()
check_environment_variables()
get_free_disk_space()
bytes_to_gb()
check_disk_health()
display_report()
main()
```

Don't get intimidated by the number.

Most are tiny.

The advantage is that each function has **one clear job**.

For example:

```python
def get_python_version():
    return platform.python_version()
```

does one thing.

And:

```python
def check_disk_health(...):
```

does one thing.

This makes the program easier to modify later.

---

# 9. `main()`

The program starts here:

```python
main()
```

Inside:

```python
def main():
```

we coordinate everything.

Think:

```text
main()
 │
 ├── get Python version
 │
 ├── get OS
 │
 ├── get working directory
 │
 ├── check environment
 │
 ├── check disk
 │
 └── display report
```

That's the overall program flow.

---

# 10. Error Handling

This section:

```python
try:
    free_space = get_free_disk_space()
    free_space_gb = bytes_to_gb(free_space)
    disk_status = check_disk_health(free_space_gb)

except OSError:
    free_space_gb = 0
    disk_status = "ERROR"
```

means:

> Try checking the disk. If the operating system reports a filesystem-related error, don't crash the entire program.

Instead:

```text
Status : ERROR
```

This is your first practical use of **exception handling**.

---

# 11. One Important DevOps Lesson

There's a subtle problem with our current program.

It tells us:

```text
DATABASE_URL : OK
```

but it doesn't tell us whether the database URL is **valid**.

Likewise:

```text
API_KEY : OK
```

only means:

> Something exists under that environment variable.

It does **not** mean the API key actually works.

That's intentional.

A beginner health checker should distinguish:

```text
Presence check
```

from:

```text
Actual service validation
```

Later, you could make a real health check that tests:

```text
DATABASE_URL
      ↓
Can we connect?

API_KEY
      ↓
Can we authenticate?

Network
      ↓
Can we reach required service?
```

But don't pretend that checking whether an environment variable exists proves that the service is healthy.

That's a common mistake in simplistic health-check scripts.

---

# 12. Common Beginner Mistakes

## Mistake 1 — Hard-coding secrets

Bad:

```python
API_KEY = "123456abcdef"
```

Don't do this.

Environment variables exist partly so configuration/secrets don't need to be embedded directly in source code.

---

## Mistake 2 — Printing secrets

Don't do:

```python
print(os.getenv("API_KEY"))
```

Your terminal or CI logs could expose it.

Instead:

```python
if os.getenv("API_KEY"):
    print("API_KEY: OK")
```

---

## Mistake 3 — Installing standard-library modules

Don't run:

```bash
pip install os
pip install platform
pip install shutil
```

These are Python standard-library modules.

---

## Mistake 4 — Assuming `/` works everywhere

This:

```python
shutil.disk_usage("/")
```

is common on Linux/macOS.

But for a cross-platform beginner script, using:

```python
shutil.disk_usage(os.getcwd())
```

is simpler.

---

## Mistake 5 — Thinking `OK` means everything is actually healthy

Our:

```text
API_KEY : OK
```

means only:

```text
Environment variable exists.
```

It doesn't mean:

```text
API service works.
```

That's an important distinction as you move toward real DevOps.

---

# 13. Practice Tasks

Now don't immediately copy the stretch goals.

Do these in order.

## Task 1 — Add another required variable

Add:

```text
SECRET_KEY
```

to:

```python
REQUIRED_ENV_VARS
```

Then test whether the program correctly reports:

```text
SECRET_KEY : MISSING
```

and:

```text
SECRET_KEY : OK
```

**Difficulty: Easy**

---

## Task 2 — Change the disk threshold

Currently:

```python
MIN_FREE_SPACE_GB = 20
```

Change it to:

```python
MIN_FREE_SPACE_GB = 100
```

Run the program.

What happens?

Why?

This is a simple but important exercise in understanding **conditions and configuration**.

**Difficulty: Easy**

---

## Task 3 — Add hostname

Add:

```text
Hostname       : MY-PC
```

Hint:

```python
platform.node()
```

You can create:

```python
def get_hostname():
    return platform.node()
```

Then include it in the report.

**Difficulty: Easy → Medium**

---

## Task 4 — Add CPU information

Find a standard-library way to get the number of CPU cores.

You can investigate:

```python
os.cpu_count()
```

Then display:

```text
CPU Cores      : 6
```

This starts moving your script toward a real system-information tool.

**Difficulty: Medium**

---

## Task 5 — DevOps challenge: health-check exit code

This is the big one.

Right now the program can say:

```text
Overall Status : NOT HEALTHY
```

but the operating system still sees the Python program as successfully completed unless we explicitly exit with a non-zero status.

Later, learn about:

```python
sys.exit()
```

and make the program behave like:

```text
HEALTHY
    ↓
exit code 0

NOT HEALTHY
    ↓
exit code 1
```

Why is this useful?

Because CI/CD tools can then do:

```text
Run health checker
       ↓
Exit code?
    ↙       ↘
   0         1
   ↓         ↓
Continue    Stop
pipeline    pipeline
```

**Difficulty: Medium → Hard**

This is probably the **most valuable stretch goal** in this project for your DevOps path.

---

# 14. What You Learned

## Python concepts

You've practiced:

* Variables
* Lists
* Dictionaries
* Conditions
* Functions
* Function arguments
* Return values
* Loops
* Modules
* `try/except`
* Environment variables
* Standard library
* Filesystem operations
* String formatting

---

## System concepts

You learned how Python can interact with the operating system to obtain:

```text
OS
Python version
Working directory
Environment variables
Disk usage
```

---

## DevOps concepts

More importantly, you've built your first **environment validation tool**.

The pattern is:

```text
Machine
   ↓
Collect information
   ↓
Check requirements
   ↓
Apply rules
   ↓
Determine health
   ↓
Generate report
```

And this is where your Python → DevOps progression starts getting more serious:

```text
Python basics
      ↓
Filesystem automation
      ↓
System information
      ↓
Health checking
      ↓
CLI tools
      ↓
Exit codes
      ↓
Logging
      ↓
JSON output
      ↓
CI/CD
      ↓
Server/cloud automation
```

Your current project is still small, but unlike the earlier history project, **this one has a direct path toward something you could genuinely use in a DevOps workflow**.

One particularly important next upgrade is **exit codes**. Once your checker can return `0` for healthy and a non-zero code for unhealthy, it stops being merely a reporting script and starts becoming something a CI/CD pipeline can actually act upon.
