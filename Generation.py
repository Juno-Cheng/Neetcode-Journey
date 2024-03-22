import os
import datetime

# Set the directory 
directory = '/path/to/your/directory'

# Set the file name format
file_name_format = 'date-leetcodes-review.py'

# Get the current date and time
current_date = datetime.datetime.now().strftime('%Y-%m-%d')

# Create the file name
file_name = file_name_format.replace('date', current_date)

content = '''"""
LeetCode Review Notes
Date: {}

This file contains review notes and solutions for LeetCode problems.
"""
'''.format(current_date)

# Write the content to the file
with open(os.path.join(directory, file_name), 'w') as f:
    f.write(content)

with open(os.path.join(directory, file_name), 'w') as f:
