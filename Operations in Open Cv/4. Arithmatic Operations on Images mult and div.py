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
    
    mult = img1*img2
    div = img1/img2
      
    title = ['Liquid Drop','madril','addition','Multiplication','Division']
    images = [img1,img2,mult,div]
    
    for i in range(4):
        plt.subplot(1,4,i+1) #row size 1st argument, column size 2nd argument, 3rd argument is position of image
        plt.imshow(images[i])
        plt.title(title[i])
        plt.xticks([])
        plt.yticks([])
    
    plt.show()
        
if __name__ == "__main__":
    main()
            