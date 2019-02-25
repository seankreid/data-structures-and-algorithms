#!usr/bin/env python3
# Sean Reid


def GCD(m,n):
	rem = m % n
	if rem == 0:
		return n
	elif rem == 1:
		return 1
	return GCD(n,rem)


def main():
	print("GCD calculator!")
	number1 = int(input("Enter a number:"))
	number2 = int(input("Enter another number:"))
	if number1 and number2 == 0:
		print("Error! Both numbers cannot be 0")
	else:
		print(GCD(number1,number2))


if __name__ == '__main__':
	main() 