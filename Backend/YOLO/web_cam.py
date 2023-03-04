import cv2, os
import time

cap = cv2.VideoCapture(0)

list_dir = os.listdir("D:\\Projects\\ISL using yolov8\\Backend\\YOLO\\training_data\\words\\namaste")

list_dir = [int(x[:-5]) for x in list_dir]

flag = True
count = 0

start_point = (100, 100)

stop_point = (740, 740)

while (True):
    success, image = cap.read()

    image = cv2.rectangle(image, start_point, stop_point, 4)

    cv2.imshow("output", image)

    image = image[100:740, 100:740]

    cv2.imshow("output", image)

    if (flag == True):
        
        print ("position your hand")
        while (count != 10):

            time.sleep(2)
            print (count)
            count += 1

        flag = False
        if len(list_dir) == 0:
            image_name = 1
        else:
            image_name = max(list_dir) + 1
    
    image = cv2.resize(image, (128, 128))

    cv2.imwrite("D:\\Projects\\ISL using yolov8\\Backend\\YOLO\\training_data\\words\\namaste\\nam_"+str(image_name)+".jpeg", image)

    image_name = image_name + 1
    if image_name > 1000:
        break

    if cv2.waitKey(5) & 0xFF == 27:
        break
