class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowel_str = []
        str_list = []

        # Collect characters and vowels
        for i in s:
            str_list.append(i)
            if i in vowels_list:
                vowel_str.append(i)

        # Reverse the list of vowels
        vowel_str.reverse()

        # Replace vowels in the string with the reversed vowels
        vowel_index = 0
        for j in range(len(str_list)):
            if str_list[j] in vowels_list:
                str_list[j] = vowel_str[vowel_index]
                vowel_index += 1

        # Join the list to form the final string
        result_str = ''.join(str_list)

        return result_str
