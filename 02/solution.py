list = [1, 2, 3, 4, 5] # <-- Given list goes here
answer = []

for i in range(len(list)):
  answer.append(1)
  for j in range(len(list)):
    answer[i] *= list[j] if i != j else 1

print(answer)