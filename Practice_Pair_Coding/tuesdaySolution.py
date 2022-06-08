#
#  Given an array of 8 ints 
#  Binary
#  Prison Cells 
#  1 = Occupied 0 = empty
#   Example
#  Day 0 = [0,1,0,1,1,0,0,1]
#  Day 1 = [0,1,1,0,0,0,0,0]
#  If both neighbors are full or empty cells become occupied
#  [0,0,1,0,1,0,0]
#  [0,0,1,1,1,0,0]
#  [0,0,0,1,0,0,0]
#
#
#


Day_0 = [0,1,0,1,1,0,0,1]
Day_1 = [0,1,1,0,0,0,0,0]
Day_2 = [0,0,0,0,1,1,1,0]
days = 1

def prisonSimulator(cells,days):
    #apply rules to the beginning and end of the array

    #loop through each day to simulate interactions
    for day in range(0,days):
        ref_array = cells.copy()
        cells[0] = 0
        cells[-1] = 0
        for index in range(1,len(cells)-1):
            #check if left and right index is occupied
            if(ref_array[index-1] == ref_array[index+1]):
                cells[index] = 1
            else:
                cells[index] = 0
        print(cells)
    return cells

        
print(prisonSimulator(Day_0,15))
