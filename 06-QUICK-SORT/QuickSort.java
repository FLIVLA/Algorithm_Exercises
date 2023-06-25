public class QuickSort {

    public int[] sort(int[] nums) {
        if (nums.length <= 1) {
            return nums;
        } else {
            int p = nums[0];
            int[] l = new int[nums.length - 1];
            int[] r = new int[nums.length - 1];
            int lidx = 0;
            int ridx = 0;
            for (int i = 1; i < nums.length; i++) {
                if (nums[i] <= p) {
                    l[lidx++] = nums[i];
                } else {
                    r[ridx++] = nums[i];
                }
            }
            int[] result = new int[l.length + r.length + 1];
            System.arraycopy(l, 0, result, 0, l.length);
            result[l.length] = p;
            for (int i = 0; i < r.length; i++) {
                result[l.length + 1 + i] = r[i];
            } return result;
        }
    }

}