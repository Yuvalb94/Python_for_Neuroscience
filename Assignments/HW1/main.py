from Q1 import trifeca
from Q2 import compare_subjects_within_student
from Q3 import check_palindrome
##############
# Question 1 #
##############

inputs = [
    'aabbcc', 'abccddee0123', 'llkkbmm', 'aaaazz', 'bbcCdd', '112233',
    '12abaa22bcbc', ' ', '1s2abacc44rr'
]

print("Question 1 check:")

for inp in inputs:
  print(f"{inp} - {trifeca(inp)}")

##############
# Question 2 #
##############

# The data struture containing the grades is a dictionary, where the subject is
# specified in the value of the key 'subject' for using inside the function.
math_grades = {
    'subject': 'math',
    'Noa': [100, 95],
    'Remi': [88, 82],
    'Lora': [70, 75],
    'Taylor': [80, 85],
    'Jeremy': [92, 94],
    'Eliyahu': [98, 87]
}
history_grades = {
    'subject': 'history',
    'Noa': [99, 95],
    'Lora': [95, 90],
    'Oren': [80, 85],
    'Jeremy': [60, 75],
    'Eliyahu': [92, 94]
}
print("\nQuestion 2 check:")
print(compare_subjects_within_student(math_grades, history_grades))

##############
# Question 3 #
##############
print("\nQuestion 3 check:")
check_palindrome()
