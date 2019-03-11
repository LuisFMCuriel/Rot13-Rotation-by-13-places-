#Writted by: Luis Felipe Morales Curiel

def new_number(number):
	if number >= 97 and number <= 122:
		if number + 13 > 122:
			S = 122 - number;
			P = 13 - S;
			new = 96 + P;
		else:
			new = number + 13;
	elif number >= 65 and number <= 90:
		if number + 13 > 90:
			S = 90 - number;
			P = 13 - S;
			new = 64 + P;
		else:
			new = number + 13;
	else:
		new = number;
	return new;

def Rot13(message):
	new_message = "";
	size = len(message);
	for x in range(0,size):
		number = ord(message[x]);
		new_message += chr(new_number(number)); 

	return new_message;




message = "Jul qvq gur puvpxra pebff gur ebnq? Gb trg gb gur bgure fvqr!";
encrypted = Rot13(message);
print(encrypted);

message = "The Quick Brown Fox Jumps Over The Lazy Dog";
encrypted = Rot13(message);
print(encrypted);