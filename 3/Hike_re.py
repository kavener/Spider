import re

content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group())
# print(result.span())

result = re.match('^Hello (.*?) World', content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())