class Solution {
    public boolean isPowerOfTwo(int n) {
        double x = Math.log10(n);
        double y = Math.log10(2);
         return (x/y) % 1  ==0;
    }
}