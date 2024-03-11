number = int(input("Input positive number : "))

if number < 2:
    print(f"{number} is not prime number")
else:
    count = 0

    for i in range(2, number):  # !
        if number % i == 0:
            count = count + 1

    if count == 0:  # !
        print(f"{number} is prime number")
    else:
        print(f"{number} is not prime number")