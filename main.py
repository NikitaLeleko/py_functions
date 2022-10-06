def square_digits(number: int):
    result = ""
    number = str(number)
    for i in range(len(number)):
        result += str(int(number[i])**2)
    result = int(result)
    print(result)
square_digits(92)