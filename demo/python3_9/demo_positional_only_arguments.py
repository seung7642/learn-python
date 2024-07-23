# Python 3.8 에 도입된 Positional only arguments
#     슬래시(/) 앞에 위치한 파라미터는 오직 위치를 맞춰서 인수를 넣어야만 사용이 가능합니다.
#     say_hello(name="John")` 처럼 Keyword argument 로 사용 불가
def say_hello(name: str, /, greeting: str = "Hello"):
    return f"{greeting}, {name}"


print(say_hello("John", greeting="Hi"))


# Python 3.0 에 도입된 Keyword only arguments
def convert_cm_to_meter(*, meter):
    return meter * 100


print(convert_cm_to_meter(meter=50))


# Positional only arguments, Keyword only arguments 혼합하여 사용 가능
def title_format(text, /, padding="*", *, size=50):
    return f"    {text}    ".center(size, padding)


print(title_format("Hello", "*", size=50))
print(title_format("Hello", padding="*", size=50))
