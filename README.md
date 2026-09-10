# Eigenface 얼굴 표현과 인식

얼굴 이미지를 벡터로 바꾸고 SVD 기저에 투영해 재구성하거나 가까운 얼굴을 찾는 선형대수 실습입니다. 픽셀 전체를 그대로 비교하는 대신 얼굴 간 차이를 적은 수의 계수로 표현하는 과정을 구현했습니다.

## 사용 기술

Python, NumPy, OpenCV를 사용합니다. NumPy로 행렬·SVD를 계산하고 OpenCV로 이미지를 읽고 결과를 표시합니다.

## 데이터와 모델 구조

참조 얼굴 A–J와 질의 이미지를 입력으로 받습니다. Grayscale로 변환하고 70×70 영역을 사용한 뒤, 참조 행렬의 평균 얼굴을 빼서 중심화합니다.

```text
참조 얼굴 → 평균 중심화 → SVD → eigenface 기저
질의 얼굴 → 같은 평균 제거 → 투영계수 → 거리 비교 / 재구성
```

참조 이미지에서 얻은 기저를 질의에도 적용해야 두 계수의 거리를 비교할 수 있습니다. 별도의 신경망이나 인물별 확률 보정은 사용하지 않습니다.

## 실습 과정

벡터 연산에서 시작해 [Eigenface_Coefficients.py](Eigenface_Coefficients.py)에서 기저와 재구성을 다뤘습니다. 기저를 줄이면 세부정보가 사라지는 대신 표현이 단순해지는 관계를 확인하는 단계입니다.

이후 [Eigenface_Recognition.py](Eigenface_Recognition.py)에서 질의를 같은 공간에 투영하고 계수가 가까운 참조 얼굴을 찾도록 연결했습니다. 원본 픽셀의 유사성과 저차원 표현의 유사성을 구분하는 것이 핵심입니다.

## 실행

```powershell
pip install -r requirements.txt
$env:EIGENFACE_DATA_DIR = "data/local"
python Eigenface_Recognition.py
```

데이터 경로 아래에 `dis/1/image A.jpg`부터 J까지, `dis/2/image (1).jpg`부터 10까지 준비합니다. 결과는 GUI 창에 표시합니다.

## 한계

고정 crop이므로 얼굴 위치·정렬·조명 변화에 민감합니다. 미등록 인물을 안전하게 거절하는 본인 인증 시스템은 아닙니다. 참조·질의가 독립적인 평가셋의 인식률은 별도로 다뤄야 합니다. 얼굴 사진은 동의와 사용권을 확보한 자료만 사용합니다.

[알고리즘 노트](docs/implementation.md) · [출처](ATTRIBUTION.md)
