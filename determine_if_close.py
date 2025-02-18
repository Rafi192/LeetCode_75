# Difficulty = Medium
# Time complexity - O(N)
# Space complexity -O(1)

# Determine if two strings are close
'''
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

'''


from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False  # Different lengths cannot be close
        
        set1, set2 = set(word1), set(word2)
        if set1 != set2:
            return False  # Both words must contain the same characters
        
        freq_dict1 = dict()
        freq_dict2 = dict()
        for i in word1:
            if i not in freq_dict1:
                freq_dict1[i] = 1 # initialize count with 1
            else:
                freq_dict1[i] +=1 # increasing the frequncy count
        
        for i in word2:
            if i not in freq_dict2:
                freq_dict2[i] = 1 # initialize count with 1
            else:
                freq_dict2[i] +=1 # increasing the frequncy count
        
             

        #freq1 = Counter(word1)
        #freq2 = Counter(word2)
        if sorted(freq_dict1.values()) == sorted(freq_dict2.values()):
            return True  # The frequency distributions must match
        
        return False  # Otherwise, they are not close
