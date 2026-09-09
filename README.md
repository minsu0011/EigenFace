# Eigenface Recognition
얼굴 영상을 평균 중심화한 뒤 SVD 기저에 투영하고 계수 공간에서 최근접 얼굴을 찾는 선형대수 실습입니다. 딥러닝 얼굴 인식이나 서비스용 본인 인증 모델이 아닙니다.

## 알고리즘
영상 → grayscale → 70×70 고정 crop → 행렬 평균 제거 → SVD → 상위 eigenface → 투영계수 → 재구성/거리 비교 순서입니다. `Eigenface_Coefficients.py`는 기저·재구성을, `Eigenface_Recognition.py`는 A–J 참조 영상과 질의 영상 비교를 수행합니다. `Vector_Operation_Practice*`는 선행 벡터 연산 연습입니다.

## 실행
`pip install -r requirements.txt` 후 `EIGENFACE_DATA_DIR`를 로컬 데이터 디렉터리로 지정하세요(기본 `data/local`). 참조 파일은 `dis/1/image A.jpg`부터 J까지, 질의는 `dis/2/image (1).jpg`부터 10까지입니다. `python Eigenface_Recognition.py`는 GUI 창을 엽니다.

## 결과와 한계
확인한 범위는 구문 및 작은 합성 행렬의 SVD 핵심 계산을 확인합니다. 실제 얼굴 정확도를 재측정하지 않으며 특정 accuracy를 주장하지 않습니다. 고정 crop과 조명·정렬 변화에 민감하고, 대규모 full SVD는 메모리 비용이 큽니다. 학습 이미지와 질의의 독립성도 사용자가 관리해야 합니다.

LFW·개인 얼굴 사진은 재배포하지 않습니다. 사진별 동의와 사용권은 별도 확보해야 합니다. [구현/검증](docs/implementation.md)을 참고하세요.
