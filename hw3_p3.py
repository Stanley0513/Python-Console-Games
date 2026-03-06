a="+---+---+---+---+---+---+---+"
a1="|   |   |   |   |   |   |   |"
L6=list(a1)
L5=list(a1)
L4=list(a1)
L3=list(a1)
L2=list(a1)
L1=list(a1)
#印一次空白的遊戲格式
print(a)
print("".join(L6))
print(a)
print("".join(L5))
print(a)
print("".join(L4))
print(a)
print("".join(L3))
print(a)
print("".join(L2))
print(a)
print("".join(L1))
print(a)
print("  0   1   2   3   4   5   6")
#開始分別判斷兩位玩家的選擇
i=1
while 1:
	#玩家X先
	while i==1:
		X=input("Player X >>")
		#確認是否在範圍內
		if not X.isdigit():
			print("Invalid input, try again [0-6].")
			i=1
		elif int(X)>6 or int(X)<0:
			print("Out of range, try again [0-6].")
			i=1
		else:
			c=int(X)*4+2
			if L1[c]=="X" or L1[c]=="O":
				if L2[c]=="X" or L2[c]=="O":
					if L3[c]=="X" or L3[c]=="O":
						if L4[c]=="X" or L4[c]=="O":
							if L5[c]=="X" or L5[c]=="O":
								if L6[c]=="X" or L6[c]=="O":
									print("This column is full. Try another column.")
									i=1
								else:
									L6[c]="X"
									i=2
							else:	
								L5[c]="X"
								i=2
						else:	
							L4[c]="X"
							i=2
					else:	
						L3[c]="X"
						i=2
				else:	
					L2[c]="X"
					i=2
			else:	
				L1[c]="X"
				i=2
		#合理範圍即印出結果
		if i==2:		
			print(a)
			print("".join(L6))
			print(a)
			print("".join(L5))
			print(a)
			print("".join(L4))
			print(a)
			print("".join(L3))
			print(a)
			print("".join(L2))
			print(a)
			print("".join(L1))
			print(a)
			print("  0   1   2   3   4   5   6")
	#確認是否X獲勝
	z=0
	for j in range(0,1):
		c=j*4+2
		if L1[c]==L1[c+4]==L1[c+8]==L1[c+12]==L1[c+16]==L1[c+20]==L1[c+24]=="X":
			L1[c]=L1[c+4]=L1[c+8]=L1[c+12]=L1[c+16]=L1[c+20]=L1[c+24]="x"
			z+=1
			break				
		elif L2[c]==L2[c+4]==L2[c+8]==L2[c+12]==L2[c+16]==L2[c+20]==L2[c+24]=="X":
			L2[c]=L2[c+4]=L2[c+8]=L2[c+12]=L2[c+16]=L2[c+20]=L2[c+24]="x"
			z+=1
			break	
		elif L3[c]==L3[c+4]==L3[c+8]==L3[c+12]==L3[c+16]==L3[c+20]==L3[c+24]=="X":
			L3[c]=L3[c+4]=L3[c+8]=L3[c+12]=L3[c+16]=L3[c+20]=L3[c+24]="x"
			z+=1
			break	
		elif L4[c]==L4[c+4]==L4[c+8]==L4[c+12]==L4[c+16]==L4[c+20]==L4[c+24]=="X":
			L4[c]=L4[c+4]=L4[c+8]=L4[c+12]=L4[c+16]=L4[c+20]=L4[c+24]="x"
			z+=1
			break	
		elif L5[c]==L5[c+4]==L5[c+8]==L5[c+12]==L5[c+16]==L5[c+20]==L5[c+24]=="X":
			L5[c]=L5[c+4]=L5[c+8]=L5[c+12]=L5[c+16]=L5[c+20]=L5[c+24]="x"
			z+=1
			break	
		elif L6[c]==L6[c+4]==L6[c+8]==L6[c+12]==L6[c+16]==L6[c+20]==L6[c+24]=="X":
			L6[c]=L6[c+4]=L6[c+8]=L6[c+12]=L6[c+16]=L6[c+20]=L6[c+24]="x"
			z+=1
			break	
		else:
			z+=0
			continue
	for j in range(0,2):
		c=j*4+2
		if L1[c]==L1[c+4]==L1[c+8]==L1[c+12]==L1[c+16]==L1[c+20]=="X":
			L1[c]=L1[c+4]=L1[c+8]=L1[c+12]=L1[c+16]=L1[c+20]="x"
			z+=1
			break				
		elif L2[c]==L2[c+4]==L2[c+8]==L2[c+12]==L2[c+16]==L2[c+20]=="X":
			L2[c]=L2[c+4]=L2[c+8]=L2[c+12]=L2[c+16]=L2[c+20]="x"
			z+=1
			break	
		elif L3[c]==L3[c+4]==L3[c+8]==L3[c+12]==L3[c+16]==L3[c+20]=="X":
			L3[c]=L3[c+4]=L3[c+8]=L3[c+12]=L3[c+16]=L3[c+20]="x"
			z+=1
			break	
		elif L4[c]==L4[c+4]==L4[c+8]==L4[c+12]==L4[c+16]==L4[c+20]=="X":
			L4[c]=L4[c+4]=L4[c+8]=L4[c+12]=L4[c+16]=L4[c+20]="x"
			z+=1
			break	
		elif L5[c]==L5[c+4]==L5[c+8]==L5[c+12]==L5[c+16]==L5[c+20]=="X":
			L5[c]=L5[c+4]=L5[c+8]=L5[c+12]=L5[c+16]=L5[c+20]="x"
			z+=1
			break	
		elif L6[c]==L6[c+4]==L6[c+8]==L6[c+12]==L6[c+16]==L6[c+20]=="X":
			L6[c]=L6[c+4]=L6[c+8]=L6[c+12]=L6[c+16]=L6[c+20]="x"
			z+=1
			break	
		else:
			z+=0
			continue
	for j in range(0,3):
		c=j*4+2
		if L1[c]==L1[c+4]==L1[c+8]==L1[c+12]==L1[c+16]=="X":
			L1[c]=L1[c+4]=L1[c+8]=L1[c+12]=L1[c+16]="x"
			z+=1
			break
		elif L2[c]==L2[c+4]==L2[c+8]==L2[c+12]==L2[c+16]=="X":
			L2[c]=L2[c+4]=L2[c+8]=L2[c+12]=L2[c+16]="x"
			z+=1
			break	
		elif L3[c]==L3[c+4]==L3[c+8]==L3[c+12]==L3[c+16]=="X":
			L3[c]=L3[c+4]=L3[c+8]=L3[c+12]=L3[c+16]="x"
			z+=1
			break	
		elif L4[c]==L4[c+4]==L4[c+8]==L4[c+12]==L4[c+16]=="X":
			L4[c]=L4[c+4]=L4[c+8]=L4[c+12]=L4[c+16]="x"
			z+=1
			break	
		elif L5[c]==L5[c+4]==L5[c+8]==L5[c+12]==L5[c+16]=="X":
			L5[c]=L5[c+4]=L5[c+8]=L5[c+12]=L5[c+16]="x"
			z+=1
			break	
		elif L6[c]==L6[c+4]==L6[c+8]==L6[c+12]==L6[c+16]=="X":
			L6[c]=L6[c+4]=L6[c+8]=L6[c+12]=L6[c+16]="x"
			z+=1
			break	
		else:
			z+=0
			continue
	for j in range(0,4):
		c=j*4+2
		if L1[c]==L1[c+4]==L1[c+8]==L1[c+12]=="X":
			L1[c]=L1[c+4]=L1[c+8]=L1[c+12]="x"
			z+=1
			break				
		elif L2[c]==L2[c+4]==L2[c+8]==L2[c+12]=="X":
			L2[c]=L2[c+4]=L2[c+8]=L2[c+12]="x"
			z+=1
			break
		elif L3[c]==L3[c+4]==L3[c+8]==L3[c+12]=="X":
			L3[c]=L3[c+4]=L3[c+8]=L3[c+12]="x"
			z+=1
			break
		elif L4[c]==L4[c+4]==L4[c+8]==L4[c+12]=="X":
			L4[c]=L4[c+4]=L4[c+8]=L4[c+12]="x"
			z+=1
			break
		elif L5[c]==L5[c+4]==L5[c+8]==L5[c+12]=="X":
			L5[c]=L5[c+4]=L5[c+8]=L5[c+12]="x"
			z+=1
			break
		elif L6[c]==L6[c+4]==L6[c+8]==L6[c+12]=="X":
			L6[c]=L6[c+4]=L6[c+8]=L6[c+12]="x"
			z+=1
			break
		else:
			z+=0
			continue
	for m in range(0,2):
		c=m*4+2
		if L1[c]==L2[c+4]==L3[c+8]==L4[c+12]==L5[c+16]==L6[c+20]=="X":
			L1[c]=L2[c+4]=L3[c+8]=L4[c+12]=L5[c+16]=L6[c+20]="x"
			z+=1
			break				
		elif L6[c]==L5[c+4]==L4[c+8]==L3[c+12]==L2[c+16]==L1[c+20]=="X":
			L6[c]=L5[c+4]=L4[c+8]=L3[c+12]=L2[c+16]=L1[c+20]="x"
			z+=1
			break
		else:
			z+=0
			continue
	for m in range(0,3):
		c=m*4+2
		if L1[c]==L2[c+4]==L3[c+8]==L4[c+12]==L5[c+16]=="X":
			L1[c]=L2[c+4]=L3[c+8]=L4[c+12]=L5[c+16]="x"
			z+=1
			break				
		elif L2[c]==L3[c+4]==L4[c+8]==L5[c+12]==L6[c+16]=="X":
			L2[c]=L3[c+4]=L4[c+8]=L5[c+12]=L6[c+16]="x"
			z+=1
			break
		elif L6[c]==L5[c+4]==L4[c+8]==L3[c+12]==L2[c+16]=="X":
			L6[c]=L5[c+4]=L4[c+8]=L3[c+12]=L2[c+16]="x"
			z+=1
			break
		elif L5[c]==L4[c+4]==L3[c+8]==L2[c+12]==L1[c+16]=="X":
			L5[c]=L4[c+4]=L3[c+8]=L2[c+12]=L1[c+16]="x"
			z+=1
			break
		else:
			z+=0
			continue
	for m in range(0,4):
		c=m*4+2
		if L1[c]==L2[c+4]==L3[c+8]==L4[c+12]=="X":
			L1[c]=L2[c+4]=L3[c+8]=L4[c+12]="x"
			z+=1
			break				
		elif L2[c]==L3[c+4]==L4[c+8]==L5[c+12]=="X":
			L2[c]=L3[c+4]=L4[c+8]=L5[c+12]="x"
			z+=1
			break
		elif L3[c]==L4[c+4]==L5[c+8]==L6[c+12]=="X":
			L3[c]=L4[c+4]=L5[c+8]=L6[c+12]="x"
			z+=1
			break
		elif L4[c]==L3[c+4]==L2[c+8]==L1[c+12]=="X":
			L4[c]=L3[c+4]=L2[c+8]=L1[c+12]="x"
			z+=1
			break
		elif L5[c]==L4[c+4]==L3[c+8]==L2[c+12]=="X":
			L5[c]=L4[c+4]=L3[c+8]=L2[c+12]="x"
			z+=1
			break
		elif L6[c]==L5[c+4]==L4[c+8]==L3[c+12]=="X":
			L6[c]=L5[c+4]=L4[c+8]=L3[c+12]="x"
			z+=1
			break
		else:
			z+=0
			continue
	for n in range(0,7):
		c=n*4+2
		if L1[c]==L2[c]==L3[c]==L4[c]=="X":
			L1[c]=L2[c]=L3[c]=L4[c]="x"
			z+=1
			break
		elif L2[c]==L3[c]==L4[c]==L5[c]=="X":
			L2[c]=L3[c]=L4[c]=L5[c]="x"
			z+=1
			break
		elif L3[c]==L4[c]==L5[c]==L6[c]=="X":
			L3[c]=L4[c]=L5[c]=L6[c]="x"
			z+=1
			break	
		else:
			z+=0
			continue
	if z!=0:
		print(a)
		print("".join(L6))
		print(a)
		print("".join(L5))
		print(a)
		print("".join(L4))
		print(a)
		print("".join(L3))
		print(a)
		print("".join(L2))
		print(a)
		print("".join(L1))
		print(a)
		print("  0   1   2   3   4   5   6")
		print("Winner: X")
		break
	#換玩家O
	while i==2:
		O=input("Player O >>")
		#確認是否在範圍內
		if not O.isdigit():
			print("Invalid input, try again [0-6].")
			i=2
		elif int(O)>6 or int(O)<0:
			print("Out of range, try again [0-6].")
			i=2
		else:
			c=int(O)*4+2
			if L1[c]=="X" or L1[c]=="O":
				if L2[c]=="X" or L2[c]=="O":
					if L3[c]=="X" or L3[c]=="O":
						if L4[c]=="X" or L4[c]=="O":
							if L5[c]=="X" or L5[c]=="O":
								if L6[c]=="X" or L6[c]=="O":
									print("This column is full. Try another column.")
									i=2
								else:	
									L6[c]="O"
									i=1
							else:	
								L5[c]="O"
								i=1
						else:	
							L4[c]="O"
							i=1
					else:	
						L3[c]="O"
						i=1
				else:	
					L2[c]="O"
					i=1
			else:	
				L1[c]="O"
				i=1
		#合理範圍內即印出結果
		if	i==1:
			print(a)
			print("".join(L6))
			print(a)
			print("".join(L5))
			print(a)
			print("".join(L4))
			print(a)
			print("".join(L3))
			print(a)
			print("".join(L2))
			print(a)
			print("".join(L1))
			print(a)
			print("  0   1   2   3   4   5   6")
	#確認是否O獲勝
	for j in range(0,1):
		z=0
		c=j*4+2
		if L1[c]==L1[c+4]==L1[c+8]==L1[c+12]==L1[c+16]==L1[c+20]==L1[c+24]=="O":
			L1[c]=L1[c+4]=L1[c+8]=L1[c+12]=L1[c+16]=L1[c+20]=L1[c+24]="o"
			z+=1
			break				
		elif L2[c]==L2[c+4]==L2[c+8]==L2[c+12]==L2[c+16]==L2[c+20]==L2[c+24]=="O":
			L2[c]=L2[c+4]=L2[c+8]=L2[c+12]=L2[c+16]=L2[c+20]=L2[c+24]="o"
			z+=1
			break	
		elif L3[c]==L3[c+4]==L3[c+8]==L3[c+12]==L3[c+16]==L3[c+20]==L3[c+24]=="O":
			L3[c]=L3[c+4]=L3[c+8]=L3[c+12]=L3[c+16]=L3[c+20]=L3[c+24]="o"
			z+=1
			break	
		elif L4[c]==L4[c+4]==L4[c+8]==L4[c+12]==L4[c+16]==L4[c+20]==L4[c+24]=="O":
			L4[c]=L4[c+4]=L4[c+8]=L4[c+12]=L4[c+16]=L4[c+20]=L4[c+24]="o"
			z+=1
			break	
		elif L5[c]==L5[c+4]==L5[c+8]==L5[c+12]==L5[c+16]==L5[c+20]==L5[c+24]=="O":
			L5[c]=L5[c+4]=L5[c+8]=L5[c+12]=L5[c+16]=L5[c+20]=L5[c+24]="o"
			z+=1
			break	
		elif L6[c]==L6[c+4]==L6[c+8]==L6[c+12]==L6[c+16]==L6[c+20]==L6[c+24]=="O":
			L6[c]=L6[c+4]=L6[c+8]=L6[c+12]=L6[c+16]=L6[c+20]=L6[c+24]="o"
			z+=1
			break	
		else:
			z+=0
			continue
	for j in range(0,2):
		c=j*4+2
		if L1[c]==L1[c+4]==L1[c+8]==L1[c+12]==L1[c+16]==L1[c+20]=="O":
			L1[c]=L1[c+4]=L1[c+8]=L1[c+12]=L1[c+16]=L1[c+20]="o"
			z+=1
			break				
		elif L2[c]==L2[c+4]==L2[c+8]==L2[c+12]==L2[c+16]==L2[c+20]=="O":
			L2[c]=L2[c+4]=L2[c+8]=L2[c+12]=L2[c+16]=L2[c+20]="o"
			z+=1
			break	
		elif L3[c]==L3[c+4]==L3[c+8]==L3[c+12]==L3[c+16]==L3[c+20]=="O":
			L3[c]=L3[c+4]=L3[c+8]=L3[c+12]=L3[c+16]=L3[c+20]="o"
			z+=1
			break	
		elif L4[c]==L4[c+4]==L4[c+8]==L4[c+12]==L4[c+16]==L4[c+20]=="O":
			L4[c]=L4[c+4]=L4[c+8]=L4[c+12]=L4[c+16]=L4[c+20]="o"
			z+=1
			break	
		elif L5[c]==L5[c+4]==L5[c+8]==L5[c+12]==L5[c+16]==L5[c+20]=="O":
			L5[c]=L5[c+4]=L5[c+8]=L5[c+12]=L5[c+16]=L5[c+20]="o"
			z+=1
			break	
		elif L6[c]==L6[c+4]==L6[c+8]==L6[c+12]==L6[c+16]==L6[c+20]=="O":
			L6[c]=L6[c+4]=L6[c+8]=L6[c+12]=L6[c+16]=L6[c+20]="o"
			z+=1
			break	
		else:
			z+=0
			continue
	for j in range(0,3):
		c=j*4+2
		if L1[c]==L1[c+4]==L1[c+8]==L1[c+12]==L1[c+16]=="O":
			L1[c]=L1[c+4]=L1[c+8]=L1[c+12]=L1[c+16]="o"
			z+=1
			break				
		elif L2[c]==L2[c+4]==L2[c+8]==L2[c+12]==L2[c+16]=="O":
			L2[c]=L2[c+4]=L2[c+8]=L2[c+12]=L2[c+16]="o"
			z+=1
			break	
		elif L3[c]==L3[c+4]==L3[c+8]==L3[c+12]==L3[c+16]=="O":
			L3[c]=L3[c+4]=L3[c+8]=L3[c+12]=L3[c+16]="o"
			z+=1
			break	
		elif L4[c]==L4[c+4]==L4[c+8]==L4[c+12]==L4[c+16]=="O":
			L4[c]=L4[c+4]=L4[c+8]=L4[c+12]=L4[c+16]="o"
			z+=1
			break	
		elif L5[c]==L5[c+4]==L5[c+8]==L5[c+12]==L5[c+16]=="O":
			L5[c]=L5[c+4]=L5[c+8]=L5[c+12]=L5[c+16]="o"
			z+=1
			break	
		elif L6[c]==L6[c+4]==L6[c+8]==L6[c+12]==L6[c+16]=="O":
			L6[c]=L6[c+4]=L6[c+8]=L6[c+12]=L6[c+16]="o"
			z+=1
			break	
		else:
			z+=0
			continue
	for j in range(0,4):
		c=j*4+2
		if L1[c]==L1[c+4]==L1[c+8]==L1[c+12]=="O":
			L1[c]=L1[c+4]=L1[c+8]=L1[c+12]="o"
			z+=1
			break				
		elif L2[c]==L2[c+4]==L2[c+8]==L2[c+12]=="O":
			L2[c]=L2[c+4]=L2[c+8]=L2[c+12]="o"
			z+=1
			break
		elif L3[c]==L3[c+4]==L3[c+8]==L3[c+12]=="O":
			L3[c]=L3[c+4]=L3[c+8]=L3[c+12]="o"
			z+=1
			break
		elif L4[c]==L4[c+4]==L4[c+8]==L4[c+12]=="O":
			L4[c]=L4[c+4]=L4[c+8]=L4[c+12]="o"
			z+=1
			break
		elif L5[c]==L5[c+4]==L5[c+8]==L5[c+12]=="O":
			L5[c]=L5[c+4]=L5[c+8]=L5[c+12]="o"
			z+=1
			break
		elif L6[c]==L6[c+4]==L6[c+8]==L6[c+12]=="O":
			L6[c]=L6[c+4]=L6[c+8]=L6[c+12]="o"
			z+=1
			break
		else:
			z+=0
			continue
	for m in range(0,2):
		c=m*4+2
		if L1[c]==L2[c+4]==L3[c+8]==L4[c+12]==L5[c+16]==L6[c+20]=="O":
			L1[c]=L2[c+4]=L3[c+8]=L4[c+12]=L5[c+16]=L6[c+20]="o"
			z+=1
			break				
		elif L6[c]==L5[c+4]==L4[c+8]==L3[c+12]==L2[c+16]==L1[c+20]=="O":
			L6[c]=L5[c+4]=L4[c+8]=L3[c+12]=L2[c+16]=L1[c+20]="o"
			z+=1
			break
		else:
			z+=0
			continue
	for m in range(0,3):
		c=m*4+2
		if L1[c]==L2[c+4]==L3[c+8]==L4[c+12]==L5[c+16]=="O":
			L1[c]=L2[c+4]=L3[c+8]=L4[c+12]=L5[c+16]="o"
			z+=1
			break				
		elif L2[c]==L3[c+4]==L4[c+8]==L5[c+12]==L6[c+16]=="O":
			L2[c]=L3[c+4]=L4[c+8]=L5[c+12]=L6[c+16]="o"
			z+=1
			break
		elif L6[c]==L5[c+4]==L4[c+8]==L3[c+12]==L2[c+16]=="O":
			L6[c]=L5[c+4]=L4[c+8]=L3[c+12]=L2[c+16]="o"
			z+=1
			break
		elif L5[c]==L4[c+4]==L3[c+8]==L2[c+12]==L1[c+16]=="O":
			L5[c]=L4[c+4]=L3[c+8]=L2[c+12]=L1[c+16]="o"
			z+=1
			break
		else:
			z+=0
			continue
	for m in range(0,4):
		c=m*4+2
		if L1[c]==L2[c+4]==L3[c+8]==L4[c+12]=="O":
			L1[c]=L2[c+4]=L3[c+8]=L4[c+12]="o"
			z+=1
			break				
		elif L2[c]==L3[c+4]==L4[c+8]==L5[c+12]=="O":
			L2[c]=L3[c+4]=L4[c+8]=L5[c+12]="o"
			z+=1
			break
		elif L3[c]==L4[c+4]==L5[c+8]==L6[c+12]=="O":
			L3[c]=L4[c+4]=L5[c+8]=L6[c+12]="o"
			z+=1
			break
		elif L4[c]==L3[c+4]==L2[c+8]==L1[c+12]=="O":
			L4[c]=L3[c+4]=L2[c+8]=L1[c+12]="o"
			z+=1
			break
		elif L5[c]==L4[c+4]==L3[c+8]==L2[c+12]=="O":
			L5[c]=L4[c+4]=L3[c+8]=L2[c+12]="o"
			z+=1
			break
		elif L6[c]==L5[c+4]==L4[c+8]==L3[c+12]=="O":
			L6[c]=L5[c+4]=L4[c+8]=L3[c+12]="o"
			z+=1
			break
		else:
			z+=0
			continue
	for n in range(0,7):
		c=n*4+2
		if L1[c]==L2[c]==L3[c]==L4[c]=="O":
			L1[c]=L2[c]=L3[c]=L4[c]="o"
			z+=1
			break
		elif L2[c]==L3[c]==L4[c]==L5[c]=="O":
			L2[c]=L3[c]=L4[c]=L5[c]="o"
			z+=1
			break
		elif L3[c]==L4[c]==L5[c]==L6[c]=="O":
			L3[c]=L4[c]=L5[c]=L6[c]="o"
			z+=1
			break	
		else:
			z+=0
			continue
	if z!=0:
		print(a)
		print("".join(L6))
		print(a)
		print("".join(L5))
		print(a)
		print("".join(L4))
		print(a)
		print("".join(L3))
		print(a)
		print("".join(L2))
		print(a)
		print("".join(L1))
		print(a)
		print("  0   1   2   3   4   5   6")
		print("Winner: O")
		break
	#確認是否平手
	s=0
	for k in range(0,7):
		c=k*4+2
		if L1[c]=="X" or L1[c]=="O":
			if L2[c]=="X" or L2[c]=="O":
				if L3[c]=="X" or L3[c]=="O":
					if L4[c]=="X" or L4[c]=="O":
						if L5[c]=="X" or L5[c]=="O":
							if L6[c]=="X" or L6[c]=="O":
								s+=1
								continue
							else:
								break
						else:
							break
					else:
						break
				else:
					break
			else:
				break
		else:
			break
	if s==7:
		print("Draw")
		break