print("1. CAPITALIZE\n" + "*" * 86)

print("""1. Make the first character upper case and the rest all lowercase
2. Capitalize() method is used to capitalize the first letter of a string
3. Returns new string, doesn't change the original string""")

print("*" * 86)
print("""SYNTAX => String.capitalize()""")
print("*" * 86)

name = "python"
name1 = "basic python"
name2 = "bAsic PYthon"
name3 = "bAsic PYTHON t"

capitalized_name = name.capitalize()
capitalized1_name = name1.capitalize()
capitalized2_name = name2.capitalize()
capitalized3_name = name3.capitalize()

print(" Given string :", name, " \t\t=> Capitalized string :", capitalized_name)
print(" Given string :", name1, " \t\t=> Capitalized string :", capitalized1_name)
print(" Given string :", name2, " \t\t=> Capitalized string :", capitalized2_name)
print(" Given string :", name3, " \t=> Capitalized string :", capitalized3_name)

print("*" * 86 + "\n\n****** BUILT IN DOC ******")
help(str.capitalize)

# \t is an escape sequence to use TAB
# \n is an escape sequence to use ENTER