# Rot13
Simple letter substitution cipher that replaces a letter with the 13th letter after it, in the alphabet.

Table with the transformation order:

Input 
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 

Output 
NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm 


UNIX command for Rot13 cipher: tr 'A-Za-z' 'N-ZA-Mn-za-m' <<< "message"

For more details visit:
https://en.wikipedia.org/wiki/ROT13
