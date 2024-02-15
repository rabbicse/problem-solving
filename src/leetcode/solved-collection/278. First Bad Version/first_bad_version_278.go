/** 
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad 
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */

func firstBadVersion(n int) int {
    start := 0
    end := n
    index := -1

    for start <= end {
        mid := int((start + end) / 2)
        if isBadVersion(mid) {
            index = mid
            end = mid - 1            
        } else {
            start = mid + 1
        }
    }
    return index
}
