def super_sum(*number):
	if not len(number):
		return "null string"
	total1 = 0
	total2 = 0
	for num in number:
		if type(number)== list:
			for digit in num:
				if type(digit) == str:
					return "wrong data input"
				total2 += digit
		else:
			if type(num) == str:
				return 'wrong data input'
			total1 += num
	return total1 + total2
print super_sum(9,8)
print super_sum(7,5,3)
print super_sum(*[1,2,3])
print super_sum([7,8],1)
