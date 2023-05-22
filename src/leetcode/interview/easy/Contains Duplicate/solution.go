func containsDuplicate(nums []int) bool {
    dict := make(map[int]bool)
    
    for _, n := range nums {
        _, ok := dict[n]
        if  ok {
            return true
        }
        
        dict[n] = true
    }
    
    return false
}
