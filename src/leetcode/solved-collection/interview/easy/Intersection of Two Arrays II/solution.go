func intersect(nums1 []int, nums2 []int) []int {
    hash := make(map[int]int)
    var ans []int
    
    for _, n := range nums1 {
        _, ok := hash[n]
        if ok {
            hash[n] = hash[n] + 1    
        } else {
            hash[n] = 1    
        }        
    }
    
    for _, n := range nums2 {
        val, ok := hash[n]
        if ok && val > 0 {
            hash[n] = hash[n] - 1 
            ans = append(ans, n)        
        }
    }
    
    return ans
}
