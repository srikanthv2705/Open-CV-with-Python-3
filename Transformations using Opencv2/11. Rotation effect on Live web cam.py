import cv2
import time

def main():
    
    windowName = "Web cam Video"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    filename = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\output\\webcam_recording_Rotating.avi"
    codec = cv2.VideoWriter_fourcc('X','V','I','D')
    
    framerate = 30   
    resolution = (640,480)
    
    videofile_output = cv2.VideoWriter(filename,codec,framerate,resolution)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    rows, columns, channels = frame.shape   
    angle = 0
#    scale = 0.1
    scale = 0.7     
    
    while True:
        
        ret, frame = cap.read()
        
        if angle == 360:
            angle = 0

 #       angle = 0 
       
 #       if scale < 2:
 #           scale = scale + 0.1
        
 #       if scale >= 2:
 #           scale = 0.1
            
        print(scale)
        
        R = cv2.getRotationMatrix2D((columns/2, rows/2), angle, scale)
        
        print(R)
    
        output = cv2.warpAffine(frame, R, (columns, rows))
    
        videofile_output.write(output)
        
        cv2.imshow(windowName, output)
    
        angle += 1
        time.sleep(0.01)
        
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyWindow(windowName)


    cv2.destroyAllWindows()    
 
    videofile_output.release()
    
    cap.release()
  


if __name__ == "__main__":
    main()