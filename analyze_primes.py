def analyze_primes(primes):
    # Initialize lists for prime gaps and twin primes
    prime_gaps = []
    twin_primes = []

    # Iterate over the list of primes
    for i in range(len(primes) - 1):
        # Calculate the gap between the current prime and the next one
        gap = primes[i + 1] - primes[i]
        prime_gaps.append(gap)

        # Check if the gap is 2 (indicating a pair of twin primes)
        if gap == 2:
            twin_primes.append((primes[i], primes[i + 1]))

    # Return the lists of prime gaps and twin primes
    return prime_gaps, twin_primes

# Example usage:
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
prime_gaps, twin_primes = analyze_primes(primes)

print("Prime Gaps:", prime_gaps)
print("Twin Primes:", twin_primes)
