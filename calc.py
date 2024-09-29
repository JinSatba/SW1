# calc.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    x = int(input("첫 번째 숫자를 입력하세요: "))
    y = int(input("두 번째 숫자를 입력하세요: "))

    print(f"{x}와 {y}의 합은: {add(x, y)}")
    print(f"{x}와 {y}의 차는: {subtract(x, y)}")