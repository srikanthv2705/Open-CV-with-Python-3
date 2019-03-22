import cv2

def main():
    windowName = "Webcam Live Video"
    cv2.namedWindow(windowName)
    vid_cap = cv2.VideoCapture(0)
    
    filename = "C:\\Users\\Srikanth\\Desktop\\Dataset\\New folder\\output\\webcam_recording.avi"
    codec = cv2.VideoWriter_fourcc('X','V','I','D') #ither popular encoding formats are WMV2,WMV1,MJPG,DIVX,XVID,H264 these are four character codes
    
    framerate = 30   #smooth frame rate
    resolution = (640,480) #lower resolution the frame is smoother
    
    videofile_output = cv2.VideoWriter(filename,codec,framerate,resolution)
    
    
    if vid_cap.isOpened():
        ret, frame = vid_cap.read()
    else:
        ret = False

    while ret:
    
        ret, frame = vid_cap.read()
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        videofile_output.write(frame)
        
        cv2.imshow(windowName, frame)
    
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()    
    videofile_output.release()
    vid_cap.release()

if __name__ == "__main__":
    main()