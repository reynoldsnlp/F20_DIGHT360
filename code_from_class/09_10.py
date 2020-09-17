def is_prime(n):  # 9
    prime_number = True
    if n > 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # range(9) -> [2,3,4,5,6,7,8]
        if n % i == 0:
            prime_number = False
    return prime_number


for i in range(50):
    if is_prime(i):
        print(i)