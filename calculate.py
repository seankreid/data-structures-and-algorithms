#!/usr/bin/env python3

# Sean Reid

import array_stack #for pop, push etc

def solve(num, op): #evaluate the numbers
	num2, num1 = number.pop(), number.pop()
	if op == "+":
		result = num1 + num2
	elif op == "-":
		result = num1 - num2
	elif op == "*":
		result = num1 * num2
	elif op == "/":
		result = num1 / num2
	return result

def calculate(expression): #calculate the result of the postfix expression
	nums = array_stack.ArrayStack()
	for e in expression:
		if type(e) is int: #check if element is a number or not
			nums.push(float(e))
		else:
			nums.push(solve(nums, e))
	return (nums.pop())

def read_file(): #read text file line by line
	fp = open("input.txt", "r")
	return fp.readlines()

def main(): #read file line by line and solve each expression 
	answers = open("answers.txt", "w")
	lines = read_file()
	for expression in file:
		expression.strip().split() #split expression
		answer = calculate(expression)
		answers.write(str(answer) + "\n") #string to print onto file

if __name__ == '__main__':
	main()












