func sortedSquares(nums []int) []int {    
    result := make([]int, len(nums))
    for i := 0;  i < len(nums); i++ {
        result[i] = nums[i] * nums[i]
    }
    sort.Ints(result)
    return result
}
