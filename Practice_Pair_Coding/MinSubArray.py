def minSubArray(arr):
    sub_array = []
    flag = False
    max_num = [None,0]
    counter = {}
    for num in arr:
        if num not in counter:
            counter.update({num:1})
        else:
            temp_val = counter.get(num)+1
            counter[num] = temp_val
        if counter[num] > max_num[1]:
            max_num = [num,counter[num]]


    target = max_num[0]
    for num in arr:
        if num == target:
            flag = True
        if flag:
            sub_array.append(num)
    if not flag:
        print("No value matches the target")
        return
    
    #second array to pop the values of the array until subarray contains only desired values
    end_pointer = len(sub_array)-1
    while(True):
        if(sub_array[end_pointer] == target):
            return len(sub_array)
        else:
            sub_array.pop(end_pointer)
            end_pointer-=1

    
test_list = [1,2,2,3,1]
print(minSubArray(test_list))


