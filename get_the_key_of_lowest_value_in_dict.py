"""
Write a python program to get the key of lowest value from the dictionary.
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}
"""

dict_var={eval(input('Key :')):eval(input('Value (int type only) :')) for x in range(int(input('How Much Items You Want To Enter In Dict...? ')))}
print('minimum value in dict :',min(dict_var.values()))