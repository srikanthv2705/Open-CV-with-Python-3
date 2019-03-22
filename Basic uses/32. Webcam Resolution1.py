import cv2

def main():
    windowName = "Webcam Live Video"
    cv2.namedWindow(windowName)
    vid_cap = cv2.VideoCapture(0)
    
    print('Width of the image' + str(vid_cap.get(3))) #3 will give width
    print('Height of the image' + str(vid_cap.get(4))) #4 will give height
    
    vid_cap.set(3,5000) #Custom Resolution it is accepting only 1280 
    vid_cap.set(4,5000) #Custom Resolution it is accepting only 720
    
    print('Width of the image' + str(vid_cap.get(3)))
    print('Height of the image' + str(vid_cap.get(4)))
    
    if vid_cap.isOpened():
        ret, frame = vid_cap.read()
    else:
        ret = False

    while ret:
    
        ret, frame = vid_cap.read()
        
        output = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        cv2.imshow(windowName, frame)
        cv2.imshow("Gray", output)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()    

    vid_cap.release()

if __name__ == "__main__":
    main()