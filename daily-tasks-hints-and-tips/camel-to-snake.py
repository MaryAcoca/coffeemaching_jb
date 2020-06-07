import re

name = input()
name_s = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
print(name_s)

