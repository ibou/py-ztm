def test(n):
    for i in range(n):
        print(f"fib {i} = {fib(i)}")


def fib(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        print(f"fib n-1 {number-1}",)
        print(f"fib n-2 {number-2}", )
        result1 = fib(number - 1) 
        result2 = fib(number - 2)
        result = result1 + result2
        print(f"==> {number} result1  {result1} et result2 {result2} = {result}")
        return result

def main():

    x = int(input('number of fib: '))
    result = fib(x)
    print(result)


def fib2(number):
    n1 = 0
    n2 = 1
    for i in range(number+1):
        print( n1)
        temp = n1
        n1 = n2
        n2 = temp + n2

def loopFib():
    x = int(input('number of fib: '))
    for i in fib2(x):
        print(i) 


# if __name__ == "__main__":
#     # main()
#     # loopFib()
#     fib2(5)
