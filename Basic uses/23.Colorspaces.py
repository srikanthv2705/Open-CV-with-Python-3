import cv2
import matplotlib.pyplot as plt

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Dataset\\New folder\\"
    image = source + "mandril_color.tif"
    img = cv2.imread(image,1) #Color image reading as it is
    
    plt.imshow(img)  
    plt.title("Default color map")
    plt.xticks([]) #hiding x ticks
    plt.yticks([]) #hiding y ticks
    plt.show()
    
if __name__ == "__main__":
    main()
    