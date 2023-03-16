func twoSum(numbers []int, target int) []int {
    m := make(map[int]int)

    for i := 0; i < len(numbers); i++ {
        m[numbers[i]] = i
    }

    i := 0
    j := len(numbers) - 1
    for i < j {
        sum := numbers[i] + numbers[j]        
        if sum == target {
            return []int {i + 1, j + 1}
        } else if sum > target {
            j--;
        } else {
            i++;
        }
    }

    return []int{-1, -1}
}
