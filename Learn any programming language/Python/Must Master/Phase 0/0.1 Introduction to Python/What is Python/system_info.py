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