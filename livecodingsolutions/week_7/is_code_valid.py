def IsCodeValid(hfcode, message):
    emsg = ''
    huffcode = {}
    maxlength = 0
    for i, j in hfcode.items():
        huffcode[j] = i
        if len(j) > maxlength:
            maxlength = len(j)
    cd = ''
    for b in message:
        cd += b
        if len(cd) > maxlength:
            return False
        if cd in huffcode:
            emsg += huffcode[cd]
            cd = ''
    if cd == '':
        return True
    else:
        return False

hfcode = eval(input())
message = input()
print(IsCodeValid(hfcode,message)) 