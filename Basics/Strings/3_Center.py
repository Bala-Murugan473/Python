print("3. CENTER\n" + "*" * 86)

print(
    """1. Can be used to get a centralized string with given length
2. Padding is done using the specified fill character(Default fiiling character is space)
3. Returns a new centered string of length width, doesn't change the original string"""
)
print("*" * 86)
print("""SYNTAX => String.center(width : int, fillchar=' ')""")
print("*" * 86)

name = "Python"
print("Center of size 20 with default char :", name.center(20))
print('Center of size 20 with given"^"char :', name.center(20, "^"))

print("*" * 86 + "\n\n****** BUILT IN DOC ******")
help(str.center)