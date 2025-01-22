class Solution:
    def compress(self, chars: List[str]) -> int:
        s =''
        string_dict = {}
        for i in chars:
            if i in string_dict:
                string_dict[i] +=1

            else:
                string_dict[i] =1
        
        for key,value in string_dict.items():
            if value==1:
                s += key
            else:
                s += key + str(value)

        chars[:] = list(s)
        return len(chars)
        
        
            

        
        
