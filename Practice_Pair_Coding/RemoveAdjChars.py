

## remove all adjacent duplicants

## input: string - lowercase english a-z

## transform: find two adjacent letters and remove them

## output: processed string with no adjacent characters

## ex:
## string: abbaca
## int_output: aaca
## final_output: ca

## string: azxxzy
## int_output: azzy
## final_output: ay

# option1
# process resursively

# option2
# [abbbbbbbbaca]
#   ^^      ^^
# last_duplicated_value = b
# [aac]
# set()



from tempfile import tempdir


def removeAdj(string):
    last_seen_char = None
    #list
    temp_string = []
    index = 0
    for char in string:
        if last_seen_char == None:
            temp_string.append(char)
            last_seen_char = char
            index+=1
            continue
        if last_seen_char != char:
            temp_string.append(char)
            last_seen_char = char
            index+=1
            continue
        else:
            temp_string.pop(index-1)
    
    #detect wether string contains a duplicate value still
    temp_set = set(temp_string)
    #loop through each value of new string and detect 
    for val in temp_set:
        count = temp_string.count(val)
        if count > 1:
            return removeAdj(''.join(temp_string))
    
    


    return temp_string

print(removeAdj("azxxzy"))
