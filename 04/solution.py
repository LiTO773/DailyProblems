def find_num(list):
  list.sort()
  # Remove all negative numbers (0 counts as a positive number)
  positive_list = []
  for elem in list:
    if elem >= 0:
      positive_list.append(elem)

  # Check the difference between elements
  num_missing = -1
  for i in range(len(positive_list)):
    if i + 1 == len(positive_list):
      num_missing = positive_list[i] + 1
      break
    
    if positive_list[i+1] - positive_list[i] != 1:
      num_missing = positive_list[i] + 1
      break

  # Return the value
  return num_missing

print(find_num([3, 4, -1, 1]))
print(find_num([1, 2, 0]))