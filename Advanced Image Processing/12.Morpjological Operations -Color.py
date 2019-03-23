import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    impath = path  + "4.2.05.tiff"

    img = cv2.imread(impath, 1)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    k = cv2.getStructuringElement(cv2.MORPH_CROSS,(5, 5))
    
    erosion = cv2.erode(img, k, iterations = 5)
    
    dilation = cv2.dilate(img, k, iterations = 5)
    
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k)
    
    print(k)
    
    output = [img, erosion, dilation, gradient]
    
    titles = ['Original', 'Erosion', 'Dilation', 'Gradient']
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(output[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()  

if __name__ == "__main__":
    main()