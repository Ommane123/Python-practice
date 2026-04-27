marks = {
    "Om": 100,
    "Shubhum": 56,
    "Rohan": 54,
    "list": [1,2,3]
}
s = {}                              #empty dict
print(marks, type(marks))           # mutable
print(marks["Om"])                  # no duplicate ele
print(marks["list"])

print("________________________________")
print("Methods\n")
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Om": 99})
print(marks)

print(marks.get("Omi"))      # prints None
print(marks["Omi"])          # returns error