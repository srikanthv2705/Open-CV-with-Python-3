import cv2
import matplotlib.pyplot as plt

def main():
    
    vid_cap = cv2.VideoCapture(0)
    
    if vid_cap.isOpened():
        ret, frame = vid_cap.read() # read() will return 2 variables ret i s return variable (True) Frame will give Ndim
        
        print(ret)
        print(frame)
    else:
        ret = False
    
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    plt.imshow(img)
    plt.title("Web cam Video Capture")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    vid_cap.release()
    
if __name__ == "__main__":
    main()
    