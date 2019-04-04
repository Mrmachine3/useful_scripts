numbers = list(range(1, 10))
print numbers

for number in numbers:
    if number == 1:
        print(str(numbers[0]) + "st")
    elif number == 2:
        print(str(numbers[1]) + "nd")
    elif number == 3:
        print(str(numbers[2]) + "rd")
    else:
        print(str(number) + "th")
