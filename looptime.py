def function(n):
    for i in range(0, n + 1):  # Loop 1
        print("First Loop")

    j = 1
    while j <= n + 1:  # Loop 2
        print("Second Loop ", j)
        j = j * 2

    for i in range(0, 100):  # Loop 3
        print("Third loop")
