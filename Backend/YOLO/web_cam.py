import cv2, os

cap = cv2.VideoCapture(0)

list_dir = os.listdir("D:\\Projects\\ISL using yolov8\\Backend\\YOLO\\data_source")

list_dir = [int(x[:-5]) for x in list_dir]

flag = True

while (True):
    success, image = cap.read()

    image = cv2.resize(image, (640, 640))

    #Convert an image from BGR to grayscale mode 
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    #Convert a grayscale image to black and white using binary thresholding 
    (thresh, BnW_image) = cv2.threshold(gray_image, 125, 255, cv2.THRESH_BINARY)

    if (flag == True):
        flag = False
        if len(list_dir) == 0:
            image_name = 1
        else:
            image_name = max(list_dir) + 1

    cv2.imwrite("D:\\Projects\\ISL using yolov8\\Backend\\YOLO\\data_source\\"+str(image_name)+".jpeg", BnW_image)

    image_name = image_name + 1
