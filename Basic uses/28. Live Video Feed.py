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
        
        cv2.imshow(windowName, frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()    

    vid_cap.release()

if __name__ == "__main__":
    main()