def is_prime(num):
    divisibility = 0
    for i in range(1,num+1):
        if num % i == 0:  # this means it's divisible
            divisibility += 1
    if divisibility <= 2:
        return True
    else:
        return False


print(is_prime(73))

