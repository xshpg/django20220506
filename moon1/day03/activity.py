def fuc_arg(a,b,*args):
    print(a,b)
    print(args)

# fuc_arg(1,2,3,4)


def func_kwargs(a,b,*args,**kwargs):
    print(a,b)
    print(args)
    print(kwargs)
func_kwargs(1,2,3,4,c=1,m=2)