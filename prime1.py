def is_prime(n):
    if n < 2:
        return False
    prime = True
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} is divisable by {x}\n")
            prime = False
    return prime


while True:
    number = int(input("Please enter a number (enter 0 to exit)\n "))
    if number == 0:
        break
    prime = is_prime(number)
    if prime is True:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
