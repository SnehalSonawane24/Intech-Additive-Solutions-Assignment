# String compression
def get_first_compress_string(s):
    
    # check if there is a any string if not then return
    if not s:
        return ""
    
    # list to store compressed string
    compressed_string = []
    # count to store occurrence of char in string
    count = 1
    
    # iterate over string
    for i in range(1, len(s)):
        
        # if char is same as previous char increase count by 1
        if s[i] == s[i - 1]:
            count = count + 1
        # if different append to list of compressed string and count will 1 for that char
        else: 
            compressed_string.append(s[i - 1] + str(count))
            count = 1
            
    # add last char and it's count 
    compressed_string.append(s[-1] + str(count))
    
    # convert list to string 
    final_compressed_string = ''.join(compressed_string)
    
    # returning final compressed string 
    return final_compressed_string 

# s = input()
# print("first compression",get_compress_string(s))


def get_second_compress_string(s):
    
    # list for storing 2nd compression string
    optimized_string = []
    i = 0
    while i < len(s):
        # get char
        char = s[i]
        i = i + 1
        num = ''
        
        # extract the number in any
        while i < len(s) and s[i].isdigit():
            num = num + s[i]
            i = i + 1
        
        n = int(num) if num else 1
        
        # if string has count 1 then remove it and keep number greater that equal to 2
        if n == 1:
            optimized_string.append(char)
            
        else:
            optimized_string.append(f"{char}{num}")
            
    # join to final string
    return ''.join(optimized_string)
    
def get_decompress_string(s):
    # list to store decompressed string
    decompressed_str = []
    i = 0
    
    # extract number from string if any
    while i < len(s):
        char = s[i]
        i = i + 1
        num_str = ''
        
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
            
        # convert number     
        num = int(num_str) if num_str else 1
        
        # repeat charecter num times
        decompressed_str.append(char * num)
        
    # joins list to final decompressed list 
    return ''.join(decompressed_str)
    
# function call
input_string = input()
first_compress_str = get_first_compress_string(input_string)
print("First compressed string: ", first_compress_str)

second_compress_str = get_second_compress_string(first_compress_str)
print("Second compressed string: ", second_compress_str)

decompress_str = get_decompress_string(second_compress_str)
print("Decompressed string: ", decompress_str)

# Input
# aabcccccaaa
# Output

"""
First compressed string:  a2b1c5a3
Second compressed string:  a2bc5a3
Decompressed string:  aabcccccaaa
"""
