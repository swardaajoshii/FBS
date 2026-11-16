def factors(n):
    print("Factors of", n, ":", end=" ")
    
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

factors(8)
