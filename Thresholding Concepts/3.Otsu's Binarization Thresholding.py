import cv2
import matplotlib.pyplot as plt

def main():
    
    Source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    
    imgpath = Source + "truck.tiff"
    
    img = cv2.imread(imgpath,0)
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    thresh = 0
    max_val = 255
    
    ret, out1 = cv2.threshold(img, thresh,max_val,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret, out2 = cv2.threshold(img, thresh,max_val,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    ret, out3 = cv2.threshold(img, thresh,max_val,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
    ret, out4= cv2.threshold(img, thresh,max_val,cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)
    ret, out5 = cv2.threshold(img, thresh,max_val,cv2.THRESH_TRUNC+cv2.THRESH_OTSU)
        
    output = [ img, out1, out2, out3, out4, out5]
    
    titles = ['Actual Image','Binary','Binary_inv','Zero','Zero_inv','Trunc']
    
    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(output[i],cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()
    
if __name__ == '__main__':
    main()