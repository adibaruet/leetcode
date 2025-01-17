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



---

## Complexity
- **Best Case**: \( O(n - m + 1) \), where no hash collisions occur.
- **Average Case**: \( O(n - m + 1) \), assuming an even distribution of hash values.
- **Worst Case**: \( O(nm) \), when all hashes collide and require verification.

> **Note**: The average case is efficient because the rolling hash reduces the need for recomputation, making each substring comparison nearly constant time.

---

---
