import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits

def password_generator(length=8): 
   alphaNum = f'{LETTERS}{NUMBERS}'

   alphaNum = list(alphaNum)
   random.shuffle(alphaNum)
 
   gen_password = random.choices(alphaNum, k=length)
   gen_password = ''.join(gen_password)
   print(gen_password)

   return gen_password

password_generator(int(input("Enter a Number: ")))   
