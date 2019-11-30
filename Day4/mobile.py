#take input as the phone number and validate

import re
import os.path
pattern = '^[0-9]{10}$'
numb = input("Enter the number")

matches = re.search(pattern, numb)
if matches:
    print("matched")
else:
    print("not matched")