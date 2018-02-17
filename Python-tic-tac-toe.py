def logic(i,p):
	  dict[i]=p
	  if(d[0]==d[1]==d[2]):                    #d[i]==d[i+1]==d[i+2]
		  return true
		  board(dict)
		  print d[0], "wins"
	  elif(d[0]==d[3]==d[6]):                  #d[i]==d[i+3]==d[i+6]
		  return true
		  board(dict)
		  print d[0], "wins"
	  elif(d[0]==d[4]==d[8]):                  #d[i]==d[i+4]==d[i++8]
		  return true
		  board(dict)
		  print d[0] ,"wins"
	  elif(d[1]==d[4]==d[7]):
		  return true
		  board(dict)
		  print d[1] ,"wins"
	  elif(d[2]==d[5]==d[8]):
		  return true
		  board(dict)
		  print d[2] ,"wins"
	  elif(d[2]==d[4]==d[6]):                 #d[i]==d[i+2]==d[i+4]
		  return true
		  board(dict)
		  print d[2] ,"wins"
	  elif(d[3]==d[4]==d[5]):
		  return true
		  board(dict)
		  print d[3] ,"wins"
	  elif(d[6]==d[7]==d[8]):
		  return true
		  board(dict)
		  print d[6] ,"wins"
	  elif(counter==8):
		  return true
		  print "draw"

dict={0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:''}
counter=0;
p='o'
global i
while(logic(i,p)!=true):
	raw_input(i)
	if(counter%2==0):
		p='o'
	else:
		p='q'
	counter=counter=+1
	logic(i,p)
	board(dict)


def board(dict):
 print("|{}|{}|{}|").format(dict[0],dict[1],dict[2])
 print("|{}|{}|{}|").format(dict[3],dict[4],dict[5])
 print("|{}|{}|{}|").format(dict[6],dict[7],dict[8])
