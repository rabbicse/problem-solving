import java.util.*;

class Solution {
    public int singleNumber(int[] nums) {
        Hashtable<Integer, Integer> hash = new Hashtable<>();
        
        for(int n : nums) {
            if(hash.containsKey(n)) {
                hash.put(n, hash.get(n) + 1);
            } else {
                hash.put(n, 1);
            }
        }
        
        for(Integer k : hash.keySet()) {
            int v = hash.get(k);
            if(v == 1) return k;
        }
        
        return -1;
    }
}
