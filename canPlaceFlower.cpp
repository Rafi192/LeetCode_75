class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int size = flowerbed.size();
        for (int i = 0; i < size && n > 0; i++) {
            if (flowerbed[i] == 0 && 
            (i==0 || flowerbed[i-1]==0)
             {
                flowerbed[i] = 1;
                n--;
            }
        }
        return n <= 0;
    }
};
