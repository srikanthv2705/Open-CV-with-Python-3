import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    imgpath = source+ "4.2.07.tiff"
    img = cv2.imread(imgpath,1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    k = np.array(([0,0,0],[0,1,0],[0,0,0]),np.float32) #k is Kernel
    k1 = np.array(([-1,-1,-1],[-1,8,-1],[-1,-1,-1]),np.float32)
    k2 = np.array(np.ones((11, 11), np.float32))/121
    k3 = np.array(([0,-1,0],[-1,5,-1],[0,-1,0]),np.float32)
    k4 = np.array(([1,4,6,4,1],[4,16,24,16,4],[6,24,-476,24,6],[4,16,24,16,4],[1,4,6,4,1]),np.float32)/-256
    
    print(k)
    print(k1)
    print(k2)
    print(k3)
    print(k4)
    
    output = cv2.filter2D(img,-1,k) #-1 is depth of output image
    output1 = cv2.filter2D(img,-1,k1)
    output2 = cv2.filter2D(img,-1,k2)
    output3 = cv2.filter2D(img,-1,k3)
    output4 = cv2.filter2D(img,-1,k4)
    
    plt.subplot(2,3,1)
    plt.imshow(img)
    plt.title("Actual Image")
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2,3,2)
    plt.imshow(output)
    plt.title("Identity image")
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2,3,3)
    plt.imshow(output1)
    plt.title("Edge Detection image")
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2,3,4)
    plt.imshow(output2)
    plt.title("Blur image")
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2,3,5)
    plt.imshow(output3)
    plt.title("Sharpen image")
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2,3,6)
    plt.imshow(output4)
    plt.title("un Sharp masking image")
    plt.xticks([])
    plt.yticks([])

    
    plt.show()
    
if __name__ =='__main__':
    main()