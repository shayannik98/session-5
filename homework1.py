ss="#*"
ws="*#"
def shatrang(row , col):
    for i in range(row):
           for j in range(col):
               if i %2==0:
                    print(ss , end=" ")
               else:
                    print(ws ,end=" ")  
           print()                

print("welcome ")
rows = int(input("The number of rows: "))
columns = int(input("The number of columns: "))
print()

shatrang(rows, columns)

        
