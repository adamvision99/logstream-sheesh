#1

def task1(array):
    count=0
    for a in range(1,len(array)-1):
        if array[a]>array[a-1] and array[a]>array[a+1]:
            count+=1
    return count

#2


def task2(array,x):
    count = array.count(x)
    array.append(x)
    array.sort(reverse=True)
    if count==0:
        return array.index(x)+1
    else:
        return array.index(x)+count+1


#3

def task3():
    x = list()
    y = list()
    flag="NO"
    for i in range(8):
        _x, _y = [int(s) for s in input().split()]
        x.append(_x)
        y.append(_y)

    for i in range(8):
        for j in range(i+1,8):
            if x[i]==x[j] or y[i]==y[j] or abs(x[i]-x[j]) == abs(y[i]-y[j]):
                flag = 'YES'
    return flag

#4

def task4(x1,y1,x2,y2):
    return (((x1-x2)**2)+((y1-y2)**2))**0.5

#5

def task5(a,n):
    if n==0:
        return 1
    else:
        return a*task5(a,n-1)
#6

def task6(*args):
    new_dict = dict()
    for i in args:
        client, thing, value = i.split()
        if not new_dict.get(client):
            new_dict[client] = dict()
        if not new_dict[client].get(thing):
            new_dict[client][thing]=int(value)
        else:
            new_dict[client][thing]+=int(value)
    return new_dict

#7

def filter1(lang, n):
    newDict = dict()
    for (key, value) in lang.items():
        if value == n:
            newDict[key] = value
    return list(newDict.keys())

def task7():
    lang = dict()
    n = int(input())
    for i in range(0, n):
        m = int(input())
        for j in range(0, m):
            l = input()
            if l in lang:
                lang[l] += 1
            else:
                lang[l] = 1

    all_know = filter1(lang, n)
    print(len(all_know)) # выведите количество языков, которые знают все школьники
    print(sorted(all_know)) # список таких языков
    print(len(lang)) # количество языков, которые знает хотя бы один школьник
    print(sorted(list(lang.keys()))) # на следующих строках - список таких языков

if __name__ == "__main__":
    #print(task1([1,4,2,1,4,3,5,2,7]))
    #print(task2([171,178,170,170,170,198,157],170))
    #print(task3())
    #print(task4(2,-5,-4,3))
    #print(task5(2,4))
    #print(task6("Ivanov paper 10","Petrov pens 5","Ivanov marker 3","Ivanov paper 7","Petrov envelope 20","Ivanov envelope 5"))
    print(task7())
