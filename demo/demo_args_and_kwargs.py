def adding_numbers(*args):
    # args is just name of variable
    _sum = sum([arg for arg in args])
    return _sum


print(adding_numbers(1, 2, 3))


def concat_str(**kwargs):
    return "".join([kw for kw in kwargs])


print(concat_str(str1='a', str2='b', str3='c'))

def mix_args(x, y, *args, **kwargs):
    lst = [x, y]
    lst.extend([arg for arg in args])
    lst.extend([kw for kw in kwargs.values()])
    return lst


print(mix_args('x', 'y', 'z', a='1'))
