import cv2

def main():
    
    vid_cap = cv2.VideoCapture(0)
    
    if vid_cap.isOpened():
        ret, frame = vid_cap.read() # read() will return 2 variables ret i s return variable (True) Frame will give Ndim
        
        print(ret)
        print(frame)
    else:
        ret = False
    
if __name__ == "__main__":
    main()
    