import cv2
import matplotlib.pyplot as plt

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Dataset\\New folder\\"
    image = source + "mandril_color.tif"
    img = cv2.imread(image,0) #Color image changing it as BW
    
    plt.imshow(img,cmap='gray')   #in Matplot Lib colors are read as RGB, using cmap we can convert image as required
    plt.title("Gray Scale Color map") #Displaying title
    plt.xticks([]) #hiding x ticks
    plt.yticks([]) #hiding y ticks
    plt.show()
    
    plt.imshow(img)  
    plt.title("Default map")
    plt.xticks([]) #hiding x ticks
    plt.yticks([]) #hiding y ticks
    plt.show()
    
    plt.imshow(img,cmap="Reds")  
    plt.title("Red Color map")
    plt.xticks([]) #hiding x ticks
    plt.yticks([]) #hiding y ticks
    plt.show()

    
if __name__ == "__main__":
    main()
    