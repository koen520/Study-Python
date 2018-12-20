import math
def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		pass
	try:
		import unicodedata
		unicodedata.numeric(s)
		return True
	except (TypeError, ValueError):
		pass 
	return False
	
while True:
	shuru=input('输入圆的半径\n')
	if is_number(shuru) is False:
	    print ('请输入数字，谢谢\n')
	
	elif float(shuru)<=0:
	    print ('数字需要大于0，谢谢 \n')
	else: 
	    rr=float(shuru)
	    print ('半径为{0}的圆的面积为{1}'.format(shuru,(math.pi*rr**2)))
		