import numpy as np
import cv2
imageList1 = []
image_70701 = []
people = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
for i in range(0, 10) :
    imageList1.append(r"C:\Users\minsu\Documents\euge\dis\1\image " + people[i] + ".jpg")  #로컬 이미지 파일을 imageList1에 저장
for image_path1 in imageList1: 
    image_color1 = cv2.imread(image_path1)  #해당 경로의 이미지 불러오기
    image_gray1 = cv2.cvtColor(image_color1, cv2.COLOR_BGR2GRAY)  #이미지 흑백화하기
    image_70701.append(image_gray1[90:160, 90:160])  #이미지 70x70으로 자르기
A = np.vstack([image.reshape(1,-1) for image in image_70701])  #추출한 matrix를 1*4900으로 reshape하고 행방향으로 쌓기 
mean_vector = A.mean(axis=0).reshape(1,-1)  #전체 이미지의 mean_vector 계산
A = A - mean_vector  
U, S, V = np.linalg.svd(A)  #SVD Decomposition
number = 10
topid = sorted(range(len(S)), key = lambda i: S[i])[-int(number):]
eigenfaces = np.vstack([V[idx].reshape(1, -1) for idx in topid])
for i in range(0, 10) :
    eigenfaces_image = eigenfaces[i] - min(eigenfaces[i])
    eigenfaces_image = eigenfaces_image / max(eigenfaces_image) * 255
    eigenfaces_image = np.asarray(eigenfaces_image, dtype = np.uint8)
    cv2.imshow("1", eigenfaces_image.reshape(70,70))
    cv2.waitKey(0)
coefficients = np.dot(eigenfaces, A.T)
reconstructed_images = np.dot(coefficients.T, eigenfaces) + mean_vector
reconstructed_images = np.asarray(reconstructed_images, dtype = np.uint8)
for i in range(0, 10) :
    cv2.imshow("1", reconstructed_images[i].reshape(70,70))
    cv2.waitKey(0)
cv2.destroyAllWindows()

##################### Recognition TEST!! (A ~ J)

imageList2 = []
image_70702 = []
for i in range(1, 11) :
    imageList2.append(r"C:\Users\minsu\Documents\euge\dis\2\image (" + str(i) + ").jpg")  #로컬 이미지 파일 경로를 imageList2에 저장
for image_path2 in imageList2:
    image_color2 = cv2.imread(image_path2)  #해당 경로의 이미지 불러오기
    image_gray2 = cv2.cvtColor(image_color2, cv2.COLOR_BGR2GRAY)  #이미지 흑백화하기
    image_70702.append(image_gray2[90:160, 90:160])  #이미지 70x70으로 자르기

print(mean_vector)

for i in range(0, 10) :
    print("who is image(" + str(i+1) + ")??")
    coefficients_test = np.dot(eigenfaces, (image_70702[i].reshape(-1,1) - mean_vector.T)).T  #전에 구했던 eigenfaces로 test이미지의 coefficient구하기
    minn = 2200000000
    reconstructed_imagesx = np.dot(coefficients_test, eigenfaces) + mean_vector  #test이미지의 coefficient와 eigenfaces를 선형결합 + mean_vector
    reconstructed_imagesx = np.asarray(reconstructed_imagesx, dtype = np.uint8)  #실수 -> 정수
    cv2.imshow("1", reconstructed_imagesx.reshape(70,70))  #이미지 출력
    cv2.waitKey(0)
    for j in range(0,10) :
        distance = np.linalg.norm(coefficients.T[j] - coefficients_test)  #아까 등록했던 10개 이미지의 coefficients와 test이미지의 coefficient 거리 계산
        if distance < minn :  #거리의 최솟값 구하기
            minn = distance
            idx = j
    print("Answer : " + people[idx])