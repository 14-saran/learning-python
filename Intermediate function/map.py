#map function   - map(function,interable)
#               - Return an interator that applies function to ever item of interable

def make_even(num):
    if num%2==1:
        return num+1
    else:
        return num
    
x = [151,248,456,567,951,424,115,789]

y= list(map(make_even, x))
#=[make_even(num) for num in x]

print(y)
