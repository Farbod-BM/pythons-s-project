v = 1

while v < 10000:
    order = len(str(v))
    result = 0
    temp = v
    while temp > 0:
        digit = temp % 10
        result += digit ** order
        temp //= 10
    if v == result:
        print(v)
    v = v + 1