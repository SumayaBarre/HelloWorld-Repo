upper_bound=int(input("enter a upper bound "  ))

deficeint_numbers = 0
perfect_numbers = 0
abundant_numbers = 0
divisor_sum = 0
for number in range(1,upper_bound +1):
	for num in range(1,number):
		if number % num == 0:
			divisor_sum +=  num
	if divisor_sum > number:
		deficeint_numbers +=  1
	elif divisor_sum < number:
		abundant_numbers+= 1
	else:
		perfect_numbers +=1
	divisor_sum = 0	

print(f"between 1 and{upper_bound} there:")
print(f"{deficeint_numbers} deficeint numbers")
print(f"{abundant_numbers} abundant numbers")
print(f"{perfect_numbers} perfect numbers")	
		
				



