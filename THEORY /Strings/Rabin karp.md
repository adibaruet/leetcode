# Rabin-Karp Algorithm

## Introduction
The **Rabin-Karp Algorithm** is an efficient string-searching algorithm that uses hashing to locate a pattern in a given text. It improves upon brute-force approaches by leveraging hash codes for efficient comparison of substrings.

---

## The Problem with Hashing
### Hash Code Basics
A **hash code** is a numerical representation of a string. For example, given a string \( P \) of length \( m \), its hash code \( h(P) \) can be computed as:
\[
h(P) = (P_0 \cdot d^{m-1} + P_1 \cdot d^{m-2} + \ldots + P_{m-1}) \mod q
\]
Where:
- \( d \) is the size of the character set (e.g., 256 for ASCII).
- \( q \) is a prime number chosen to reduce hash collisions.

### Limitations of Hashing
1. **Hash Collisions**: Two different substrings can produce the same hash value, leading to false positives. Additional character-by-character comparisons are then required.
2. **Efficiency Concerns**: A naive hashing approach that recomputes the hash from scratch for every substring has a worst-case time complexity of \( O(nm) \).

---

## Rabin-Karp Algorithm
The **Rabin-Karp Algorithm** addresses these limitations using a **rolling hash**. Instead of recalculating the hash for every substring, the algorithm updates the hash in constant time as the pattern slides across the text.

---

## Algorithm Steps
1. Compute the hash of the pattern \( P \) and the initial substring of the text \( T \) of the same length.
2. Compare the hash values:
   - If the hashes match, verify the substrings character by character.
3. Slide the pattern one position to the right:
   - Update the hash for the next substring using the rolling hash formula.
4. Repeat steps 2–3 until the entire text is processed.

---

## Complexity
- **Best Case**: \( O(n - m + 1) \), where no hash collisions occur.
- **Average Case**: \( O(n - m + 1) \), assuming an even distribution of hash values.
- **Worst Case**: \( O(nm) \), when all hashes collide and require verification.

> **Note**: The average case is efficient because the rolling hash reduces the need for recomputation, making each substring comparison nearly constant time.

---

## Example
### Problem
Find the pattern `"AB"` in the text `"ABABDABACDABABCABAB"`.

### Parameters
- \( d = 256 \) (ASCII characters).
- \( q = 101 \) (a prime number).

### Execution
1. Compute the hash for the pattern \( P \) and the first substring of the text \( T_0 \) (length = pattern length).
2. Compare \( h(P) \) and \( h(T_0) \). If they match, confirm the match character by character.
3. Slide the pattern to the next position and update the hash using the rolling hash formula.

#### Results
The pattern `"AB"` is found at indices **0, 2, 8, 12, 16**.

---
