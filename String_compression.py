# Time Complexity: O(n), as we traverse the list once.
# Space Complexity: O(1) as no additional data structures are used.
# Using two pointer technique

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Pointer for writing the compressed string
        read = 0   # Pointer for reading the input list
        
        while read < len(chars):
            char = chars[read]
            count = 0
            
            # Count the number of consecutive occurrences
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write
