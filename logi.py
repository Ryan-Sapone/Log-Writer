import datetime
import sys

# Define a function to create a new entry in the log file
def log_entry(title, description):
    # Get the current date and time
    now = datetime.datetime.now()

    # Open the log file in append mode
    # Edit the filename
    with open("EDIT_ME.txt", "a") as log_file:
        # Write the entry to the file
        log_file.write(f"[{now}] {title}\n")
        log_file.write(f"{description}\n")
        log_file.write("\n")

# Prompt the user to enter a new log entry
title = input("Enter a title for the log entry: ")
print("Enter a description for the log entry (paste your text and press CTRL-D on a new line to finish):")
description = sys.stdin.read()

# Check if the user entered any text
if not description:
    # The user did not enter any text, so don't create a log entry
    print("No log entry created.")
else:
    # Create a new entry in the log file
    log_entry(title, description)
    print("Log entry created successfully.")
