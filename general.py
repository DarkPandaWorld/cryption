import math
import string
import numpy as np


#Principle of Sieve of eratosthenes
#https://code.activestate.com/recipes/117119/
def gen_primes(): # Generates an infinite sequence of prime numbers
  D = {}
  q = 2  # first integer to test for primality.

  while True:
    if q not in D:
      # not marked composite, must be prime  
      yield q 

      #first multiple of q not already marked
      D[q * q] = [q] 
    else:
      for p in D[q]:
        D.setdefault(p + q, []).append(p)
      # no longer need D[q], free memory
      del D[q]
    q += 1

def valid(user_translation_order):
  if user_translation_order == "0" or user_translation_order == "1" or user_translation_order == "2" or user_translation_order == "3":
    return True
  else:
    return False

def generateRow(prime, alphabet):
  a = []
  for i in range(26):
    if i + (prime%26) >= 26:
      a.append(alphabet[i + (prime%26) - 26])
    else: a.append(alphabet[i + (prime%26)])

  # print(a)
  return a

#not used
def translate(character): #returns the index of the character in the alphabet
  return ord(character) - ord('a')

def find(character, first): #returns the index of the row in the matrix
  for i in range(len(first)):
    if first[i] == character:
      return i
  return -1

def primeArr():
  #generate 26 prime numbers in primes array
    infinityprimes = gen_primes() 
    primes = []
    for i in range(26):
        primes.append(next(infinityprimes))
    #   print (next(primes))

    return primes

def fibArr():
    #generate 26 fibonacci numbers in fib array
    fib = [0, 1]
    for i in range(24):
        fib.append(fib[-1] + fib[-2])
    return fib

def generateAlphabet(keyword): # generate my "alphabet" array
    alphabet = [] 
    alphabet_lowercase = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    for i in range(26):
        if i < len(keyword):
            alphabet.append(keyword[i])
            # search_character(keyword[i], alphabet_lowercase)
            alphabet_lowercase.remove(keyword[i])
    
        else:
            alphabet.append(alphabet_lowercase.pop(0))
    return alphabet  

def generateMatrix(alphabet, encodes):
    matrix = []
    for i in range(26): #for every row do this
        num = encodes[i]

        #generate the row (with the prime stuff)
        a = generateRow(num, alphabet)
        matrix.append(a)
    return matrix

def encrypt(matrix, password, message):
  encryption = ""
  for i in range(len(message)):
    row = find(password[i], [row[0] for row in matrix])
    col = find(message[i], matrix[0])
    encryption += matrix[row][col]
  return encryption

def decrypt(matrix, password, message):
  decryption = ""
  for i in range(len(message)):
    row = find(password[i], [row[0] for row in matrix]) #Returns index int of row
    col = find(message[i], matrix[row]) #Returns index int of col

    decryption += matrix[0][col]
  return decryption

def main_encrypt():
    
    user_keyphrase = input("Please enter your keyphrase: ")
    user_pswd = input("Please enter your password: ")
    user_message = input("Please enter your message: ")

    #remove white space
    user_keyphrase = user_keyphrase.replace(" ", "")
    user_pswd = user_pswd.replace(" ", "")
    user_message = user_message.replace(" ", "")

    user_keyphrase = user_keyphrase.lower()
    user_pswd = user_pswd.lower()
    user_message = user_message.lower()

    #choose your translation order
    #0 = default, 1 = prime, 2 = Fibonacci, 3 = random
    user_translation_order = input("Please enter your translation order where 0 = default, 1 = prime, 2 = Fibonacci, 3 = random: ")
    encodes = []

    while not valid(user_translation_order):
        user_translation_order = input("Please enter your translation order where 0 = default, 1 = prime, 2 = Fibonacci, 3 = random: ")
    #check if user uses tool correct 
    if user_translation_order == "0":
        print("You chose default translation order")
        encodes = list(range(26))
    elif user_translation_order == "1":
        print("You chose prime translation order")
        encodes = primeArr()  
    elif user_translation_order == "2":
        print("You chose Fibonacci translation order")
        encodes = fibArr()
    else :
        print("You chose random translation order")
        encodes = np.random.permutation(26)

    alphabet = generateAlphabet(user_keyphrase)
    matrix = generateMatrix(alphabet, encodes)
    
    #make password same length as message
    if len(user_pswd) < len(user_message):
        for i in range(len(user_message) - len(user_pswd)):
            user_pswd += user_pswd[i]
    if len(user_pswd) > len(user_message):
        password = password[:len(user_message)]

    print(encrypt(matrix, user_pswd, user_message))

def main_decrypt():

    user_keyphrase = input("Please enter your keyphrase: ")
    user_pswd = input("Please enter your password: ")
    user_secret_message = input("Please enter your secret message: ")

    #remove white space
    user_keyphrase = user_keyphrase.replace(" ", "")
    user_pswd = user_pswd.replace(" ", "")
    user_secret_message = user_secret_message.replace(" ", "")

    user_keyphrase = user_keyphrase.lower()
    user_pswd = user_pswd.lower()
    user_message = user_message.lower()

    #choose your translation order
    #0 = default, 1 = prime, 2 = Fibonacci, 3 = random
    user_translation_order = input("Please enter the translation order where 0 = default, 1 = prime, 2 = Fibonacci, 3 = random: ")
    encodes = []

    while not valid(user_translation_order):
        user_translation_order = input("Please enter your translation order where 0 = default, 1 = prime, 2 = Fibonacci, 3 = random: ")
    #check if user uses tool correct 
    if user_translation_order == "0":
        print("You chose default translation order")
        encodes = list(range(26))   
    elif user_translation_order == "1":
        print("You chose prime translation order")
        encodes = primeArr()  
    elif user_translation_order == "2":
        print("You chose Fibonacci translation order")
        encodes = fibArr()
    else :
        print("You chose random translation order")
        encodes = np.random.permutation(26)

    alphabet = generateAlphabet(user_keyphrase)
    matrix = generateMatrix(alphabet, encodes)

    #make password same length as message
    if len(user_pswd) < len(user_secret_message):
        for i in range(len(user_secret_message) - len(user_pswd)):
            user_pswd += user_pswd[i]
    if len(user_pswd) > len(user_secret_message):
        password = password[:len(user_secret_message)]
   
    print(decrypt(matrix, user_pswd, user_secret_message))




#Please first read READ.md to understand the types of things you will be asked
type_request = input("Please enter 0 for encryption or 1 for decryption: ")
if type_request == "0":
    main_encrypt()
elif type_request == "1":
    main_decrypt()
else:
    print("Not valid, program terminates")
