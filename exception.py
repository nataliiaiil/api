try:
    a = int(input("Input first value: "))
    b = int(input("Input the second value: "))
    result2 = a + b
    print(result2)
    result = int(a / b)
except ZeroDivisionError:
    result = 0
    print("The second value can't be 0")
except ValueError as err:
    result = 0
    print("All values should be numbers")
print("Result is " + str(result))


#print(result2)s
#1ZeroDivisionError
#ValueError