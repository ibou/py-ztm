from functools import reduce

def multiply_by_2(x):
    new_list = []
    # for i in range(0, len(x)):
    #     x[i] = x[i] * 2
    # for i in x:
    #     new_list.append(i*2)
    # return new_list
    return x * 2

# print(multiply_by_2([1, 2, 3, 5, 9]))  # [2, 4, 6]
print(list(map(multiply_by_2, [1, 2, 3, 5, 9]))) # [2, 4, 6, 10, 18]

# 1 Capitalize all of the pet names and print the list
my_pets = ["sisi", "bibi", "titi", "carla"]

def capitalize(string):
    return string.upper()

# print(list(map(capitalize, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [5, 4, 3, 2, 1]

# my_numbers.sort()
print(list(zip(my_strings,sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def is_smart_student(student):
    return student > 50
  
print(list(filter(is_smart_student, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item
  
print(reduce(accumulator, (my_numbers + scores)))

