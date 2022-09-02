#Write a python program to change the value of a specific item by referring to its key name.

dict_var={1:'rahul',2:'nilesh',3:'himanshu',4:'gaurav',5:'navkar'}
print('original dict variable :',dict_var.items())

dict_var[1]='bhutaiya'
print('after changing value of item by its key name :',dict_var.items())