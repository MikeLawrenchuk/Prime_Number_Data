# Prime Number Analyzer

This Python program analyzes a list of prime numbers. It calculates the gaps between consecutive primes and identifies pairs of twin primes.

## How to Use

1. Ensure you have Python installed on your machine. This program was developed using Python 3.8, but it should work with any version of Python 3.

2. Save the Python script in a file, for example `prime_analyzer.py`.

3. Prepare a list of prime numbers in ascending order. This list should be written in the Python script in the `primes` variable.

4. Run the script using Python. For example, if you're using a command line interface, you can run the script with the command `python prime_analyzer.py`.

The program will print two lists: one for the gaps between consecutive primes, and one for the pairs of twin primes.

## Example

Here's an example of how to use the program:

```python
# Example usage:
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
prime_gaps, twin_primes = analyze_primes(primes)

print("Prime Gaps:", prime_gaps)
print("Twin Primes:", twin_primes)
```

In this example, the program analyzes the first 25 prime numbers. The output will be:

```
Prime Gaps: [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8]
Twin Primes: [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73)]
```

## License

This program is free to use, modify, and distribute under the terms of the MIT license.

---
