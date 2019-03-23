import cv2
import matplotlib.pyplot as plt

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    imgpath = source+ "5.1.11.tiff"
    img = cv2.imread(imgpath,1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    edgesx = cv2.Sobel(img,-1,dx= 3,dy= 0,ksize=13,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT) #KSIZE must be odd, shuldnot exceed 31
    edgesy = cv2.Sobel(img,-1,dx= 0,dy= 3,ksize=13,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)
    edges = edgesx+edgesy
    
    output = [img,edgesx,edgesy,edges]
    title = ['Actual','Edgesx','edgesy','edges']
    
    
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.imshow(output[i],cmap='gray')
        plt.title(title[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
if __name__ =='__main__':
    main()