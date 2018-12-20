import random
print ('这是个猜数字游戏，请输入整数。\n')
print ('电脑已经随机在1到100之间选出了一个数，现在你来猜猜看吧。仅限整数哦。\n')
guess=0
realnumber = random.randint(0,101)
#realnumber = 50
numbers = input('首先，请输入一个整数。放心，如果不对的话电脑会给你提示的。\n')

while True:
	guess += 1
	if not numbers.isdigit():
		print ('叫你输入整数，你怎么这么不听话呢？')
		numbers = input('快输入整数。')
	elif int(numbers)<0 or int(numbers)>100:
		print ('说了数字是0到100之间，你搞个范围外干嘛呢？要不我下次搞个范围无限的让你猜个爽？')
		numbers = input('快输入0到100以内的数字。')
	else:
		number = int(numbers)
		if number == realnumber:
			if guess == 1:
				print ('你作弊了吧？{}次就猜中了？不去考虑买张彩票么？' .format(guess))
				break
			elif 1 < guess < 5:
				print ('我那个去，你居然{}次就猜中了。' .format(guess))
				break
			else:
				print ('居然{}次才猜对，你不行啊。' .format(guess))
				break
		elif number > realnumber:
			print ('你猜的数字太大了。')
			numbers = input('请再次输入')
			
		elif number < realnumber:
			print ('你猜的数字太小了。')
			numbers = input('请再次输入')
			
		else:
			print ('系统错误，联系作者。')
	