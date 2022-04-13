b=1 
row=5
for i in range (row,0,-1):
    for j in range (1,i+1):
        print (b,end=" ")
    b+=1
    print("\r")    
