# Checks if a number is prime
def is_prime(n):

    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# First 100 digits of Pi
def find_largest_prime_in_pi():
    pi_digits = (
        "314159265358979323846264338327950288419716939937510582097494459"
        "2307816406286208998628034825342117067"
    )
    
    max_prime = 0

    # Iterate over all 5-digit substrings
    # 100 digits → 96 five-digit numbers
    for i in range(len(pi_digits) - 4):
        # Extract 5-digit number
        num = int(pi_digits[i:i+5])
        # Check if it's prime
        if is_prime(num):
            max_prime = max(max_prime, num)

    return max_prime

# Run the function and print result
largest_prime = find_largest_prime_in_pi()
print(f"Largest 5-digit prime in the first 100 digits of Pi: {largest_prime}")
