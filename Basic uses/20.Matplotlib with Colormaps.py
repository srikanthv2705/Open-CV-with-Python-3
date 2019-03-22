import cv2
import matplotlib.pyplot as plt

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Dataset\\New folder\\"
    image = source + "mandril_color.tif"
    img = cv2.imread(image,0) #Color image changing it as BW
    
    plt.imshow(img)
    plt.show()
    
    cv2.imshow("mandril",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
    