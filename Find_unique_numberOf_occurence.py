class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_arr = dict()
        n = len(arr)
        for i in range(n):
            if arr[i] in dict_arr:
                dict_arr[arr[i]] += 1 # increasing the count/value of that key 
            
            if arr[i] not in dict_arr:
                dict_arr[arr[i]] = 1 # setting the count of that first key as 1
        

        '''
        #Using the set method to check if any values are same or not
        seen_value = set()

        for key, value in dict_arr.items():
            if value in seen_value:
                return False
                break
            
            seen_value.add(value)
        '''
        # the ubove method for checking if any values in the dictionary are same
        # can be obtained by this below set length checking method as well.
        if len(set(dict_arr.values())) < len(dict_arr.values()):
            return False 

        return True


            


        
