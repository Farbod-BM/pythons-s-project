firstNum = int(input(" enter the first number : "))
secondNum = int(input(" enter the second number : "))
thirdNum = int(input(" enter the third number : "))

# first we should check if this three sides can make a triangle ,then we should if this triangle is right or not
# for any triangle The sum of the lengths of any two sides is greater than the length of the third
# we can recognize right triangle by Pythagorean theorem -> Pythagorean theorem : a^2 + b^2 - c^2 == 0


if firstNum + secondNum < thirdNum or firstNum + thirdNum < secondNum or secondNum + thirdNum < firstNum:
    print("error : not a triangle")
else:
    result1 = ((firstNum ** 2) + (secondNum ** 2)) - (thirdNum ** 2)
    result2 = ((firstNum ** 2) + (thirdNum ** 2)) - (secondNum ** 2)
    result3 = ((thirdNum ** 2) + (secondNum ** 2)) - (firstNum ** 2)

    if result1 == 0 or result2 == 0 or result3 == 0:
        print("Right")
    else:
        print("Not right")