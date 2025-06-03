class Solution {
    public int countPrimes(int n) {
        boolean [] composites = new boolean [n];
        for (int i=2; i<Math.sqrt(n);i++){
            if (composites [i]==false){
                for (int j=2 ; j*i<n ;j++){
                    composites[i*j] = true;
                }
            }
        }
        int prime =0;
        for(int i=2;i<n;i++){
            if (composites[i]==false){
                prime++;
            }
        }
        return prime;
    }
}