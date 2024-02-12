# 01. Read two strings from user then concatenate them and store the concatenation in string.
'''str1 = input("Enter your first word: ")
str2 = input("Enter your second word: ")
str3 = str1 + str2
print(f"Concatenated Word:", str3)'''

#02. Read string from user then converts the first character to upper case
'''str1 = input("Enter your word:")
str1 = str1.capitalize()
print(f"Capitalized word: {str1}")'''

#03. Read string from user then convert this string to lower case.
'''str1 = input("Enter your word: ")
str1 = str1.lower()
print(f"the lower case: {str1}")'''

#04. Read string from user then convert this string to upper case.
'''str1 = input("Enter your word: ")
str1 = str1.upper()
print(f"the lower case: {str1}")'''

#05. Read string from user then enter character and show if this string contains this character or no and if yes show its index in string.
'''str1 = input("Enter your word: ")
char = input("Enter your character: ")
x = str1.find(char)
print(f"The character index : {x}") '''

#duplicated char??    

        
# 06. Read string from user then replace each space ' ' by comma ','. 
'''str1 = input("Enter your word: ")
str1 = str1.replace(' ',',')
print(f"No spaces : {str1}")'''

# 07. Read string from user then convert the first character of each word to upper case.
'''str1 = input("Enter your word: ")
str1 = str1.title()
print(f"First char capital : {str1}")'''

# 08. Read string from user then replace each comma by ',' by astrisk '*'.
'''str1 = input("Enter your word: ")
str1 = str1.replace(',','*')
print(f"No coma : {str1}")'''

# 09. Read string from user then remove all spaces at the first and the last.
'''str1 = input("Enter your word: ")
str1 = str1.replace(' ','')
print(f"No spaces : {str1}")'''

# 09. Read string from user then convert string to list by splitting string after each space?
'''str1 = input("Enter your world: ")
str1 = str1.split(' ')
list1 = list(str1)
print(f"String to list : {list1}")'''

# 10. Read string and check if this string starts with vowel or not.
'''str1 = input("Enter your word: ")
vowels = ['a','i','o','u','e']
if str1[0].lower() in vowels:
    print("The word starts with vowel")
else:
    print("The word dose not starts with vowel")'''

# 11. Read list from user then sort this list.
'''size = input("Enter the list size: ")
list1 = []
for n in range(int(size)):
    var = input(f"enter your number {n+1}: ")
    list1.append(int(var))
list1.sort()  
print(f"Sorted list: {list1}") '''

# 12. Read list from user then get the second-to-last number in the list.
'''size = input("Enter the list size: ")
list1 = []
for n in range(int(size)):
    var = input(f"enter your number {n+1}: ")
    list1.append(int(var))  
#list1.remove(list1[0]) 
print(f"Sorted list: '{list1[1:]}'")''' 

# 13. Read list of degrees and find the max degree in this list.
'''size = input("Enter the list size: ")
list1 = []
for n in range(int(size)):
    var = input(f"enter your number {n+1}: ")
    list1.append(int(var))  
max = list1[0]
for x in list1:
    if x >= max:
        max = x
print(f"The max degree : {max}")'''    

'''size = input("Enter the list size: ")
list1 = []
for n in range(int(size)):
    var = input(f"enter your number {n+1}: ")
    list1.append(int(var))
list1.sort()  
print(f"The max degree : '{list1[-1]}'")'''

# 14. Read list of words and find longest word.
'''size = input("Enter the list size: ")
list1 = []
for n in range(int(size)):
    var = input(f"enter your number {n+1}: ")
    list1.append(var)
longest = list1[0]
for x in list1:
    if len(x) >= len(longest):
        longest = x 
print(f"The longest word : {longest}") '''

'''size = input("Enter the list size: ")
list1 = []
list2 =[]
for n in range(int(size)):
    var = input(f"enter your number {n+1}: ")
    list1.append(var)
list1 = sorted(list1 , key=len)
print(f"The max degree : {list1[-1]}")'''

# 15. Read list and append any item to this list.
'''size = input("Enter the list size: ")
list1 = []
for n in range(int(size)):
    var = input(f"enter your number {n+1}: ")
    list1.append(var)
list1.append('The end')    
print(f"The appended item: {list1}")'''

# 16. Read list from user then give user the apility to remove item with the specified value.
'''size = input("Enter the list size: ")
list1 = []
for n in range(int(size)):
    var = input(f"enter your number {n+1}: ")
    list1.append(var)
removedWord = input("Enter the value you want to remove or 'NO' to stop: ")
if removedWord == 'NO':
    print(f"your list without removing : {list1}")
else:    
    list1.remove(removedWord)
    print(f"your list after removing : {list1}")'''    

# 17. Write a Python program to convert a list to a tuple.
'''size = input("Enter the list size: ")
list1 = []
for n in range(int(size)):
    var = input(f"enter your number {n+1}: ")
    list1.append(int(var))
listToTuple = tuple(list1)
print(f"Convert list to tuple: {listToTuple}")'''

# 18. Write a Python program to reverse a tuple.
'''tuple1 = (1,2,3,4,5)
list1 = list(tuple1)
list1.sort(reverse = True)
tuple1 = tuple(list1)
print(f"Reversed tuple: {tuple1}")'''

# 19. Write a python program to find size of set.
'''set1 = {1,2,3,4,5}
print(len(set1))'''

'''size = input("Enter your range: ")
set1 = set()
for n in range(int(size)):
    var = input(f"enter your number {n+1}: ")
    set1.add(int(var))
print(f"The size of the set: {str(set1.__sizeof__())} bytes")'''

# 20. Write a program to Read list from user then print distinct items in this list.
'''size = input("Enter the list size: ")
list1 = []
for n in range(int(size)):
    var = input(f"enter your number {n+1}: ")
    list1.append(int(var))
list1 = list(set(list1))
print(f"NO Duplicated values : {list1}")'''

'''size = input("Enter the list size: ")
list1 = []
for n in range(int(size)):
    var = input(f"enter your number {n+1}: ")
    list1.append(int(var))
NoDuplicate = []
for x in list1:
    if x not in NoDuplicate:
        NoDuplicate.append(x) 
print(f"NO Duplicated values : {NoDuplicate}")'''

# 21. Write a program to find sum of all items in tuples.
'''tuple1 = (1,2,3,4,5,6,7)
sum = 0
for x in tuple1:
    sum += x
print(f"sum of all items in tuples : {sum}")'''

# 22. Write a program Removes all the elements from the list.
'''list1 = [1,2,3,4,5,6,7]
print(f"Before clear:{list1}")
list1.clear()
print(f"Clear list: {list1}")'''

# 23. Write a program to print dictionary values without keys.
'''size = input("Enter the list size: ")
dict1 = {}
for n in range(int(size)):
    Key = input("Enter The Key: ")
    Value = input("Enter The value: ")
    dict1[Key] = Value

#print(dict1)
print(f"The Dictionary values:  {dict1.values()}")'''

# 24. Write a program to print dictionary keys only.
'''size = input("Enter the list size: ")
dict1 = {}
for n in range(int(size)):
    Key = input("Enter The Key: ")
    Value = input("Enter The value: ")
    dict1[Key] = Value

#print(dict1)
print(f"The Dictionary keys:  {dict1.keys()}")'''

# 25. Write a program to print a specefic item by key.
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "bran": "Ford",
  "mod": "Mustang",
  "yr": 1964
}'''


'''size = input("Enter the list size: ")
dict1 = {}
for n in range(int(size)):
    Key = input("Enter The Key: ")
    Value = input("Enter The value: ")
    dict1[Key] = Value

#print(dict1)
x = input("Enter the key: ")
for k,v in dict1.items():
    if k == x:
        print(f"The value by its key:l {v}")'''

# 26. Write a Python program to remove duplicates from Dictionary.
'''size = input("Enter the list size: ")
dict1 = {}
for n in range(int(size)):
    Key = input("Enter The Key: ")
    Value = input("Enter The value: ")
    dict1[Key] = Value
list1 =[]
dict2 = {}
for x, y in dict1.items():
    if y not in list1:
        list1.append(y)
        dict2[x] = y 
print(f"Dictionary without duplicated: {dict2}")'''


# 27. Write a Python program to check a dictionary is empty or not.
'''thisdict ={}
if len(thisdict) == 0:
    print("dictionary is empty")
else:
    print("Dictionary is not empty") ''' 
     
# 28. Write a NumPy program to create an array of 10 zeros and 10 ones.
'''import numpy as np 
a = np.zeros(10)
b = np.ones(10)
print(f"Zeros array :{a} \nOnes array: {b}")'''

# 29. Write a NumPy program to generate a random number between 0 and 1.
'''import numpy as np
rand_num = np.random.uniform(0, 1)
print("Random number between 0 and 1: ",rand_num)'''

# 30. Write a NumPy program to create an array of the integers from 30 to 70.
'''import numpy as np
arr1 =np.arange(30,71)
print("Array of the integers from 30 to70: \n",arr1)'''


#D:\GP\Cousres\PyTask\task.py