def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "0으로 나눌 수 없습니다."

if __name__ == "__main__":
    a = int(input("첫 번째 숫자를 입력하세요: "))
    b = int(input("두 번째 숫자를 입력하세요: "))

    print(f"{a} + {b} = {addition(a, b)}")
    print(f"{a} - {b} = {subtraction(a, b)}")
    print(f"{a} * {b} = {multiplication(a, b)}")
    print(f"{a} / {b} = {division(a, b)}")