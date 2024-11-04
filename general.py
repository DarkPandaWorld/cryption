import math
import string
import random


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
  
def find(character, first): #returns the index of the row in the matrix
  for i in range(len(first)):
    if first[i] == character:
      return i
  return -1

def primeArr():
  #generate 26 prime numbers in primes array
    infinityprimes = gen_primes() 
    # primes = []
    # for i in range(26):
    #     primes.append(next(infinityprimes))
    # #   print (next(primes))
    return infinityprimes
    # return primes

def fibArr():
    # Fibonacci sequence generator
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
    # print(fib)
    # return fib

def generateEncode(list): 
    number_arr = []
    while len(number_arr) < 26:
        mom = next(list) % 26

        if(mom not in number_arr and mom != 0):
            number_arr.append(mom)
        else:
            while mom in number_arr or mom == 0:
                mom += 1
            number_arr.append(mom)
    return number_arr


def generateAlphabet(keyword): # generate my "alphabet" array
    alphabet = [] 
    alphabet_lowercase = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    used_characters = set()  # Track used characters to avoid duplicates

# Add characters from the keyword to the alphabet
    for char in keyword:
        if char not in used_characters:
            alphabet.append(char)
            used_characters.add(char)
            try:
                alphabet_lowercase.remove(char)
            except ValueError:
                pass

    # Add remaining characters from alphabet_lowercase to the alphabet
    for char in alphabet_lowercase:
        alphabet.append(char)
    return alphabet  

def generateMatrix(alphabet, numbers):
    # print(len(alphabet))
    # print(alphabet)
    matrix = []
    for i in numbers:
        arr = []
        for j in range(26):
            # print(j+i % 26)
            arr.append(alphabet[(j + i) % 26])
        matrix.append(arr)
    
    # print(matrix)
       
    return matrix

def write_matrix(matrix):
   # Write the matrix to a text file
  with open("matrix.txt", "w") as file:
    for row in matrix:
        file.write(" ".join(row) + "\n")


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
    user_translation_order = input("Please enter your translation order where 0 = default, 1 = prime, 2 = fibonacchi, 3 = random: ")
    encodes = []

    while not valid(user_translation_order):
        user_translation_order = input("Please enter your translation order where 0 = default, 1 = prime, 2 = fibonacchi, 3 = random: ")
    #check if user uses tool correct 
    if user_translation_order == "0":
        print("You chose default translation order")
        encodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    elif user_translation_order == "1":
        print("You chose prime translation order")
        encodes = generateEncode(gen_primes())
    # elif user_translation_order == "2":
    #     print("You chose Fibonacci translation order")
    #     encodes = fibArr()
    elif user_translation_order == "2":
        print("You chose fibonacchi translation order")
        encodes = generateEncode(fibArr())
        # encodes = (26, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25)
    else:
        print("You chose random translation order")
        encodes = list(range(26)) 
        random.shuffle(encodes)
        print(encodes)



        print("Do you want to save your translation order to a file? (y/n): ")
        user_dec = input()
      
        if user_dec == "y":
            with open("translation_order.txt", "w") as file:
                for i in encodes:
                    file.write(str(i) + " ")
  

    print("Works till here")

  

    alphabet = generateAlphabet(user_keyphrase)
    matrix = generateMatrix(alphabet, encodes)

    print("Works after generating matrix")  
    
    #make password same length as message
    if len(user_pswd) < len(user_message):
        for i in range(len(user_message) - len(user_pswd)):
            user_pswd += user_pswd[i]
    if len(user_pswd) > len(user_message):
        user_pswd = user_pswd[:len(user_message)]
    
    user_dec = input("Do you want to write the matrix to a file? (y/n): ")
    if user_dec == "y":
        write_matrix(matrix)

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
    user_secret_message = user_secret_message.lower()

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
        user_pswd = user_pswd[:len(user_secret_message)]
   
    print(decrypt(matrix, user_pswd, user_secret_message))




#Please first read READ.md to understand the types of things you will be asked
type_request = input("Please enter 0 for encryption or 1 for decryption: ")
if type_request == "0":
    main_encrypt()
elif type_request == "1":
    main_decrypt()
else:
    print("Not valid, program terminates")
