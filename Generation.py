import os
import datetime

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Set the Review directory relative to the script location
directory = os.path.join(script_dir, 'Review')
file_name_format = 'date-leetcodes-review.py'
current_date = datetime.datetime.now().strftime('%Y-%m-%d')

# Create the Review directory if it doesn't exist
os.makedirs(directory, exist_ok=True)

# Create the file name
file_name = file_name_format.replace('date', current_date)

content = '''"""
LeetCode Review Notes
Date: {}

This file contains review notes and solutions for LeetCode problems.
"""
'''.format(current_date)

# Write the content to the file
file_path = os.path.join(directory, file_name)
with open(file_path, 'w') as f:
    f.write(content)

print(f"Review file created: {file_path}")


