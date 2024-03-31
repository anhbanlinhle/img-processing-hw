import re

def is_valid(email):
    pattern = r'^[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, email) is not None

n = int(input())
emails = [input() for i in range(n)]

valid_emails = sorted(filter(is_valid, emails))

print(valid_emails)