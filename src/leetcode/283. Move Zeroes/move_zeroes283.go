func moveZeroes(nums []int)  {
    k := 0
    for i := 0; i < len(nums); i++ {
        if nums[i] != 0 {
            nums[i], nums[k] = nums[k], nums[i]
            k++
        }
    }
}
