import random
import time
#製作棋盤
def table(space):
	print("   a   b   c   d   e   f   g   h   i")
	print(" +" + "---+" * 9)
	for i in range(1,10):
		print(str(i)+"|",end="")
		print(space[i-1])
		print(" +" + "---+" * 9)
	return " "
#判斷八方位的地雷
def mineplace(i,j,grid1):
	total=0
	if grid1[i][j]!="X":
		test=[(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
		for k in test:
			x,y=k
			if 0<=x<len(grid1) and 0<=y<len(grid1[i]):
				if grid1[x][y]=="X":
					total+=1
				else:
					continue
			else:
				continue
	else:
		total="X"
	return str(total)
#給提示
def help():
	print(table(space))
	print("Enter the column followed by the row (ex: a5). To add or remove a flag,")
	print("add 'f' to the cell (ex: a5f).Type 'help' to show this message again")
	print()
#確認相鄰位置是否一樣為0
def check(i,j,t1):
	if t1[i][j]=='0':
		test1=[(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
		for k in test1:
			x,y=k
			if 0<=x<len(t1) and 0<=y<len(t1[i]):
				if t1[x][y]=="0":
					space[x]=space[x][:y*4+1]+"0"+space[x][y*4+2:]
					t1[i]=t1[i][:j]+["*"]+t1[i][j+1:]
					check(x,y,t1)
				elif t1[x][y]!="*" and t1[x][y]!="0":
					space[x]=space[x][:y*4+1]+str(t1[x][y])+space[x][y*4+2:]
			else:
				continue
	return " "
#重置
def resetup(t1):
	for s in range(0,9):
		for t in range(0,9):
			if t1[s][t]=="*":
				t1[s][t]="0"
#設置炸彈
def setup(mines):
	while len(mines)<10:
		mine=random.randint(0,80)
		if mine not in mines:
			mines.append(mine)
	grid=[]
	for i in range(0,81):
		if i in mines:
			grid.append("X")
		else:
			grid.append(".")
	grid1=[]
	i=0
	while i<81:
		row=grid[i:i+9]
		grid1.append(row)
		i+=9
	t=[]
	for i in range(0,len(grid1)):
		for j in range(0,len(grid1[i])):
			a=mineplace(i,j,grid1)
			t.append(a)
	i=0
	while i<81:
		r=t[i:i+9]
		t1.append(r)
		i+=9
#遊戲結果
def result():
	for i in range(0,9):
		for j in range(0,9):
			space[i]=space[i][:j*4+1]+str(t1[i][j])+space[i][j*4+2:]
	print(table(space))
#開始遊戲
while 1:
	start_time=time.time()
	space=[]
	for i in range(0,9):
		space1="   |" *9
		space.append(space1)
	mines=[]
	t1=[]
	help()
	setup(mines)
	num_mines=10
	cell=str(input("Enter the cell (%d mines left):"%(num_mines)))
	#確定第一個空格為0
	while 1:
		if len(cell)==2:
			i,j=int(cell[1])-1,ord(cell[0])-97
			if t1[i][j]=='0':
				break
			else:
				mines=[]
				t1=[]
				setup(mines)
		elif cell=="help":
			help()
			cell=str(input("Enter the cell (%d mines left):"%(num_mines)))
	while 1:
		#確定踩此格
		if len(cell)==2:
			#判斷是否範圍內
			if 0<=int(cell[1])-1<9 and 0<=ord(cell[0])-97<9:
				i,j=int(cell[1])-1,ord(cell[0])-97
				#判斷格子是否合理
				if space[i][j*4+1]==" ":
					#踩到地雷
					if t1[i][j]=="X":
						print()
						print("Game Over")
						print()
						result()
						break
					#顯示格子資訊並判斷是否獲勝
					else:
						space[i]=space[i][:j*4+1]+str(t1[i][j])+space[i][j*4+2:]
						check(i,j,t1)
						resetup(t1)
						a=0
						for m in range(0,9):
							for n in range(0,9):
								if space[m][n*4+1]==" " or space[m][n*4+1]=="F":
									a+=1
						if a==10:
							end_time=time.time()
							duration=end_time-start_time
							print()
							print("You Win. It took you %d minutes and %d seconds."%(duration//60,duration%60))
							print()
							result()
							break
						else:
							print(table(space))
				elif space[i][j*4+1]!=" " and space[i][j*4+1]!="F":
					print(table(space))
					print("That cell is already shown")
					print()
				elif space[i][j*4+1]=="F":
					print(table(space))
					print("There is a flag there")
					print()
			else:
				print(table(space))
				print("Invalid cell. Enter the column followed by the row (ex: a5). To add or")
				print("remove a flag, add 'f' to the cell (ex: a5f).")
				print()
		#設置標記
		elif len(cell)==3:
			#判斷是否範圍內
			if 0<=int(cell[1])-1<9 and 0<=ord(cell[0])-97<9:
				i,j=int(cell[1])-1,ord(cell[0])-97
				#判斷是否能標記並判斷是否獲勝
				if space[i][j*4+1]==" ":
					space[i]=space[i][:j*4+1]+"F"+space[i][j*4+2:]
					a=0
					for m in range(0,9):
						for n in range(0,9):
							if space[m][n*4+1]==" " or space[m][n*4+1]=="F":
								a+=1
					if a==10:
						end_time=time.time()
						duration=end_time-start_time
						print("You Win. It took you %d minutes and %d seconds."%(duration//60,duration%60))
						print()
						result()
						break
					else:
						print(table(space))
						num_mines-=1
				elif space[i][j*4+1]=="F":
					space[i]=space[i][:j*4+1]+" "+space[i][j*4+2:]
					print(table(space))
					num_mines+=1
				else:
					print(table(space))
					print("Cannot put a flag there")
					print()
			else:
				print(table(space))
				print("Invalid cell. Enter the column followed by the row (ex: a5). To add or")
				print("remove a flag, add 'f' to the cell (ex: a5f).")
				print()
		#請求幫助
		elif cell=="help":
			help()
		#繼續遊戲
		cell=str(input("Enter the cell (%d mines left):"%(num_mines)))
	#詢問再玩一次
	ans=str(input("Play again? (y/n):"))
	if ans=='y':
		continue
	else:
		break