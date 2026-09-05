milestones = [
    {
        "year": 1989,
        "event": "Python development begins",
        "description": "Guido van Rossum begins developing Python."
    },
    {
        "year": 1991,
        "event": "Python 0.9.0 released",
        "description": "Python 0.9.0 is released publicly."
    },
    {
        "year": 1994,
        "event": "Python 1.0 released",
        "description": "Python 1.0 is released with several important features."
    },
    {
        "year": 2000,
        "event": "Python 2.0 released",
        "description": "Python 2.0 is released with major language improvements."
    },
    {
        "year": 2001,
        "event": "Python Software Foundation established",
        "description": "The Python Software Foundation is established."
    },
    {
        "year": 2008,
        "event": "Python 3.0 released",
        "description": "Python 3.0 is released as a major new version of Python."
    },
    {
        "year": 2020,
        "event": "Python 2 reaches EOL",
        "description": "Python 2 officially reaches end of life."
    }
]


# Display the title
print("==============================")
print("      PYTHON HISTORY")
print("==============================")

# Display the timeline
print()
print("Timeline:")

for milestone in milestones:
    print(milestone["year"], "-", milestone["event"])


# Ask the user for a year
year = int(input("\nEnter a year to learn more: "))

# Search for the year
found = False

for milestone in milestones:
    if milestone["year"] == year:
        print()
        print("Year:", milestone["year"])
        print("Event:", milestone["event"])
        print("Description:", milestone["description"])
        found = True


# Handle a year that was not found
if not found:
    print()
    print("Sorry, no milestone was found for that year.")