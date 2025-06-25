books = 1
if (books > 1 ):
    print("You have" ,books, 'books')
else:
    print('You have' ,books, 'book')

print('Your have',books, ('books' if (books >1 ) else 'book'))


print('--------------------------------')


# value_true if condition else value_false

x = 0

ans = 'positive' if x>0 else 'nagative' if x<0 else 'zero'
print(ans)


def check_pos_neg(num):
    return 'positive' if num>0 else ' nagative' if num<0 else 'zero'

print(check_pos_neg(10))

print('--------------------------------')

number = [1,2,3,4,5]

list = ['even' if num%2==0 else 'odd' for num in number]
print(list)