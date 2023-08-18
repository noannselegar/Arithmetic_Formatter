def formatter(listOps, ans=False):
    o = [ops.split() for ops in listOps]
    width = len(max(o))+5
    new_line = '\n'
    hyphen = '-'
    for x in range(len(listOps)):
        for i in range(3):
            print(f'{o[i][x].rjust(width)}', end='')
        else:
            print(new_line)     
    #print(o)