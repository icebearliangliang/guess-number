import random
r = random.randint(1, 100)
count=0
while True:
	num = input('please guess number: ')
	num = int(num)
	count = count + 1 # count += 1
	if num == r:
		print('you are right!')
		print('this is the', count, 'time')
		break
	elif num > r:
		print('too big')
	elif num < r:
		print('too small')
	print('this is the', count, 'time')