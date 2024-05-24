
my_list = [1,2,3,4,5]
  
print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item%2 ==0, my_list)))
new_list = list(map(lambda item: item**2, my_list))
print(new_list)

listdata = ['a', 'b', 'c', 'd', 'e']
second_list = list(map(lambda item: item.upper(), listdata))
print(second_list)