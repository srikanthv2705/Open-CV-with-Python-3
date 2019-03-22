import cv2

def main():
    windowName = "Video Playback"
    cv2.namedWindow(windowName)
    filename = "C:\\Users\\Srikanth\\Desktop\\Dataset\\New folder\\output\\webcam_recording.avi"
    vid_cap = cv2.VideoCapture(filename)
    
    ret = True
    
    while ret:
        if vid_cap.isOpened():  
            ret, frame = vid_cap.read()

        if ret:
            cv2.imshow(windowName,frame)
            if cv2.waitKey(33) == 27: #fps rate should match with Video play back rate
                break
        else:
            break

    cv2.destroyAllWindows()    
    vid_cap.release()

if __name__ == "__main__":
    main()