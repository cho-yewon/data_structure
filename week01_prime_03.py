number = int(input("Input positive number : "))

if number < 2:
    print(f"{number} is not prime number")
else:
    count = 0

    for i in range(2, number):  # !
        if number % i == 0:
            count = count + 1
            break
        print(i, end=' ')

    if count == 0:  # !
        print(f"\n{number} is prime number")
    else:
        print(f"\n{number} is not prime number")