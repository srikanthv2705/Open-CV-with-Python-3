import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    imgpath = source+ "4.2.03.tiff"
    img = cv2.imread(imgpath,1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    Noise_Image = np.zeros(img.shape,np.uint8)
    
    prob = 0.2
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            r = np.random.random()
            if r < prob/2:
                Noise_Image[i][j] = [0,0,0]
            elif r < prob:
                Noise_Image[i][j] = [255,255,255]
            else:
                Noise_Image[i][j] = img[i][j]
                
    Noise_to_Normal = cv2.medianBlur(Noise_Image,5)
    output = [img,Noise_Image,Noise_to_Normal]
    titles = ["actual image",'Noise image','Noise to Normal']
    
    for i in range(3):
        plt.subplot(1,3,i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    
    plt.show()
    
if __name__ =='__main__':
    main()