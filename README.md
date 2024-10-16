# Cryption

**Overview**

This program allows you to encrypt and decrypt messages using Vigenère tables, complete with some unique features.

**Important Information Before You Start**

This program will help you encrypt or decrypt messages based on your input. Here's how it works:

**Steps to Use the Program**
1. Choose Your Goal:
	- Enter `0` for encryption
	- Enter `1` for decryption
2. Input Required Information:
	Keyphrase: Used to construct the alphabet for the matrix.
	Password: Serves as a key for the encryption/decryption process.
	Message: Your secret message that you wish to encrypt or decrypt.

	Keyphrase vs. Password:
		The keyphrase builds the "alphabet" for the matrix.
		The password acts as a key for the encryption/decryption.

3. Select a Translation Order: You can choose from the following options:
	Default: Shifts letters one by one.
	Prime: Shifts letters based on prime numbers.
	Fibonacci: Uses the Fibonacci sequence to shift letters.
	Random: This option is more experimental and can lead to unpredictable
			results, making it a fun challenge for those interested in
			cracking their own codes.

****Constructing the Alphabet**

For example, if your keyphrase is "cat", the program will move "cat" to the front of the alphabet and arrange the remaining letters behind it. The resulting alphabet will look like this:

`{c a t b d e f g h i j k l m n o p q r s u v w x y z}`
No duplicate letters will be present.

**Creating the Matrix**

To create a 26-row matrix, we apply the translation method chosen:

_Default Translation:_ Each row shifts the letters by one position.

![image](https://github.com/user-attachments/assets/20bfff1d-5e24-4020-87fb-bf4f0f8eaa2e)


_Prime and Fibonacci Translations:_ Each of these methods shifts the alphabet based on their respective sequences. So those matrices would look something like this:
Prime: 

![image](https://github.com/user-attachments/assets/63a1e2e2-9fbf-4259-b980-bbfabe1ef7e3)



Fibo:

![image](https://github.com/user-attachments/assets/b8222d2a-53f9-4abf-b0b3-6cb64c6915cc)



**Encrypting and Decrypting Messages**

Encryption: To encrypt a message, look at the first column for the letter from your password and the first row for the letter from your message. The intersection of these will give you the encrypted character.

	Example: 
 		We choose the following:
		Keyphrase: cat
  		Password: fibo
    		message: hello

	As before, our matrix looks like this:
		![image](https://github.com/user-attachments/assets/5105f0e2-9c96-4413-8d32-cb5aeb85541e)

	Now we make password and message same length, to do that we enlarge/shorten the password to the 		message length... by repeating, if necessary the password. 
   		So we get :
     			msg:	h e l l o
			psw: 	f i b o f

	Now, we take each pair: 
     			We search the first column for letter f and get a row. 
			We search the first row for letter h and get a column.
   			The intersection is our encrypted character: 
      		
![image](https://github.com/user-attachments/assets/0c43a598-bc85-4c13-98e9-7bb6f42deb75)

      
		Decryption: For decryption, the process is reversed:
		Find the index of the row corresponding to your password character.
		Locate the right column in that row to retrieve the first entry.
