import math

def largest_prime_factor(n):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?   

    """
    #Setting the largest_number as 2 and reducing the given_input_number n by 2.
    largest_number = 0
    while n % 2 == 0:
        largest_number = 2
        n = n/2
    
    #At this point you will have your n as odd, so we skip all the even test cases by haiving a steps of 2 in range.

    for i in range(3, int(math.sqrt(n)+1),2):
        while n % i == 0:
            largest_number = i
            n = n/i
            
   
    if n>2:
        largest_number = n
    
    return int(largest_number)

    


print(largest_prime_factor(600851475143))



