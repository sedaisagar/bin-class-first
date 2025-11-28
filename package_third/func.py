# Functions In Python

# Ordinary function definition / declaration
# def ordinary_func(d,c,e,a="",b=1,):
#     pass
#     total : int = 5
#     return b,total,a,e,d,c

def ordinary_func(a,b,*args,kiran=0, **kwargs):
    # list((1,2,3,4,)) => [1,2,3,4]
    # *[1,2,3,4] => 1,2,3,4
    values = [*list(args),*list(kwargs.values())]
    return values, args, kwargs, a, b, kiran
# Function Calls
# 

rvs = ordinary_func(1,2,3,4,d=2,c=3, kiran="pandey") 
print(rvs)