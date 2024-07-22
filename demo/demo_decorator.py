from typing import Callable, TypeVar, Any, ParamSpec

T = TypeVar('T', bound=[int, str])
P = ParamSpec('P')


def trace(func: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'{func.__name__}({signature}) function start')
        result = func(*args, **kwargs)
        print(f'{func.__name__}({signature}) function end')
        return result
    return wrapper


@trace
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(a=1, b=2))


def multiple_two(a: int, b: int) -> int:
    return a * b


print(trace(multiple_two)(3, 4))

