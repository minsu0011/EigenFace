# Eigenface

얼굴 이미지를 SVD 기저에 투영해 재구성하고 가까운 참조 얼굴을 찾는 선형대수 실습입니다. Python, NumPy와 OpenCV를 사용합니다.

## 처리 과정

```text
참조 얼굴 → grayscale / crop → 평균 중심화 → SVD 기저
질의 얼굴 → 같은 평균 제거 → 투영계수 → 거리 비교 / 재구성
```

- [Eigenface_Coefficients.py](Eigenface_Coefficients.py): 기저·투영계수·재구성
- [Eigenface_Recognition.py](Eigenface_Recognition.py): 질의와 참조 얼굴의 계수 비교

## 실행

```powershell
pip install -r requirements.txt
$env:EIGENFACE_DATA_DIR = "data/local"
python Eigenface_Recognition.py
```

`dis/1/image A.jpg`부터 J까지, `dis/2/image (1).jpg`부터 10까지 준비합니다. 결과는 GUI 창에 표시합니다.

70×70 고정 crop을 사용하므로 정렬·조명 변화에 민감합니다. 사용권을 확보한 이미지를 사용하세요.

[알고리즘 노트](docs/implementation.md) · [출처](ATTRIBUTION.md)
