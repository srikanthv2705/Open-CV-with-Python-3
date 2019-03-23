import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    imgpath = source+ "4.2.02.tiff"
    img = cv2.imread(imgpath,1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    rows, columns, channels = img.shape
    
    prob = 0.15 #probability of Noise
    
    output1 = img
    output = np.zeros(img.shape,np.uint8) #Place Holder for output image
    
    for i in range(rows):
        for j in range(columns):
            r = np.random.random()
            if r < prob/2:
                #Pepper Sprinkle
                output[i][j] = [0,0,0]
            elif r < prob :
                #Salt Sprinkle
                output[i][j] = [255,255,255]
            else:
                output[i][j] = img[i][j]
    
    
    print(output)
    print(output1)
    
    plt.imshow(output1)
    plt.title("Actual Image")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    plt.imshow(output)
    plt.title("Image with Noise")
    plt.xticks([])
    plt.yticks([])
    plt.show()
if __name__ =='__main__':
    main()