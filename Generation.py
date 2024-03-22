import os
import datetime

# Set the directory 
directory = '/Users/omega/Desktop/Github/Neetcode-Journey/Review'
file_name_format = 'date-leetcodes-review.py'
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


