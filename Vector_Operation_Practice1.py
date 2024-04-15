#두 벡터 내적 함수
def inner_product(x,y):
    res = 0
    for i in range(len(x)) :
        res += x[i] * y[i]
    return res

n = int(input("차원 입력: "))
x = []


print(f"{n}차원 벡터 {n}개를 입력하세요:")
for i in range(n):
    while True:
        try:
            vector_input = list(map(float, input(f"{i + 1}번째 벡터를 공백으로 구분하여 입력하세요: ").split()))
            if len(vector_input) == n:
                x.append(vector_input)
                break
            else:
                print(f"{n}차원 벡터를 입력하세요.")
        except ValueError:
            print("숫자를 입력하세요.")

# v에 입력받은 x 복사
v = [arr[:] for arr in x]

# 수행
for i in range(n):
    for j in range(i):
        for k in range(n):
            v[i][k] -= inner_product(x[i], v[j]) * v[j][k] / inner_product(v[j], v[j])

# 입력 받은 n차원 벡터들 출력
print("\n입력된 n차원 벡터들")
print(x)

# 직교 기저 출력
print("\n\nOrthogonal Basis-------\n")
print(v)