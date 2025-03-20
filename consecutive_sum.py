# consecutive sums
def count_consecutive_sums(n):
    # Stores the number of ways
    count = 0
    
    # Try all values of k (length of sequence)
    k = 2
    while k * (k - 1) < 2 * n:
        # Check if 2n is divisible by k
        if (2 * n) % k == 0:
            # Compute x
            x = ((2 * n) // k - (k - 1)) // 2
            # x must be positive
            if x > 0:
                count += 1
        k += 1
        
    return count

# Example usage
n = 15
print(count_consecutive_sums(n))  

# Output: 3
# k = 2, 7 + 8 = 15
# k = 3, 4 + 5 + 6 = 15
# k = 4, 1 + 2 + 3 + 4 + 5 = 15 
