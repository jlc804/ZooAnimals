import json
person = '{"name": "Bob", "languages": ["English", "French"]}'
mystery = json.loads(person)
print(type(mystery))