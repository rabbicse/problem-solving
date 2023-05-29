func singleNumber(nums []int) int {
    hash := make(map[int]int)
    
    for _, n := range(nums) {
        val, ok := hash[n]
        if ok {
            hash[n] = val + 1
        } else {
            hash[n] = 1
        }
    }
    
    for k, v := range hash { 
        if v == 1 {
            return k
        }
    }
    
    return -1
}
