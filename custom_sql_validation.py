import os
import re

# Define the pattern to match UPDATE statements without WHERE clauses
update_pattern = re.compile(r'^\s*UPDATE\s+\w+\s+SET\s+(?!.*\bWHERE\b)', re.IGNORECASE)

# Function to scan SQL files in a directory and check for the specified pattern
def check_sql_files(directory):
    issues_found = False
    for filename in os.listdir(directory):
        if filename.endswith('.sql'):
            with open(os.path.join(directory, filename), 'r') as file:
                for line_number, line in enumerate(file, start=1):
                    if update_pattern.match(line):
                        print(f"Issue found in '{filename}' at line {line_number}: UPDATE statement without WHERE clause")
                        issues_found = True
    return issues_found

# Run the script
if __name__ == "__main__":
    sql_directory = 'files'  # Update this with your directory containing SQL files
    issues = check_sql_files(sql_directory)
    if issues:
        exit(1)  # Exit with non-zero status code if issues were found
