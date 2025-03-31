def first_numer_to(list):
  for i, num in enumerate(list):
    if i==(len(list)-1):
      before = list[i-1]
      after = list[0]
    else:
      before = list[i-1]
      after = list[i+1]
    if num > (before + after):
      return (i, num)
  print("no number in the list in greater than the sum of its neighbors.")

my_list = [3, 3, 4, 6, 1]
index, number = first_numer_to(my_list)
print(f"The first number that is greater than the sum of its neighbors is {number} and its index is {index}.")