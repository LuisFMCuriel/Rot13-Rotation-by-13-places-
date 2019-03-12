# Rot13 cipher
![alt text](http://lh3.ggpht.com/c1XhkTPJdlK1dn5oopdRQsibKA9k-nZTvCxJGtgpYkkX_FFlS5E_bIsW0fSHEYLKIA=w300)

Caesar Cipher. Simple letter substitution cipher that replaces a letter with the 13th letter after it, in the alphabet.

## How it works?

It just replaces a letter with the 13th letter after it for example if we add the next input:

```
> ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 
```
We are going to get the next Output:

```
> NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm  
```

So if we introduce A in the Rot13 Function:
```
ROT13('A') = 'N'
```
UNIX command for Rot13 cipher: 

```
> tr 'A-Za-z' 'N-ZA-Mn-za-m' <<< "message"  
```


For more details visit:
*https://en.wikipedia.org/wiki/ROT13
