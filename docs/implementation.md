# Linear algebra and validation
X는 한 행이 하나의 crop인 행렬입니다. 평균 μ를 뺀 Xc=UΣVᵀ에서 기저 E를 선택해 C=Xc Eᵀ, 복원 Xhat=C E+μ를 계산합니다. Recognition은 같은 μ/E로 query를 투영한 뒤 coefficient 거리로 참조 영상을 고릅니다.
tests/test_core.py는 원본 Recognition source의 수치 assignment를 추출해 synthetic crop으로 실행합니다. GUI/파일 loader/실제 얼굴 일반화는 검증하지 않습니다. 행렬 자체를 검사하는 테스트를 실제 인식률로 표시하지 않습니다.

