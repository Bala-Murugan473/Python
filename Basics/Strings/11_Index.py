print("11. INDEX")
# ref 8_Find.py
print("*" * 86)
print(
    """1. Returns the first index of the substring present in the given substring
2. if the given substring is not present it returns -1
3. Can also check with slicing the string as well
4. Same like find but  throws value error if the substring is not found
5. Case sensitive
6. Returns Integer"""
)
print("*" * 86)
print(
    """SYNTAX => String.index(substring,start_index,end_index)
start_index and end_index are optional"""
)
print("*" * 86)

txt = "Basic python"

index1 = txt.index("c")
# index2= txt.index('z')   # 'z' is not present, will throws ValueError
index3 = txt.index("")  # when passing empy string it will returns 0

print("Given String <=", txt)
print("'c' is at index =>", index1)
# print("'z' is at index =>",index2)
print("'' is at index =>", index3)

print("*" * 86 + "\n\n****** BUILT IN DOC ******")
help(str.index)

# \n is an escape sequence to use ENTER