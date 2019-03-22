import cv2
import matplotlib.pyplot as plt

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Dataset\\New folder\\"
    image = source + "mandril_color.tif"
    img = cv2.imread(image,0) #Color image changing it as BW
    
    plt.imshow(img,cmap='gray')   #in Matplot Lib colors are read as RGB, using cmap we can convert image as required
    plt.show()
    
if __name__ == "__main__":
    main()
    