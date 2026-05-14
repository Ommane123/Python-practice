# Given a integer N, find and print the smallest digit and the largest digit present in the number

n = int(input("Enter the Number: ").strip())            # .strip() -->Return a copy of the string with leading and trailing whitespace removed

min_digit = 9
max_digit = 0

while n > 0:
    digit = n % 10
    min_digit = min(digit, min_digit)
    max_digit = max(digit, max_digit)
    n //= 10

print(f"Smallest Digit = {min_digit}\nLargest Digit = {max_digit}")