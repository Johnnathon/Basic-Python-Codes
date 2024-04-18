import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = []
for x in alphabet:
    uppercase.append(x.upper())

pass_length = random.randint(8,12)
password = ""

while len(password) < pass_length:
     character = random.randint(1,3)
     if character == 1:
        password += alphabet[random.randint(0,25)]
     elif character == 2:
        password += uppercase[random.randint(0, 25)]
     elif character == 3:
        password += str(random.randint(0,9))

print (password)
