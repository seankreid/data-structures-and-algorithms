#!usr/bin/env python3

# Sean Reid

def toBinary(n): #take a positive int and convert to binary(sequence of length 8)
	binary = ""
	while n > 0:
		if (n % 2 !=0):
			binary = "1" + binary
		else:
			binary = "0" + binary
		n = n // 2
	while len(binary) % 8 != 0:
		binary = "0" + binary
	return (binary)

def toDecimal(data):
	decimal = 0
	for number in data:
		decimal *= 2
		if number == '1':
			decimal +=1
	return (decimal)

def sum(n,m): #add two binary sequences together, return the sum in decimal form, use zfill function to fill remaining 0s
	bin1 = toBinary(n)
	bin2 = toBinary(m)
	sequenceLength = max(len(bin1), len(bin2))
	bin1 = bin1.zfill(sequenceLength)
	bin2 = bin2.zfill(sequenceLength)
	c = 0 #carry value for adding binary sequences
	solution = ""
	for i in range(sequenceLength-1,-1,-1):
		s = c
		if (bin1[i] == "1"):
			s += 1
		else:
			s += 0
		if (bin2[i] == "1"):
			s += 1
		else:
			s += 0 
		solution = ("1" if s % 2 == 1 else "0") + solution
		if (s < 2):
			c = 0
		else:
			c = 1
	if c != 0:
		solution = "1" + solution
	return (toDecimal(solution.zfill(sequenceLength)))

def doubleIt(n): #multiply binary sequence by 2
	bin1 = toBinary(n)
	doubleBin1 = bin1[1:] + "0"
	return (toDecimal(doubleBin1))


def main(): #test my functions
	print (toBinary(10))
	print (toDecimal ('01100100'))
	print (sum(9,16))
	print (doubleIt(25))

if __name__ == '__main__':
	main()
