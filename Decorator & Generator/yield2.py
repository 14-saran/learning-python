def sum_all_digit(n):
    return sum(int(c) for c in str(n))

def lucky(target=9, start_num=1, stop_num=100):
    d = []
    for i in range(start_num, stop_num + 1):
        if sum_all_digit(i) == target:
            d.append(i)
    return d

def luck_gen(target=9, start_num=1):
    i = start_num
    while True:
        if sum_all_digit(i) == target:
            yield i
        i += 1

print(lucky(9, 1, 100))
g = luck_gen(9,1)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print('--------------------------------')

def zip_demo():
    pretest = [5,10,9,7,2,3,9,]
    posttest = [4,5,9,6,2,3,10,]
    z = zip(pretest, posttest)
    print(next(z))
    for i,j in z:
        print(i,j)

zip_demo()

