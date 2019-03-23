import cv2
import matplotlib.pyplot as plt

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    imgpath = source+ "7.1.02.tiff"
    img = cv2.imread(imgpath,1)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    L1 = cv2.Canny(img,50,300, L2gradient = False)
    L2 = cv2.Canny(img,50,300, L2gradient = True)
    
    output = [img,L1,L2]
    title = ['Actual','L1','L2']
    
    
    for i in range(3):
        plt.subplot(1,3,i+1)
        plt.imshow(output[i],cmap='gray')
        plt.title(title[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
if __name__ =='__main__':
    main()