import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits

def password_generator(length=8): 
   printable = f'{LETTERS}{NUMBERS}'

   printable = list(printable)
   random.shuffle(printable)
 

   return random_password
