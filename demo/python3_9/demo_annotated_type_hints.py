from typing import Annotated

# 이전에는 다음과 같이 Type Hints 에 실제 타입 대신 설명을 넣는 경우가 있었습니다.
def convert_m2cm(m: "meter") -> "centi":
    return m * 100


# Python 3.9 부터는 typing 모듈의 Annotated 타입을 사용해 실제 타입과 설명을 동시에 표현할 수 있습니다.
def convert_meter_to_cm(m: Annotated[int, "meter"]) -> Annotated[int, "centimeter"]:
    return m * 100


if __name__ == "__main__":
    print(convert_m2cm(50))
    print(convert_meter_to_cm(50))
