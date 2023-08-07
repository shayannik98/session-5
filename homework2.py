import math
# b**2-4ac
def moadele_2_majhul():
    print("welcome: ")
    while True:
           userinput=("input your numbers for moadele")
           a=int(input("enter num a: "))
           b=int(input("enter num b:"))
           c=int(input("enter num c: "))
           delta = b**2-4*a*c
           #print (x)
           if delta > 0:
               x1 = (-b +math.sqrt(delta)) / (2*a)
               x2 = (-b -math.sqrt(delta)) / (2*a)
               print ("X1 =",x1,"  X2 =",x2)
           elif delta == 0 :
                x = -b / (2*a)
                print ("X =",x) 
           else :
                print("not valid")         


moadele_2_majhul()

