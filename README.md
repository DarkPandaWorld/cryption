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

For example, if your password is "cat", the program will move "cat" to the front of the alphabet and arrange the remaining letters behind it. The resulting alphabet will look like this:

`{c, a, t, b, d, e, ..., x, y, z}`
No duplicate letters will be present.

**Creating the Matrix**

To create a 26-row matrix, we apply the translation method chosen:

_Default Translation:_ Each row shifts the letters by one position.

`Row 1: c, a, t, b, d, e, ...
Row 2: a, t, b, d, e, f, ...
Row 3: t, b, d, e, f, g, ...
...`

_Prime and Fibonacci Translations:_ Each of these methods shifts the alphabet based on their respective sequences.


**Encrypting and Decrypting Messages**

Encryption: To encrypt a message, look at the first column for the letter
			from your password and the first row for the letter from your
			message. The intersection of these will give you the encrypted
			character.

	Example: With the password "cat" and message "hello":

	Find the row starting with 'c'.
	Find the column starting with 'h'.
	The character at the intersection is your encrypted code.
	
	Decryption: For decryption, the process is reversed:
	Find the index of the row corresponding to your password character.
	Locate the right column in that row to retrieve the first entry.
