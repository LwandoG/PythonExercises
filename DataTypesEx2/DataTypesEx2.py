numbers = [56,78,34,21,56,34,125,45,89,75,12,56]
numbers.sort() #sorting the list in ascending order
print("The largest number is " +str(numbers[numbers.__len__()-1]))
print("The smallest number is "+str(numbers[0]))
numbers2 =[]

#print(flag)

for i in numbers:
    if i not in numbers2:  #comparing the old list with new list
        numbers2.append(i) #adding the value if it is not already in list

print(numbers2) #printing with no duplicates

print("The sum is " +str(sum(numbers))) #printing the sum