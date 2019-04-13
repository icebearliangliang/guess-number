import random
r = random.randint(1, 100)
while True:
	num = input('please guess number: ')
	num = int(num)
	if num == r:
		print('you are right!')
		break
	elif num > r:
		print('too big')
	elif num < r:
		print('too small')