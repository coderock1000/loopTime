def myfunction(n):
    if n <= 0:  
        return
    for i in range(0, int(n) + 1):  
        print("Codingal")
    myfunction(n // 2)  
    myfunction(n // 3)  

myfunction(4)

for i in range(0, 5):
    print(i)