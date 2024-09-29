def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

if __name__ == "__main__":
    a = int(input("첫 번째 숫자를 입력하세요: "))
    b = int(input("두 번째 숫자를 입력하세요: "))

    print(f"{a} + {b} = {addition(a, b)}")
    print(f"{a} - {b} = {subtraction(a, b)}")