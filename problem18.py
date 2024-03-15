

# hackerrank assesment


def Contactlist(contactlimit):
    d = {}
    for i in range(contactlimit):
        name, number = input().split()
        d[name] = number
    return d
    # print(d)



if __name__=="__main__":
    contactlimit = int(input())
    d = Contactlist(contactlimit)
    while(True):
        query = input()
        if(query in d):
            print(query+"="+d[query])
        else:
            print("Not found")