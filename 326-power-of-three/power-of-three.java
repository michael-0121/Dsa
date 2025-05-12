class Solution {
    public boolean isPowerOfThree(int n) {
         double x = Math.log10(n);
        double y = Math.log10(3);
         return (x/y) % 1  ==0;
    }
    }
