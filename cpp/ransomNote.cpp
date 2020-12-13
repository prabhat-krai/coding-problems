class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        map<char, int> mag;
        for(char i : magazine){
            if(mag.find(i) != mag.end()){
                mag[i] +=1;    
            } else {
                mag[i] = 1;
            }
          
        }
        for(char j : ransomNote){
            if(mag.find(j) == mag.end()){
                return false;
            } else {
                if(mag[j] == 0){
                    return false;
                } else {
                    mag[j]--;
                }
            }
        }
       return true;
    }
};