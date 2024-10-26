def multiply_once(a, b):
    return a * b

def multiply_n_iterations(a, b):
    result = 0
    for _ in range(abs(b)):  
        result += a
    if b < 0:
        result = -result  
    return result

num1 = int(input("Enter 'a' for a*b: "))
num2 = int(input("Enter 'b' for a*b: "))

result_once = multiply_once(num1, num2)
result_n_iterations = multiply_n_iterations(num1, num2)

print("1 iteration: ", result_once)
print("N iteration: ", result_n_iterations)
