#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

class StringSum {
public:
    vector<string> getPossibilities(string searchSpace, int target) {
        vector<string> result;
        if (searchSpace.empty()) {
            if (target == 0) result.push_back("");
            return result;
        }
        for (int i = 1; i <= searchSpace.size(); i++) {
            string take = searchSpace.substr(0, i);
            string permuteOn = searchSpace.substr(i, searchSpace.size()-1);
            int take_int = stoi(take);
            vector<pair<string, int> > remains;
            remains.push_back(make_pair("-", target+take_int));
            remains.push_back(make_pair("+", target-take_int));
            for (auto remain : remains) {
                vector<string> possibilities = getPossibilities(permuteOn, remain.second);
                if (!possibilities.empty()) {
                    for (string& possibilitiy : possibilities) possibilitiy = remain.first + take + possibilitiy;
                    result.insert(result.end(), possibilities.begin(), possibilities.end());
                }
            }
        }
        return result;
    }
};
int main() {
    StringSum obj;
    vector<string> results = obj.getPossibilities("123456789", 100);
    for (string result : results) cout << result << endl;
    return 0;
}
