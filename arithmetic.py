def formatter(listOps, ans=False):
    listO = [ops.split() for ops in listOps]
    listS = [ops.split(maxsplit=1) for ops in listOps]
    res = list()

    for o in listO:
        if o[1] == '+':
            res.append(int(o[0])+int(o[2]))
        else:
            res.append(int(o[0])-int(o[2]))

    width = len(str(max(res)))*2
    for x in range(2):
        for i in range(len(listS)):
            print(f'{listS[i][x].rjust(width)}', end='')
        else:
            print('')
    else:
        for _ in range(len(listS)):
            print(' ', ''.center(width-2, '-'), end='')
        else:
            if ans==True:
                print('')
                for y in range(len(listS)):
                    print(' ', str(res[y]).rjust(width-2), end='')

