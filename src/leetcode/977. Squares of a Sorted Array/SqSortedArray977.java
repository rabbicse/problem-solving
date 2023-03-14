class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] results = new int[nums.length];
        for(int i = 0; i < nums.length; i++) {
            results[i] = nums[i] * nums[i];
        }
        Arrays.sort(results);
        return results;
    }
}
