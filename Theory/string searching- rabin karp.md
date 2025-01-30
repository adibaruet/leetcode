# Rabin-Karp Algorithm

## Introduction
The **Rabin-Karp Algorithm** is an efficient string-searching algorithm that uses hashing to locate a pattern in a given text. It improves upon brute-force approaches by leveraging hash codes for efficient comparison of substrings.

---

## The Problem with Hashing
### Hash Code Basics
A **hash code** is a numerical representation of a string.

### Limitations of Hashing
1. **Hash Collisions**: Two different substrings can produce the same hash value, leading to false positives. Additional character-by-character comparisons are then required.
2. **Efficiency Concerns**: A naive hashing approach that recomputes the hash from scratch for every substring has a worst-case time complexity of ( O(nm) ).

---

## Rabin-Karp Algorithm
The **Rabin-Karp Algorithm** addresses these limitations using a **rolling hash**. Instead of recalculating the hash for every substring, the algorithm updates the hash in constant time as the pattern slides across the text.

---
## Complexity
- **Best Case**: \( O(n - m + 1) \), where no hash collisions occur.
- **Average Case**: \( O(n - m + 1) \), assuming an even distribution of hash values.
- **Worst Case**: \( O(nm) \), when all hashes collide and require verification.

> **Note**: The average case is efficient because the rolling hash reduces the need for recomputation, making each substring comparison nearly constant time.

---
Here is the Python  implementation of the Rabin Karp Algorithm:

```python
# d is the number of characters in the input alphabet
d = 256

# Function to search for the pattern in the text
def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1

    # The value of h would be "pow(d, M-1) % q"
    for i in range(M - 1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window of text
    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    # Slide the pattern over the text one by one
    for i in range(N - M + 1):
        # Check the hash values of the current window of text and pattern
        # If the hash values match, then only check for characters one by one
        if p == t:
            # Check for characters one by one
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break

            # if p == t and pat[0...M-1] = txt[i, i+1,...i+M-1]
            if j == M - 1:
                print(f"Pattern found at index {i}")

        # Calculate the hash value for the next window of text:
        # Remove the leading digit, add the trailing digit
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q

            # We might get a negative value of t, converting it to positive
            if t < 0:
                t = (t + q)

# Driver code to test the function
txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 101  # A prime number
search(pat, txt, q)
```

### Explanation:
- The logic in the Java code has been directly translated into Python.
- The function `search` calculates the hash values for both the pattern and the text, then slides the pattern across the text.
- The prime number `q` is used for modulus operations to prevent overflow.
- The main logic uses `ord()` to get the ASCII values of the characters (since Python strings work with Unicode by default).
# Source: GEEKS FOR GEEKS #
---
