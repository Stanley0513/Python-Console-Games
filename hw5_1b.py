import random
rank=['ACE','2','3','4','5','6','7','8','9','10','JACK','QUEEN','KING']
suit=['SPADE','HEART','DIAMOND','CLUB']
#創建隨機排組
def create():
	global deck
	deck=[]
	for i in range(0,13):
		for j in range(0,4):
			deck.append(rank[i]+"-"+suit[j])
	random.shuffle(deck)
#抽取玩家排組
def play():
	global card
	card=[]
	for k in range(0,2):
		card+=[deck[0]]
		deck.remove(deck[0])
#決定獲勝者
def winner(value,dvalue):
	if value>dvalue and value<=21 and dvalue<=21:
		print("*** You beat the dealer! ***")
	elif value<dvalue and value<=21 and dvalue<=21:
		print("*** Dealer wins! ***")
	elif value==dvalue and value<=21 and dvalue<=21:
		print("*** You tied the dealer, nobody wins. ***")
	elif dvalue>21 and value<=21:
		print("*** You beat the dealer! ***")
	elif value>21:
		print("*** Dealer wins! ***")

while 1:
	create()
	play()
	while 1:
		#判斷玩家排組數值
		value=0
		a=0
		for k in card:
			if ord(k[0])==65:
				a+=1
			elif ord(k[0])==74 or ord(k[0])==75 or ord(k[0])==81:
				value+=10
			elif int(k[0])==1 and int(k[1])==0:
				value+=10
			else:
				value+=int(k[0])
		for k in range(0,a):
			if value<=10:
				value+=11
			else:
				value+=1
	#顯示判斷結果
		if value<21:
			print("Your current value is",value)
			print("with the hand:",",".join(card))
		elif value==21:
			print("Your current value is Blackjack! (21)")
			print("with the hand:",",".join(card))
		else:
			print("Your current value is Bust! (>21)")
			print("with the hand:",",".join(card))
			print()
			break
	#詢問玩家選擇
		print()
		ans=int(input("Hit or stay? (Hit = 1, Stay = 0):"))
		if ans==1:
			print("You draw",deck[0])
			print()
			card+=[deck[0]]
			deck.remove(deck[0])
		else:
			print()
			break
	#創建電腦排組
	dcard=[]
	for k in range(0,2):
		dcard+=[deck[0]]
		deck.remove(deck[0])
	#判斷電腦排組數值
	while 1:
		dvalue=0
		da=0
		for k in dcard:
			if ord(k[0])==65:
				da+=1
			elif ord(k[0])==74 or ord(k[0])==75 or ord(k[0])==81:
				dvalue+=10
			elif int(k[0])==1 and int(k[1])==0:
				dvalue+=10
			else:
				dvalue+=int(k[0])
		for k in range(0,da):
			if dvalue<=10:
				dvalue+=11
			else:
				dvalue+=1
	#顯示並完成最後判斷結果
		if dvalue<17:
			print("Dealer's current value is",dvalue)
			print("with the hand:",",".join(dcard))
			print()
			print("Dealer draws",deck[0])
			print()
			dcard+=[deck[0]]
			deck.remove(deck[0])
		elif dvalue>=17 and dvalue<21:
			print("Dealer's current value is",dvalue)
			print("with the hand:",",".join(dcard))
			break
		elif dvalue==21:
			print("Dealer's current value is Blackjack! (21)")
			print("with the hand:",",".join(dcard))
			break
		else:
			print("Dealer's current value is Bust! (>21)")
			print("with the hand:",",".join(dcard))
			break
	print()
	winner(value,dvalue)
	#詢問是否繼續玩
	print()
	ask=str(input("Want to play again? (y/n):"))
	if ask==str("y"):
		print()
		print("----------------------------------------")
		print()
		continue
	else:
		break