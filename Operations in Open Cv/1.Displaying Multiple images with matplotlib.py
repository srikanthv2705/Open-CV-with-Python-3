import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    
    img_path1 = path + "4.2.01.tiff"
    img_path2 = path + "4.2.03.tiff"
    
    img1 = cv2.imread(img_path1,1)
    img2 = cv2.imread(img_path2,1)
    
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    
    plt.subplot(1,2,1) #row size 1st argument, column size 2nd argument, 3rd argument is position of image
    plt.imshow(img1)
    plt.title("Liquid Drop")
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(1,2,2)
    plt.imshow(img2)
    plt.title("Mandril")
    plt.xticks([])
    plt.yticks([])
    
    plt.show()
        
if __name__ == "__main__":
    main()
            