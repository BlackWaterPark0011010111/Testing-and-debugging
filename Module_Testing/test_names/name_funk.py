def get_form_name(first,last,middle=''):
    if middle:
        full_name=f'{first} {middle} {last}'
    else:
        full_name=f'{first} {last}'
    
    return full_name.title()




#def get_formatted_name(first, middle, last):
#full_name = f"{first} {middle} {last}"
#return full_name.title()
"""
E 
===================================================================== 
ERROR: test_first_last_name (__main__.NamesTestCase) 
---------------------------------------------------------------------- 
Traceback (most recent call last): 
 File "test_name_function.py", line 8, in test_first_last_name
 formatted_name = get_formatted_name('janis', 'joplin') 
 TypeError: get_formatted_name() missing 1 required positional argument: 
 'last' 
---------------------------------------------------------------------- 
Ran 1 test in 0.000s
FAILED (errors=1)"""


#def get_formatted_name(first, last, middle=''):
#    if middle:
#        full_name = f"{first} {middle} {last}"
#    else:
#        full_name = f"{first} {last}"
#        return full_name.title()
#    """в качестве альтернативы и необязательного ввода,можно добавить middle=''"""