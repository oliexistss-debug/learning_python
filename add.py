# function definition
def add(number1, number2):
	result = number1 + number2
	#print(f"output={result}")
	return result

# using the function, or
# calling the function
#add(number1=6, number2=7)
#add(number1=1000, number2=-1)
#add(number1=1000, number2=0.1)
#add(number1="wh", number2="at")
#add(2,3)

output_of_add = add(number1=6, number2=7)
print(f"output of add is: {output_of_add}")

another_output_of_add = add(number1=1000, number2=-1)
print(f"output of add is: {another_output_of_add}")

x = add(number1=output_of_add, number2=another_output_of_add)
print(x)


def multiply(num1, num2):
	answer = num1 * num2
	print(f"output={answer}")
	return answer



multiply(num1=6, num2=7)
rgbgfb=multiply(num1=6, num2=7)
print(rgbgfb)

print("good lesson")