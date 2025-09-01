def Count_Divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i == n // i:
                count += 1
            else:
                count += 2
        i += 1
    return count

# Test Cases
print(Count_Divisors(12))   
print(Count_Divisors(18))   
print(Count_Divisors(29))  
print(Count_Divisors(100)) 
print(Count_Divisors(1))   
print(Count_Divisors(997)) 
print(Count_Divisors(36)) 
