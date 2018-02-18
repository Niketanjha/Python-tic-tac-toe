def logic(i,p):
	  if(d[0]==d[1]==d[2]==p):                    #d[i]==d[i+1]==d[i+2]
		  return True
		  board(d)
		  print(d[0], "wins")
	  elif(d[0]==d[3]==d[6]==p):                  #d[i]==d[i+3]==d[i+6]
		  return True
		  board(d)
		  print(d[0], "wins")
	  elif(d[0]==d[4]==d[8]==p):                  #d[i]==d[i+4]==d[i++8]
		  return True
		  board(d)
		  print(d[0] ,"wins")
	  elif(d[1]==d[4]==d[7]==p):
		  return True
		  board(d)
		  print(d[1] ,"wins")
	  elif(d[2]==d[5]==d[8]==p):
		  return True
		  board(d)
		  print(d[2] ,"wins")
	  elif(d[2]==d[4]==d[6]==p):                 #d[i]==d[i+2]==d[i+4]
		  return True
		  board(d)
		  print(d[2] ,"wins")
	  elif(d[3]==d[4]==d[5]==p):
		  return True
		  board(d)
		  print(d[3] ,"wins")
	  elif(d[6]==d[7]==d[8]==p):
		  return True
		  board(d)
		  print(d[6] ,"wins")
	  elif(counter==9):
		  return True
		  print "draw"
	  else:
		  return False

def board(d):
 print("|{}|{}|{}|").format(d[0],d[1],d[2])
 print("|{}|{}|{}|").format(d[3],d[4],d[5])
 print("|{}|{}|{}|").format(d[6],d[7],d[8])

d={0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:''}
p='o'
i=int(raw_input("Enter choice"))
d[i]=p
board(d)
counter=1;
while(logic(i,p)!=True):
	i=int(raw_input("Enter your move"))
	if(0>i<9):
		print("wrong value ")
		exit	
	if(counter%2==0):
		p='o'
	else:
		p='x'
	d[i]=p
	print(logic(i,p))
	counter=counter+1
	print(counter)
	logic(i,p)
	board(d)
