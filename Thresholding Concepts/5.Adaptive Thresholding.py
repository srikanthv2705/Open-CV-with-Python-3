import cv2
import matplotlib.pyplot as plt

def main():
    
    Source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    
    imgpath = Source + "4.1.05.tiff"
    
    img = cv2.imread(imgpath,0)
    
    block_size = 513
    constant = 2
    T1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,block_size,constant)
    T2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,block_size,constant)
    
    output = [img,T1,T2]
    
    titles = ['Actual Image','Gaussian Adaptive','Mean Adaptive']
    
    for i in range(3):
        plt.subplot(1,3,i+1)
        plt.imshow(output[i],cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()

if __name__ == '__main__':
    main()