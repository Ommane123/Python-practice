letter = '''Dear <|Name|>.
<|date|>'''

print(letter.replace("<|Name|>", "Om").replace("<|date|>", "24 dec 2345"))