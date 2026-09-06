# Python Mini Project — CLI Log Scanner

This is a **much better project for practicing loops** than another system-information checker.

We're going to build a small interactive CLI that processes log entries, counts their severity, stores errors, and lets the user search through the logs.

The important part is that we're going to **actually use `for`, `while`, `break`, `continue`, `if/elif/else`, and `range()`**, rather than forcing those concepts into the project just for the sake of using them.

---

# 1. Understand the Project

## What are we building?

We're building:

```text
CLI Log Scanner
```

It starts with a list of logs:

```python
logs = [
    "INFO Server started",
    "INFO User logged in",
    "WARNING Disk usage above 80%",
    "ERROR Database connection failed",
    "INFO Backup completed",
    "ERROR API request failed",
    "WARNING Memory usage above 75%"
]
```

The program will process these logs and allow the user to choose:

```text
========== LOG SCANNER ==========

1. View Summary
2. View Errors
3. Search Logs
4. Exit

Choose:
```

For example:

```text
Choose: 1

========== SUMMARY ==========

Total logs : 7
INFO       : 3
WARNING    : 2
ERROR      : 2
```

Choosing `2`:

```text
========== ERRORS ==========

1. Database connection failed
2. API request failed
```

Choosing `3`:

```text
Search keyword: database

Found:
ERROR Database connection failed
```

---

# Why is this a DevOps project?

Logs are one of the most basic sources of information when operating applications and servers.

A real system might produce:

```text
INFO Server started
INFO Request received
WARNING Memory usage high
ERROR Database unavailable
ERROR API timeout
```

A human shouldn't have to manually inspect thousands of lines.

Automation can:

```text
Log file
   ↓
Read entries
   ↓
Identify severity
   ↓
Count problems
   ↓
Find important messages
   ↓
Generate report
   ↓
Alert / monitoring system
```

Our project is a **tiny beginner version of that workflow**.

Later, when you learn file handling, we'll replace:

```python
logs = [...]
```

with:

```text
application.log
       ↓
Python
       ↓
CLI Log Scanner
```

That's where this starts becoming genuinely useful.

---

# 2. Requirements

## Software

You need:

* Python 3
* VS Code
* Terminal / Command Prompt

## External libraries

**None.**

We're using only basic Python.

---

# 3. Project Structure

Keep it extremely simple:

```text
cli-log-scanner/
│
└── log_scanner.py
```

Only one Python file is needed right now.

### `log_scanner.py`

Contains:

* log data
* log analysis
* summary
* error display
* search
* menu

We're **not** going to create five different files for a project this small.

---

# 4. Build It Step-by-Step

## Step 1 — Create the project

Create:

```text
cli-log-scanner
```

Inside it:

```text
log_scanner.py
```

---

# Step 2 — Add the logs

At the top of the file:

```python
logs = [
    "INFO Server started",
    "INFO User logged in",
    "WARNING Disk usage above 80%",
    "ERROR Database connection failed",
    "INFO Backup completed",
    "ERROR API request failed",
    "WARNING Memory usage above 75%"
]
```

This is our sample log data.

---

# Step 3 — Create counters

We need to count each type.

Create:

```python
info_count = 0
warning_count = 0
error_count = 0
```

Initially:

```text
INFO = 0
WARNING = 0
ERROR = 0
```

As we process the logs, we'll increase the appropriate counter.

---

# Step 4 — Create a list for errors

We also need to remember the actual error messages.

Create:

```python
error_messages = []
```

Initially:

```text
[]
```

When we find:

```text
ERROR Database connection failed
```

we'll store:

```text
Database connection failed
```

inside that list.

---

# Step 5 — Process every log with `for`

Now the main loop:

```python
for log in logs:
    print(log)
```

This means:

> Take each log from the `logs` list, one at a time.

So Python processes:

```text
INFO Server started
        ↓
INFO User logged in
        ↓
WARNING Disk usage above 80%
        ↓
ERROR Database connection failed
        ↓
...
```

This is the perfect situation for a `for` loop.

---

# Step 6 — Identify severity

Each log begins with:

```text
INFO
WARNING
ERROR
```

So we can check:

```python
if log.startswith("INFO"):
    info_count += 1

elif log.startswith("WARNING"):
    warning_count += 1

elif log.startswith("ERROR"):
    error_count += 1
```

Now we're practicing:

```text
if
elif
```

and counters.

---

# Step 7 — Store error messages

When we find an error:

```python
elif log.startswith("ERROR"):
    error_count += 1
```

we also want the actual message.

The log is:

```text
ERROR Database connection failed
```

We want:

```text
Database connection failed
```

We can use:

```python
message = log[6:]
```

Why `6`?

Because:

```text
ERROR 
012345
```

The first six characters are:

```text
ERROR 
```

So:

```python
log[6:]
```

returns:

```text
Database connection failed
```

Then:

```python
error_messages.append(message)
```

stores it.

---

# Step 8 — Put analysis into a function

Instead of keeping all this logic floating around, let's create:

```python
def analyze_logs(logs):
```

Inside:

```python
def analyze_logs(logs):
    info_count = 0
    warning_count = 0
    error_count = 0
    error_messages = []

    for log in logs:
        if log.startswith("INFO"):
            info_count += 1

        elif log.startswith("WARNING"):
            warning_count += 1

        elif log.startswith("ERROR"):
            error_count += 1
            error_messages.append(log[6:])

    return info_count, warning_count, error_count, error_messages
```

Now we can call:

```python
info_count, warning_count, error_count, error_messages = analyze_logs(logs)
```

This gives us all the results.

---

# Step 9 — Display the summary

Create:

```python
def display_summary(logs, info_count, warning_count, error_count):
    print()
    print("========== SUMMARY ==========")
    print()

    print("Total logs :", len(logs))
    print("INFO       :", info_count)
    print("WARNING    :", warning_count)
    print("ERROR      :", error_count)
```

The total number of logs is:

```python
len(logs)
```

For our list:

```text
7
```

---

# Step 10 — Display errors

Create:

```python
def display_errors(error_messages):
    print()
    print("========== ERRORS ==========")
    print()

    if len(error_messages) == 0:
        print("No errors found.")
    else:
        for i in range(len(error_messages)):
            print(f"{i + 1}. {error_messages[i]}")
```

Now we're using:

```python
range()
```

This is intentional.

If there are two errors:

```python
len(error_messages)
```

returns:

```text
2
```

Therefore:

```python
range(2)
```

produces:

```text
0
1
```

We then use:

```python
i + 1
```

so the user sees:

```text
1.
2.
```

instead of:

```text
0.
1.
```

---

# Step 11 — Why not just use `for error in error_messages`?

We actually **could**:

```python
for error in error_messages:
    print(error)
```

And for real production code, I'd probably prefer that here.

But you're currently learning `range()`, so this is a reasonable place to practice it.

The important lesson is:

> Don't use `range()` everywhere just because you've learned it.

Use the simplest loop that solves the problem.

---

# Step 12 — Create the search feature

We want the user to search the logs.

Create:

```python
def search_logs(logs):
    keyword = input("Enter search keyword: ")
```

Now loop:

```python
for log in logs:
    if keyword.lower() in log.lower():
        print(log)
```

This allows:

```text
database
```

to find:

```text
ERROR Database connection failed
```

even though the capitalization is different.

---

# Step 13 — Use `continue`

Here's a genuine place for `continue`.

We only want to search logs that are not empty.

Modify the loop:

```python
for log in logs:
    if log == "":
        continue

    if keyword.lower() in log.lower():
        print(log)
```

If an empty log appears:

```text
""
```

Python skips it and moves to the next log.

That's what `continue` means:

> Stop this iteration and continue with the next one.

---

## But is `continue` necessary here?

Not really.

That's an important lesson.

Our current dataset doesn't contain empty logs, so adding `continue` doesn't provide much value.

We could simply write:

```python
for log in logs:
    if keyword.lower() in log.lower():
        print(log)
```

**Don't force `continue` into every project.**

Your requirement says to use it where it genuinely improves the logic. We'll use it in the final version when validating search input.

---

# Step 14 — Create the menu

Now comes the interactive part.

We need:

```text
1. View Summary
2. View Errors
3. Search Logs
4. Exit
```

This is where we use:

```python
while
```

Create:

```python
while True:
    print()
    print("========== LOG SCANNER ==========")
    print()
    print("1. View Summary")
    print("2. View Errors")
    print("3. Search Logs")
    print("4. Exit")

    choice = input("Choose: ")
```

`while True` means:

> Keep showing the menu until we explicitly stop the loop.

---

# Step 15 — Process the menu choice

Add:

```python
if choice == "1":
    display_summary(
        logs,
        info_count,
        warning_count,
        error_count
    )

elif choice == "2":
    display_errors(error_messages)

elif choice == "3":
    search_logs(logs)

elif choice == "4":
    print("Exiting...")
    break

else:
    print("Invalid choice.")
```

Now we finally have our `break`.

When the user chooses:

```text
4
```

this executes:

```python
break
```

and the menu loop stops.

---

# Step 16 — Where should `break` be used?

The search feature can also use `break` if we add a search mode such as:

```text
Search for:
database

Found:
ERROR Database connection failed

Search again? y/n
```

But we don't need to complicate the first version.

The **menu's Exit option** is already a perfect and natural use of `break`.

So:

```python
elif choice == "4":
    break
```

is enough.

---

# 5. Complete Working Code

Here's the complete beginner-friendly version.

```python
logs = [
    "INFO Server started",
    "INFO User logged in",
    "WARNING Disk usage above 80%",
    "ERROR Database connection failed",
    "INFO Backup completed",
    "ERROR API request failed",
    "WARNING Memory usage above 75%"
]


def analyze_logs(logs):
    info_count = 0
    warning_count = 0
    error_count = 0
    error_messages = []

    for log in logs:

        if log.startswith("INFO"):
            info_count += 1

        elif log.startswith("WARNING"):
            warning_count += 1

        elif log.startswith("ERROR"):
            error_count += 1

            # Remove "ERROR " from the beginning
            error_message = log[6:]
            error_messages.append(error_message)

    return info_count, warning_count, error_count, error_messages


def display_summary(logs, info_count, warning_count, error_count):
    print()
    print("========== SUMMARY ==========")
    print()

    print("Total logs :", len(logs))
    print("INFO       :", info_count)
    print("WARNING    :", warning_count)
    print("ERROR      :", error_count)


def display_errors(error_messages):
    print()
    print("========== ERRORS ==========")
    print()

    if len(error_messages) == 0:
        print("No errors found.")

    else:
        for i in range(len(error_messages)):
            print(f"{i + 1}. {error_messages[i]}")


def search_logs(logs):
    print()
    print("========== SEARCH LOGS ==========")

    keyword = input("Enter search keyword: ").strip()

    if keyword == "":
        print("Please enter a keyword.")
        return

    found = False

    for log in logs:

        if log == "":
            continue

        if keyword.lower() in log.lower():
            print(log)
            found = True

    if not found:
        print("No matching logs found.")


def main():
    # Analyze the logs once
    info_count, warning_count, error_count, error_messages = analyze_logs(logs)

    while True:
        print()
        print("========== LOG SCANNER ==========")
        print()
        print("1. View Summary")
        print("2. View Errors")
        print("3. Search Logs")
        print("4. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            display_summary(
                logs,
                info_count,
                warning_count,
                error_count
            )

        elif choice == "2":
            display_errors(error_messages)

        elif choice == "3":
            search_logs(logs)

        elif choice == "4":
            print()
            print("Exiting Log Scanner...")
            break

        else:
            print()
            print("Invalid choice. Please choose 1-4.")


main()
```

---

# 6. How to Run

Your folder should look like:

```text
cli-log-scanner/
└── log_scanner.py
```

Open a terminal in that folder.

### Windows

```bash
python log_scanner.py
```

or:

```bash
py log_scanner.py
```

### Linux/macOS

```bash
python3 log_scanner.py
```

No packages need to be installed.

---

# 7. Example Run

Start the program:

```text
========== LOG SCANNER ==========

1. View Summary
2. View Errors
3. Search Logs
4. Exit

Choose:
```

Enter:

```text
1
```

Output:

```text
========== SUMMARY ==========

Total logs : 7
INFO       : 3
WARNING    : 2
ERROR      : 2
```

---

## View Errors

Choose:

```text
2
```

Output:

```text
========== ERRORS ==========

1. Database connection failed
2. API request failed
```

---

## Search

Choose:

```text
3
```

Then:

```text
========== SEARCH LOGS ==========
Enter search keyword: database

ERROR Database connection failed
```

Try:

```text
server
```

Output:

```text
INFO Server started
```

Try:

```text
backup
```

Output:

```text
INFO Backup completed
```

---

## Search for something that doesn't exist

```text
Enter search keyword: nginx

No matching logs found.
```

---

## Exit

Choose:

```text
4
```

Output:

```text
Exiting Log Scanner...
```

The `while` loop stops because of:

```python
break
```

---

# 8. Code Explanation

Now let's connect the project directly to the Python concepts you're learning.

---

## `for`

The main log processing happens here:

```python
for log in logs:
```

If there are seven logs, the loop processes seven entries.

Conceptually:

```text
log 1
 ↓
log 2
 ↓
log 3
 ↓
log 4
 ↓
...
 ↓
log 7
```

This is exactly what `for` loops are good at.

---

# `if / elif / else`

We identify severity:

```python
if log.startswith("INFO"):
    info_count += 1

elif log.startswith("WARNING"):
    warning_count += 1

elif log.startswith("ERROR"):
    error_count += 1
```

Think of it as:

```text
Is it INFO?
   ↓ No
Is it WARNING?
   ↓ No
Is it ERROR?
   ↓
Count it
```

---

# `while`

The menu uses:

```python
while True:
```

because we don't know how many times the user wants to use the program.

Maybe:

```text
Summary
   ↓
Errors
   ↓
Search
   ↓
Summary
   ↓
Search
   ↓
Exit
```

A `for` loop isn't appropriate because we don't know the number of menu interactions beforehand.

That's a key distinction:

### `for`

Use when you're going through a known collection or sequence.

```python
for log in logs:
```

### `while`

Use when something should continue until a condition changes.

```python
while True:
```

---

# `break`

We use:

```python
elif choice == "4":
    break
```

This immediately exits the nearest loop.

So:

```text
while True
   ↓
choice = 4
   ↓
break
   ↓
loop ends
```

---

# `continue`

We have:

```python
if log == "":
    continue
```

Suppose the list contained:

```python
logs = [
    "INFO Server started",
    "",
    "ERROR Database failed"
]
```

When Python reaches:

```text
""
```

it does:

```python
continue
```

and skips that log.

The loop then continues with:

```text
ERROR Database failed
```

Again, this is a small example. In a more advanced log parser, `continue` becomes much more useful for skipping malformed or irrelevant entries.

---

# `range()`

We use:

```python
for i in range(len(error_messages)):
```

Suppose:

```python
error_messages = [
    "Database connection failed",
    "API request failed"
]
```

Then:

```python
len(error_messages)
```

is:

```text
2
```

Therefore:

```python
range(2)
```

gives indexes:

```text
0
1
```

Then:

```python
i + 1
```

produces:

```text
1
2
```

for user-friendly numbering.

---

# Nested Conditions

We have an `if` inside a loop:

```python
for log in logs:

    if log == "":
        continue

    if keyword.lower() in log.lower():
        print(log)
```

This is a simple example of **nested logic**.

The program is essentially asking:

```text
For every log:
    Is it empty?
        Yes → skip
        No → check keyword
```

---

# 9. One Important Improvement

There is something I'd change if this were a real log-processing utility.

Currently we identify severity using:

```python
log.startswith("ERROR")
```

That's fine for this beginner project because **we control the log format**.

But real logs could look like:

```text
2026-09-06 12:20:51 ERROR Database connection failed
```

Now:

```python
log.startswith("ERROR")
```

wouldn't work.

Real log parsing usually requires understanding the actual log format, potentially using:

* string splitting
* regular expressions
* structured JSON logs
* dedicated logging systems

Don't jump to regex yet just because it's "more professional." For your current learning stage, `startswith()` is exactly enough.

---

# 10. Another Important Design Decision

We're analyzing the logs once:

```python
info_count, warning_count, error_count, error_messages = analyze_logs(logs)
```

before entering the menu.

That's fine because our logs **never change**.

If we later allow the user to:

```text
add a new log
delete a log
load a new log file
```

then we'd need to re-run the analysis.

That's something you'll encounter naturally when we upgrade this project.

---

# 11. Practice Tasks

Don't immediately jump into file handling.

First modify this version.

## Task 1 — Add `DEBUG`

Add logs such as:

```python
"DEBUG Checking database connection"
```

Create:

```python
debug_count = 0
```

and make the summary show:

```text
DEBUG      : 1
INFO       : 3
WARNING    : 2
ERROR      : 2
```

**Difficulty: Easy**

---

## Task 2 — Add "View Warnings"

Add a fifth menu option:

```text
5. View Warnings
```

Create a list:

```python
warning_messages = []
```

and store the warning text.

For example:

```text
========== WARNINGS ==========

1. Disk usage above 80%
2. Memory usage above 75%
```

**Difficulty: Easy → Medium**

---

## Task 3 — Search only errors

Add:

```text
4. Search Errors
```

The user enters:

```text
database
```

and the program searches only:

```text
ERROR ...
```

rather than all logs.

**Difficulty: Medium**

---

## Task 4 — Add a log counter using `range()`

Create an option:

```text
5. View All Logs
```

and display:

```text
1. INFO Server started
2. INFO User logged in
3. WARNING Disk usage above 80%
...
```

Use `range()` to number the entries.

**Difficulty: Medium**

---

## Task 5 — DevOps challenge

Add a menu option:

```text
5. Check Log Health
```

Make the program decide:

```text
0 errors → HEALTHY

1-2 errors → WARNING

3+ errors → CRITICAL
```

Example:

```text
========== LOG HEALTH ==========

Errors found : 2
Status       : WARNING
```

Use:

```text
if
elif
else
```

to make the decision.

**Difficulty: Medium**

---

# 12. Future DevOps Evolution

This project has a much more useful progression than simply making it bigger for no reason.

### Version 1 — Current

```text
Python list
   ↓
Analyze logs
   ↓
CLI report
```

### Version 2 — File handling

```text
application.log
      ↓
Python
      ↓
Analyze logs
```

You'll learn to read:

```text
.log
```

files.

### Version 3 — Better searching

```text
Search:
database
```

could find:

```text
Database connection failed
Database timeout
Database authentication failed
```

### Version 4 — Log statistics

Something like:

```text
========== LOG REPORT ==========

Total Entries : 15,820

INFO          : 13,102
WARNING       : 1,937
ERROR         : 781

Most Common Error:
Database connection failed
```

### Version 5 — JSON output

```bash
python log_scanner.py --json
```

Output could eventually be:

```json
{
    "total": 15820,
    "info": 13102,
    "warning": 1937,
    "error": 781
}
```

### Version 6 — CI/CD

The scanner could return:

```text
0 → no critical errors
1 → errors detected
2 → scanner failure
```

Then:

```text
CI/CD Pipeline
      ↓
Run Log Scanner
      ↓
Errors?
   ↙       ↘
 No         Yes
 ↓           ↓
Continue    Fail
```

### Version 7 — Monitoring

Eventually:

```text
Application
     ↓
Logs
     ↓
Log Scanner
     ↓
Error detected
     ↓
Alert
     ↓
DevOps engineer
```

That's a legitimate automation pipeline.

---

# 13. What You Learned

### Python concepts

You've practiced:

* `for`
* `while`
* `range()`
* `break`
* `continue`
* `if`
* `elif`
* `else`
* Nested conditions
* Lists
* Dictionaries/return values
* Functions
* Function arguments
* `input()`
* String methods
* Counters
* List `.append()`

### Programming concepts

You practiced:

```text
Collection processing
      ↓
Condition checking
      ↓
Counting
      ↓
Filtering
      ↓
Searching
      ↓
User interaction
```

### DevOps concepts

More importantly, you practiced the basic idea behind **log-processing automation**:

```text
Raw logs
   ↓
Parse
   ↓
Classify
   ↓
Count
   ↓
Filter
   ↓
Report
```

And the next major upgrade should **not** be another unrelated project. When you learn **file handling**, upgrade this exact project so it reads a real `.log` file instead of the hard-coded list.

That will give you a natural progression:

```text
Hard-coded logs
      ↓
File logs
      ↓
Search/filtering
      ↓
Statistics
      ↓
JSON report
      ↓
Exit codes
      ↓
CI/CD log analysis
```

That is a much more realistic Python → DevOps learning path than repeatedly building generic system checkers.
