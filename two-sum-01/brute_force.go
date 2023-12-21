// Brute-force
// Time: O(n^2)
// Space: O(1)


func twoSum(nums []int, target int) []int {
    // declare a Result array
    res := make([]int, 0, 2) 

    // size of the input array
    n := len(nums)

    // traversing the input arrray
    for i:=0; i < n; i++ {
        for j:= i+1; j<n; j++ {
            // check if sum of i and j is equal to target
            if target == nums[i] + nums[j] {
                // add these two indices to res array
                res = append(res, i, j)
                return res // exactly one solution
            }
        }
    }

    return res
}

/*
[]{2,11,7,15}  9

loop 1: 1st iternation, i = 0 , val: 2
// // j=11
target=11+2!=9  so loop continue then it will check another condition 
j=7 
target=2+7=9 the the result will print 
res is the indices of the values

*/