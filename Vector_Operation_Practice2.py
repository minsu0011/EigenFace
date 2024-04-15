import random
from decimal import Decimal, getcontext
getcontext().prec = 7


# 두 벡터의 규격화
def normalize(vector):
    magnitude = float((sum(Decimal(str(x)) * Decimal(str(x)) for x in vector))) ** 0.5
    result = []
    for x in vector:
        result.append(float(Decimal(str(x)) / Decimal(str(magnitude))))
    return result


# 직교성 확인 함수
def check_orthogonality(vectors):
    inner_products = []
    for i, v1 in enumerate(vectors):
        for j, v2 in enumerate(vectors):
            if i != j:
                dot_product = inner_product(v1, v2)
                if dot_product <= 0.0001 : # 부동소수점 오차 보정
                    inner_products.append(0)
                else :
                    inner_products.append(dot_product)
    average_inner_product = sum(inner_products) / len(inner_products)
    return average_inner_product


# 두 벡터 내적 함수
def inner_product(x, y):
    res = 0
    for i in range(len(x)):
        res = float(Decimal(str(res)) + Decimal(str(x[i])) * Decimal(str(y[i])))
    return res


# 벡터 스칼라 곱 함수
def scalar_multiply(scalar, vector):
    return [float(Decimal(str(scalar)) * Decimal(str(x))) for x in vector]


# 벡터 덧셈 함수
def vector_add(v1, v2):
    return [float(Decimal(str(x)) + Decimal(str(y))) for x, y in zip(v1, v2)]


# 벡터 뺄셈 함수
def vector_subtract(v1, v2):
    return [float(Decimal(str(x)) - Decimal(str(y))) for x, y in zip(v1, v2)]


#입력
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
basis_vectors = []

# orthonogonal basis vector + normalize 수행
for i in range(n):
    for j in range(i):
        if inner_product(v[j], v[j]) != 0:
            for k in range(n):
                v[i][k] = float(Decimal(str(v[i][k])) - Decimal(str(inner_product(x[i], v[j]))) * Decimal(str(v[j][k])) / Decimal(str(inner_product(v[j], v[j]))))
    basis_vectors.append(normalize(v[i]))

# 입력 받은 n차원 벡터들 출력
print("\n입력된 n차원 벡터들")
print(x)

# orthogonal basis vector 출력
print("\n\nOrthogonal Basis-------\n")
print(v)

# orthonormal basis vector 출력
print("\n\nOrthonormal Basis-------\n")
print(basis_vectors)

# 선형결합 계산
for i in range(3):  # 임의의 벡터 3개 생성 및 직교성 확인
    y = [random.randint(0, 10) for _ in range(n)]  # 임의의 n차원 벡터 생성
    c = [float(Decimal(str(inner_product(y, q))) / Decimal(str(inner_product(q, q)))) for q in basis_vectors]  # basis vector와의 내적을 통해 C(i) 구하기
    y_ = [0 for k in range(n)]
    for i in range(n): # c를 이용한 선형결합 결과 
        t = scalar_multiply(c[i],basis_vectors[i])
        y_ = vector_add(t, y_)
    print(f"\n임의의 {n}차원 벡터 Y :")
    print(y)
    print(f"\n계수 c : ")
    print(c)
    print("\n선형결합하여 만들어진 벡터 :")
    print(y_)
    print("\n오차 :")
    print(vector_subtract(y_, y))

# 직교성 확인
check_average = check_orthogonality(basis_vectors)
print("\nOrthonormality of basis vectors =", check_average)