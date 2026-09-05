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