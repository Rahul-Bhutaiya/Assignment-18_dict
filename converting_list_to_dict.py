#Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.

list_var1=[1,2,3,4]
list_var2=['dell','hp','lenovo','mac-book']
dict_var={}

i=0
while i<4:
    dict_var[list_var1[i]]=list_var2[i]
    i+=1
print('List1 :',list_var1)
print('List2 :',list_var2)
print('Values in Dict : ',dict_var)