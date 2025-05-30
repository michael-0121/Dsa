class Solution {
    public boolean isPowerOfFour(float n) {
        double x = Math.log10(n);
        double y = Math.log10(4);
         return (x/y) % 1  ==0;
    }
}