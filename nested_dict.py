#Write a python program to create a dictionary that contains three dictionaries.(nested)

dict_main={'dict_var1':{1:'rahul','yogichowk':'nilesh',3:'himanshu','srk':'gaurav','ahemdavad':'navkar'},'dict_var2':{'name':'Rahul Bhutaiya','age':20,'Profession':'Student','Currently_Studing':'B.C.A. T.Y.','Favourite_language':'Python'},'dict_va3':{1:'rahul',2:'nilesh',3:'himanshu',4:'gaurav',5:'navkar'}}

for key,value in dict_main.items():
    print(key,':',value)