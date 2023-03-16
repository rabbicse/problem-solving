func rotate(nums []int, k int)  {
    l := len(nums)
    arr := make([]int, l)
    copy(arr, nums)
    
    for i := 0; i < l; i++ {
        nums[(i + k) % l] = arr[i]
    }
}
