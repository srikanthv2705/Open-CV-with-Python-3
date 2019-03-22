import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    
    imgpath1 = source + "4.2.01.tiff"
    
    img = cv2.imread(imgpath1,1)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    rows, columns, channels = img.shape
    
    T = np.float32([[1,0,50],[0,1,-50]])
    
    print(T)
    
    output = cv2.warpAffine(img,T, (columns,rows))
        
    plt.imshow(output)
    plt.title("Shifted image")
    plt.show()
    
if __name__ == '__main__':
    main()