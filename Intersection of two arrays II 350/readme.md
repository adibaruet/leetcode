nums1 = [1, 2, 2, 3]
nums2 = [2, 2, 3, 3]
c = Counter(nums1)  # c = {1: 1, 2: 2, 3: 1}

Iteration 1: n = 2, c[2] > 0 -> output = [2], c = {1: 1, 2: 1, 3: 1}
Iteration 2: n = 2, c[2] > 0 -> output = [2, 2], c = {1: 1, 2: 0, 3: 1}
Iteration 3: n = 3, c[3] > 0 -> output = [2, 2, 3], c = {1: 1, 2: 0, 3: 0}
Iteration 4: n = 3, c[3] == 0 -> skip

Result: [2, 2, 3]
