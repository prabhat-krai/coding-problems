class Solution {
public:
    bool isHappy(int n) {
        int i = 0;
        while(n != 1 && i < 100){
            int q = 0;
            while(n!= 0){
                q += (n%10)*(n%10);
                n /=10;
                i += 1;
            }
            n = q;
        }
        return n==1;
    }
};