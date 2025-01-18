class Solution:
    def reverseWords(self, s: str) -> str:

        s=s.strip()
        reverse_words = ' '.join(s.split()[::-1])

        return reverse_words

        
