def salt(password):
    count = 0
    lst = ''
    for i in password:
        count +=1
        lst = lst + i
        if count % 2 == 0:
            lst = lst + '$pain$'
    return lst