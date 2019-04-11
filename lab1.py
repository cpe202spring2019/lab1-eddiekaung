def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == None:       # error handling
      raise ValueError
   elif len(int_list) == 0:   # when the list is empty
      return None
   else:
      max_num = int_list[0]
      for num in int_list:
         if num > max_num:
            max_num = num
      return max_num


def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:      # error when list is None
      raise ValueError
   elif len(int_list) == 0:  # when the list is empty
      return []
   else:
      if len(int_list) == 1:
         return [int_list[0]]
      return [int_list[-1]] + reverse_rec(int_list[:-1])  # slicing list


def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if high < low:           # returns None if target is not found
      return None
   midpoint = (high + low) // 2
   if int_list[midpoint] == target:
      return midpoint
   elif target < int_list[midpoint]:   # when target is lower than midpoint
      return bin_search(target, low, midpoint - 1, int_list)
   elif target > int_list[midpoint]:   # when target is greater than midpoint
      return bin_search(target, midpoint + 1, high, int_list)

