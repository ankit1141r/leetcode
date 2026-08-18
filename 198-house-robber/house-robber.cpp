class Solution {
public:
    int rob(vector<int>& nums) {
        int prev = 0, maximum = 0;
        
        for (int num : nums) {
            int temp = max(maximum, prev + num);
            prev = maximum;
            maximum = temp;
        }
        
        return maximum;  
    }
};