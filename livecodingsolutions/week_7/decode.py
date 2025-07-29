def decode(root, ciphertext):
    message = ''
    temp = root
    for i in ciphertext:
        if i == '0':
            temp = temp.left
        if i == '1':
            temp = temp.right
        if temp.left == None and temp.right == None:
            message += temp.symbol
            temp = root
    return message
