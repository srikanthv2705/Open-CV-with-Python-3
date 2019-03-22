import cv2
import time

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    
    imgpath1 = source + "4.2.01.tiff"
    
    img = cv2.imread(imgpath1,1)
    
    rows, columns, channels = img.shape
    
    angle = 360
    
    while True:
        
        if angle == 0:
            angle = 360 #Rotating Clockwise Direction
        
        R = cv2.getRotationMatrix2D((columns/2, rows/2), angle, 0.5)
        
        print(R)
    
        output = cv2.warpAffine(img, R, (columns, rows))
    
    
        cv2.imshow('Rotating Image', output)
        angle -= 1
        time.sleep(0.01)
        
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyWindow('Rotating Image')

if __name__ == "__main__":
    main()