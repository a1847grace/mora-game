import random
while True:
	rival = str
	x = random.randint(1,3)
	if x == 1:
		rival = "剪刀"
	elif x == 2:
		rival = "石頭"
	else:
		rival = "布"
	user = str
	print ('請輸入剪刀或石頭或布')
	user = input()
	if user == "剪刀":
		if x == 1:
			print ('對方出', rival, '，平手！')
			break
		elif x == 2:
			print ('對方出', rival, '，你輸了！')
			break
		else:
			print ('對方出', rival, '，你贏了！')
			break
	elif user == "石頭":
		if x == 1:
			print ('對方出', rival, '，你贏了！')
			break
		elif x == 2:
			print ('對方出', rival, '，平手！')
			break
		else:
			print ('對方出', rival, '，你輸了！')
			break
	elif user == "布":
		if x == 1:
			print ('對方出', rival, '，你輸了！')
			break
		elif x == 2:
			print ('對方出', rival, '，你贏了！')
			break
		else:
			print ('對方出', rival, '，你輸了！')
			break
	else:
		print ('只能輸入剪刀或石頭或布，不要亂輸入')