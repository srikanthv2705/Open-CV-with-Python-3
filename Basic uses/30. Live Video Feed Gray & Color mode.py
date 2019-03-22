import cv2

def main():
    windowName = "Webcam Live Video"
    cv2.namedWindow(windowName)
    vid_cap = cv2.VideoCapture(0)
    
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