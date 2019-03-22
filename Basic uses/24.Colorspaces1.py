import cv2
import matplotlib.pyplot as plt

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Dataset\\New folder\\"
    image = source + "mandril_color.tif"
    img = cv2.imread(image,1) #Color image reading as it is
    
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
    plt.imshow(img)  
    plt.title("Color Image BGR")
    plt.xticks([]) #hiding x ticks
    plt.yticks([]) #hiding y ticks
    plt.show()
    
    plt.imshow(img1)  
    plt.title("Color Image RGB")
    plt.xticks([]) #hiding x ticks
    plt.yticks([]) #hiding y ticks
    plt.show()
    
if __name__ == "__main__":
    main()
    