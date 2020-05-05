#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("enter the first name")


# In[28]:


print("enter the first name")
firstname = input()
print("enter the second name")
lastname = input()
print(lastname," ",firstname)


# In[17]:


pi_value = 3.1415926535897931
r_value= 13.0
V_value= 4.0/3.0*pi_value* r_value**3
print('The volume of the sphere is: ',V_value)


# In[20]:


saran = input("Input  comma sepersted numbers : ")
list = saran.split(",")
print(list)


# In[2]:


n=6;
for i in range(n):
    for j in range(i):
        print ('* ',end="")
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[7]:


print("enter the word")
word = input()
reversedstring=''.join(reversed(word))
print(reversedstring)


# In[18]:


print("WE, THE PEOPLE OF INDIA,\n\t\t having solemnly resolved to constitute India into a SOVEREIGN, \n\t\t\t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t\t and to secure to all its citizens")


# In[20]:


print ("Printing the divisble by 7 and not multiple of 5  b/w 2000 to 3200 \n")

"""Getting the numbers divisible by 7 """

my_list7=list(range(2000, 3201))

my_list7 = list(filter(lambda x: (x % 7 == 0) , my_list7))
""" print(my_list7)  """
final_result = list(filter(lambda x: (x % 5 !=0) , my_list7))


print(final_result)


# In[21]:


print("enter the first name")
firstname = input()
print("enter the second name")
lastname = input()
print(lastname," ",firstname)


# In[ ]:




