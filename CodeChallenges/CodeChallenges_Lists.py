def append_size(lst):
  lst.append(len(lst))
  return lst

#print(append_size([23,42,108]))  

def append_sum(lst):
  for x in range(3 ):
   lst.append(lst[-1] + lst[-2])
  return lst

#print(append_sum([1,1,2]) )

def larger_list(lst1, lst2):
  if( len(lst1) >= len(lst2)):
    return lst1[-1]
  else:
    return lst2[-1]

#print(larger_list([4,10,2,5],[-10,2,5,10]))

def more_than_n(lst, item, n):
  return True if lst.count(item) > n else False
  
#print(more_than_n([2,4,6,2,3,2,1,2], 2, 3))

def combine_sort(lst1,lst2):
  return sorted(lst1 + lst2)
  
#print(combine_sort([4,10,2,5],[-10,2,5,10]))

# -------------------Advanced Challenges ----------------
def every_three_nums(num):
  return list(range(num, 101, 3))

#print(every_three_numbers(91))

def remove_middle(lst, start, end):
  del lst[start:end]
  return lst

#print(remove_middle([4,8,15,16,23,42],1,3))
def more_frequent_item(lst, item1, item2):
  
  x = lst.count(item1)
  y = lst.count(item2)
  return item1 if x >=y else item2

#print(more_frequent_item([2,3,3,2,3,2,3,2,3],2,3))

def double_index(lst, index):

  return lst[:index] + [lst[index] * 2] + lst[index+1:] if index > 0 and index < len(lst) else lst
   
 
#print(double_index([3,8,-10,12], - 2))

def middle_element(lst):
  midIndex = len(lst)/2
  return  lst[(int)(midIndex)]  if len(lst) % 2 > 0  else (int)((lst[(int)(midIndex)] + lst[(int)(midIndex) - 1]) /2)

  
  
print(middle_element([5, 2, -10, -4, 4
]))