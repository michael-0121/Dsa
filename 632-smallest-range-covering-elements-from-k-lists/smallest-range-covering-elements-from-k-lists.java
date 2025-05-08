import java.util.*;

class Solution {
    public int[] smallestRange(List<List<Integer>> nums) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        int maxElement = Integer.MIN_VALUE;
        for (int i = 0; i < nums.size(); i++) {
            pq.offer(new int[]{nums.get(i).get(0), 0, i});
            maxElement = Math.max(maxElement, nums.get(i).get(0));
        }
        
        int[] ans = {-100000, 100000};
        
        while (!pq.isEmpty()) {
            int[] temp = pq.poll();
            int element = temp[0];
            int index = temp[1];
            int listIndex = temp[2];
            
            if (maxElement - element < ans[1] - ans[0]) {
                ans[0] = element;
                ans[1] = maxElement;
            }
            
            if (index + 1 < nums.get(listIndex).size()) {
                int nextElement = nums.get(listIndex).get(index + 1);
                pq.offer(new int[]{nextElement, index + 1, listIndex});
                maxElement = Math.max(maxElement, nextElement);
            } else {
                break;
            }
        }
        
        return ans;
    }
}

