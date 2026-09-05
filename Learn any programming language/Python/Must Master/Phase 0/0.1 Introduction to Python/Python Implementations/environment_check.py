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