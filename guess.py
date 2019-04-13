import random
start = input('请输入范围开始值: ')
end = input('请输入范围结束值: ')
r = random.randint(1, 100)
count=0
while True:
	num = input('请猜数字: ')
	num = int(num)
	count = count + 1 # count += 1
	if num == r:
		print('你猜对了!')
		print('这是你猜的第', count, '次')
		break
	elif num > r:
		print('too big')
	elif num < r:
		print('too small')
	print('这是你猜的第', count, '次')
		