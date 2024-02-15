import java.util.*;

class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Hashtable<Integer, Integer> hash = new Hashtable<>();
        List<Integer> answer = new ArrayList<>();
        
        for(int n : nums1) {
            if(hash.containsKey(n)) {
                hash.put(n, hash.get(n) + 1);
            } else {
                hash.put(n, 1);
            }
        }
        
        for(int n : nums2) {
            if(hash.containsKey(n) && 
               hash.get(n) > 0) {
                hash.put(n, hash.get(n) - 1);
                answer.add(n);
            }
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
