print('*'*80)
print(' 1. Make the first character upper case and the rest all lowercase')
print(' 2. Capitalize() method is used to capatialize the first letter of a string')
print(" 3. Returns new string, doesn't change the original string")
print('*'*80)

name='python'
name1='basic python'
name2='bAsic PYthon'
name3='bAsic PYTHON t'

print(' Given string :',name,' \t\t=> Capitalized string :',name.capitalize())
print(' Given string :',name1,' \t=> Capitalized string :',name1.capitalize())
print(' Given string :',name2,' \t=> Capitalized string :',name2.capitalize())
print(' Given string :',name3,' \t=> Capitalized string :',name3.capitalize())

# \t is an escape sequence to use TAB
print('*'*80+"\n\n****** BUILT IN DOC ******")
help(str.capitalize)