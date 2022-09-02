#Write a python program to merge two python dictionaries into one dictionary.

dict_var1={1:'rahul','yogichowk':'nilesh',3:'himanshu','srk':'gaurav','ahemdavad':'navkar'}
dict_var2={1:'saurabh',2:'karan',3:'nikhil',4:'jenil',5:'harshad'}

for x in dict_var1:
    if x in dict_var2:
        continue
    dict_var2[x]=dict_var1[x]
print('Merged Two Dicts :',dict_var2)