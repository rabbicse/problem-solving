class Solution {
    public void rotate(int[] nums, int k) {
        int len = nums.length;
        int[] ans = Arrays.copyOf(nums, len);

        for(int i = 0; i < len; i++) {
            nums[(i + k) % len] = ans[i];
        }
    }
}
