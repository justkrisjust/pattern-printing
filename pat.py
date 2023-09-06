"""so basically patttern printing should be done
and the stars should be print form
1 to given n number here n is input
if true ascending order if false reverse should be
print hmmm wt to do know ?

if 1 straight way printing will be done 
if 0  reverse way printing will be done"""





print("enter n")
n=int(input())
a= "*"
b = bool(int(input("type 1 or 0 \n")))

if (b==True):
  for i in range (1,n+1):
    for j in range(1,i+1):
      print(a,end="  ")
    print()
else:
  for i in range (n,0,-1):
    for j in range(1,i+1):
      print(a,end="  ")
    print()

