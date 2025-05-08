import re 

text = "Searching for digits in text 87 is not difficult 54 with regex 109!!!"

pattern = "\d+"
result = re.findall(pattern, text)
print(result)

pattern = "di[a-z]+"
result = re.findall(pattern, text)
print(result)
