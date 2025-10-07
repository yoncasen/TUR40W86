import random 

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = int(input("Parolanın uzunluğu ne olsun?"))

password = ""

for i in range(length):
  char = random.choice(characters)
  password += char

print(password)

