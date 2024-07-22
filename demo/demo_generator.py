from typing import Generator


def echo_round() -> Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return 'Done'


a = echo_round()
print(a.send(None))
print(a.send(3.5))
try:
    print(a.send(-3))
except StopIteration:
    print(f'StopIteration error.')
