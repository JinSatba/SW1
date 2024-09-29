def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다."
    return a / b

if __name__ == "__main__":
    x = int(input("첫 번째 숫자를 입력하세요: "))
    y = int(input("두 번째 숫자를 입력하세요: "))

<<<<<<< HEAD
    print(f"숫자의 합은 {add(x, y)}입니다.")
=======
    print(f"Feature 1에서 수정된 결과: {add(x, y)}")
>>>>>>> feature-branch1
    print(f"{x}와 {y}의 차는: {subtract(x, y)}")
    print(f"{x}와 {y}의 곱은: {multiply(x, y)}")
    print(f"{x}를 {y}로 나눈 결과는: {divide(x, y)}")