from pathlib import Path

log_directory = Path(__file__).parent / "logs"

if log_directory.exists():
    print("Logs directory already exists.")

logs_files = list(log_directory.glob("*.log"))

print("==============================")
print("       LOG REPORT")
print("==============================")
print()

print("Log files found: ")

for log_file in logs_files:
    print(f"-", log_file.name)

print()
print("Total: ", len(logs_files))

if len(logs_files) == 0:
    print("No logs found.")

