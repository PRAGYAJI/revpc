#!/usr/bin/env python
# coding: utf-8

# Problem Statement: 1
# You work in XYZ Corporation as a Data Analyst. Your company has told you to work with the IfElse Conditions.
# Tasks to be performed:
# 1. Input the values of a and b as 10 and 20 respectively. Now check if a is greater or b is greater
# using if condition. Think about all the edge cases, and print the statements accordingly.

# In[ ]:


a = 10
b = 20
if a>b:
    print("a is greater")
else:
    print("b is greater")


# In[ ]:





# Problem Statement: 2 You work in XYZ Corporation as a Data Analyst. Your company has told you to work with the IfElse Conditions. Tasks to be performed:
# 
# Take three user inputs and print the greatest number from those inputs using if-else condition. Edge cases if any, should also be handled.

# In[ ]:


a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))
if a > b and a>c:
    print("a is greater")
elif b>a and b>c :
    print("b is greater")
elif c>b and c>a:
    print("c is greater")
elif a==b and a==c and c==b:
    print("all are equal ")
elif a==b and a>c:
    print("a and b are same and is greater than c")
elif b==c and b>a:
    print("b and c are same and is greater than a")
else:
    print("error")


# In[ ]:





# Problem Statement: 3 You work in XYZ Corporation as a Data Analyst. Your company has told you to work with the IfElse Conditions. Tasks to be performed:
# 
# Print the numbers from 1 to 10 using while loop.

# In[2]:


x=1
while x<11 :
    print(x)
    x+=1


# Problem Statement: 4 You work in XYZ Corporation as a Data Analyst. Your company has told you to work with the IfElse Conditions. Tasks to be performed: Create a list that is having 10,23,4,26,4,75,24,54 values and with the help of while loop, fetch the even numbers and print the numbers.

# In[ ]:
a = [10,23,4,26,4,75,24,54]
i = 0
while i<len(a):
    if a[i]%2==0:
        print(a[i])
    i+=1



# Problem Statement: 5
# Consider yourself to be Sam who is a data scientist. He has been invited as a guest lecturer at a college
# to take an introductory session on Python.
# Tasks to be performed:
# 1. Create a list containing squares of numbers from 1 to 10 (HINT: use List Comprehension).
# 2. Write a Function to check if year number is a leap year.
# 3. Write a Function to take an array and return another array that contains the members of first
# array that are even.
# 4. Write a Function that takes 2 arrays and prints the members of first array that are present of
# second array. (HINT: use Membership Comprehension)
# 
# 

# In[ ]:
s = []
x = 1
while x < 11:
    b = x*x
    s.append(b)
    x+=1

print(s)



# In[ ]:
def leap_year(year):
    if((year%4 == 0 ) and (year % 100 != 0 ) ):
        return True
    else:
        return False

# In[ ]
def findEvenNo(lst):
    ans = []
    for i in lst:
        if(i%2 == 0):
            ans.append(i)
    return ans



# In[ ]:
def check(arr1, arr2):
    for i in range(0, len(arr1)):
        for j in range(0,len(arr2)):
            if arr1[i] == arr2[j]:
                print(arr2[j])



Problem Statement: 6
Consider yourself to be Sam who is a data scientist. He has been invited as a guest lecturer at a college
to take an introductory session on Python.
Tasks to be performed:
1. Create 1st tuple with values -> (10,20,30), 2nd tuple with values -> (40,50,60).
a. Concatenate the two tuples and store it in “t_combine”
b. Repeat the elements of “t_combine” 3 times
c. Access the 3rd element from “t_combine”
d. Access the first three elements from “t_combine”
e. Access the last three elements from “t_combine”
2. Create a list ‘my_list’ with these elements:
a. First element is a tuple with values 1,2,3
b. Second element is a tuple with values “a”,”b”,”c”
c. Third element is a tuple with values True,False
3. Append a new tuple – (1,’a’,True) to ‘my_list’
a. Append a new list – *“sparta”,123+ to my_list
4. Create a dictionary ‘fruit’ where:
a. The first key is ‘Fruit’ and the values are (“Apple”,”Banana”,”Mango”,”Guava”)
b. The second key is ‘Cost’ and the values are (85,54,120,70)
c. Extract all the keys from ‘fruit’
d. Extract all the values from ‘fruit’
5. Crete a set named ‘my_set’ with values (1,1,”a”,”a”,True,True) and print the result
# In[]:

