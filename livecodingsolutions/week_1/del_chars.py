# delete all characters fro a given string
def del_char(s, c):
    if len(c) != 1:
        return(s)
    snew = ""
    for char in s:
        if char != c:
            snew = snew + char
    return(snew)

s = input()
c = input()
print(del_char(s,c))