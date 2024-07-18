import re
text = "Hello, my name is saran and my email is saran@gmail.com"
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regex = re.compile(pattern)
matches = regex.findall(text)
for match in matches:
    print("Match found: ", match)
