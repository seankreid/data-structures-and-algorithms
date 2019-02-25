#!/usr/bin/env python3
# Sean Reid



def acctBalance(deposit,interestRate,years):
	if years == 0:
		return (deposit) # no years, so just return initial amount
	else:
		return acctBalance(deposit * (1 + interestRate), interestRate, years -1)

def main():
	startingAmount = float(input("What is your initial deposit?"))
	interst = float(input("What is the interst rate?")) / 100 #convert number to decimal form
	year = float(input("How many years?"))
	print ("Your amount after",year, "years is:")
	print (acctBalance(startingAmount,interst,year))

if __name__ == '__main__':
	main()
