#importing opencv2 module
import cv2

#defining main function

def main():
    
   #Getting image from Source using Opencv2
   
    Source = "C:\\Users\\Srikanth\\Desktop\\Dataset\\mandril_color.tif"
    img = cv2.imread(Source,0)  #0 indicates gray
    
    cv2.imshow("Madril",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
   
if __name__ == "__main__":
    main()