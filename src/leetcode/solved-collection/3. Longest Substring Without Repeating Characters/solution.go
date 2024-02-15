func lengthOfLongestSubstring(s string) int {
    n := len(s)
    result := 0
    for i := 0; i < n; i++ {
        visited := make([]bool, 256)
        for j := i; j < n; j++ {
            if visited[s[j]] {
                break
            } else {
                result = max(j - i + 1, result)
                visited[s[j]] = true
            }
        }
        visited[s[i]] = false
    }

    return result
}

func max(a, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}
