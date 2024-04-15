import numpy as np
import cv2
imageList = []
image_7070 = []

#1. Image 불러오기
for i in range(1, 3001) :
    imageList.append(r"C:\Users\minsu\Documents\euge\lfw_funneled\image (" + str(i) + ").jpg") #로컬 이미지 파일을 imageList에 저장

#2. Image 가공
for image_path in imageList: 
    image_color = cv2.imread(image_path)  #해당 경로의 이미지 불러오기
    image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)  #이미지 흑백화하기
    image_7070.append(image_gray[90:160, 90:160])  #이미지 70x70으로 자르기

A = np.vstack([image.reshape(1,-1) for image in image_7070])  #추출한 matrix를 1*4900으로 reshape하고 행방향으로 쌓기 
mean_vector = A.mean(axis=0).reshape(1, -1)  #전체 이미지의 mean_vector 계산
A = A - mean_vector

#3. SVD Decomposition
U, S, V = np.linalg.svd(A)  #SVD Decomposition


number = 50  #선택할 eigenvalue의 개수 : 임의의 숫자 대입 후 결과 확인!!


topid = sorted(range(len(S)), key = lambda i: S[i])[-int(number):]  #eigenvalue를 내림차순으로 정렬했을때 큰 순서대로 number개 만큼 그 index를 topid에 저장
eigenfaces = np.vstack([V[idx].reshape(1, -1) for idx in topid])  #선택한 eigenvalue에 대응하는 eigenvector를 열방향으로 쌓기

#4. EigenFaces 출력
for i in range(0, number) :
    eigenfaces_image = eigenfaces[i] - min(eigenfaces[i])  #-1 ~ 1 의값을 가지는 eigenfaces를 0 ~ 2의 값을 가지도록 eigenface의 최솟값을 더해줌
    eigenfaces_image = eigenfaces_image / max(eigenfaces_image) * 255  #0~255의 값을 가지되 최댓값이 255에 근접한 값을 가지도록 255/max 를 곱해줌
    eigenfaces_image = np.asarray(eigenfaces_image, dtype = np.uint8)  #정수로 변환
    cv2.imshow("1", eigenfaces_image.reshape(70,70))  #70x70 으로 변환하여 출력
    cv2.waitKey(0)
cv2.destroyAllWindows()

#5. Coefficients 계산 및 Image 재구성
coefficients = np.dot(eigenfaces, A.T)  #eigenface와 A.T를 행렬곱하여 coefficient 계산
reconstructed_images = np.dot(coefficients.T, eigenfaces) + mean_vector  #coefficients 와 eigenfaces를 선형결합하고 mean_vector을 더해서 재구성된 이미지 matrix 만들기
reconstructed_images = np.asarray(reconstructed_images, dtype = np.uint8)  #이미지 matrix를 실수 -> 정수로 변환
for i in range(0, 5):
    cv2.imshow("recontructed_images", reconstructed_images[i].reshape(70,70))  #이미지 matirx 중 특정한 image vector를 70x70 matrix로 변환하여 출력
    cv2.waitKey(0)
cv2.destroyAllWindows()