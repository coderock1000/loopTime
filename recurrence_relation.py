def myfunction1(n):
    if (n > 0):   
        return
    for i in range(0, n + 1):  
        print("Codingal")
    myfunction1(n / 2)  
    myfunction1(n / 3)  

myfunction1(4)