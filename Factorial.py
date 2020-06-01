n = int(input("Please enter a number for Factorial : "))

def fact():
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

Answer = fact()

print("Factorial of {} is {}".format(n, Answer))

print(" #################### using recursion ######################### ")

x = int(input("Please enter a number for Factorial : "))


def fact1(x):
    if x == 0:
        return 1
    return x * fact1(x - 1)

result = fact1(x)

print(result)
