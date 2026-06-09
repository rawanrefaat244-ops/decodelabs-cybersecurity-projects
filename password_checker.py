import string

print("Welcome to DecodeLAbs Password Checker!")
print("Enter a password to check if its strength.\n")

password = input("Enter your password: ")

has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(char in string.punctuation for char in password)
is_long = len(password) >= 8

score = 0

if is_long:
    score += 1

if has_uppercase:
    score += 1

if has_lowercase:
    score += 1

if has_digit:
    score += 1

if has_symbol:
    score += 1


print("\nPassword Analysis:")
print("Length 8 or more:", is_long)
print("Contains uppercase:", has_uppercase)
print("Contains lowercase:", has_lowercase)
print("Contains number:", has_digit)
print("Contains symbol:", has_symbol)

if score <= 2:
    strength = "weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print("\nPassword Strength:", strength)
