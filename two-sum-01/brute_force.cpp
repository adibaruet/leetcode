#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::vector<int> res;

        // Size of the input array
        int n = nums.size();

        // Traverse the input array
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                // Check if the sum of nums[i] and nums[j] is equal to the target
                if (target == nums[i] + nums[j]) {
                    // Add the indices to the result vector
                    res.push_back(i);
                    res.push_back(j);
                    return res; // Exactly one solution
                }
            }
        }

        return res;
    }
};
