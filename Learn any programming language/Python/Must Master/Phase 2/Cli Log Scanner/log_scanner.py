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