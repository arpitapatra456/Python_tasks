import os
import re
files = os.listdir("C:\\Users\\arpatra\\")
for var in files:
    if re.search("pdf$|csv$", var):
        print(var)
