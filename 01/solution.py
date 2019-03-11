list = [10, 15, 3, 7]
target = 17
found = False

for i in range(len(list)):
  if found: break # Already found a match
  for j in range(len(list)):
    if i != j:
      if list[i] + list[j] == target:
        print("FOUND! " + str(list[i]) + " + " + str(list[j]) + " = " + str(target))
        found = True
        break

if not found:
  print("No matches found!")