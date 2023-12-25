// Brute-force
// Time: O(n^2)
// Space: O(1)
func majorityElement(nums []int) int {
    n := len(nums)

    if n == 1 {
        return nums[0]
    }
	
    for i:=0; i<= n/2; i++ {
        // 2
        count:= 1
        for j:=i+1; j<n; j++ {
            // main condition
            if nums[i] == nums[j] {
                count++
            }

            if count > n/2 {
                return nums[i]
            }
        }
    }
    return 0
}