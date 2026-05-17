def is_isogram(string):
    string = string.lower().strip()

    string = ''.join(c for c in string if c.isalpha())
    
    for i in range(len(string)):
        
        for j in range(i + 1, len(string)):
            
            if string[i] == string[j]:
                
                return False
    
    return True