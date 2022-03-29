import math

x = math.radians(float(input("enter a number ")))

def sin(x: float, Z: int = 10):
    result = 0
    for m in range(Z):

     result += ((-1) ** m * x ** (2 * m + 1)) / math.factorial(2 * m + 1)

    return result

if __name__ == '__main__':
    print(sin(x))