import cv2
import matplotlib.pyplot as plt

def main():
    
    Source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    
    imgpath = Source + "truck.tiff"
    
    img = cv2.imread(imgpath,0)
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    thresh1 = 127
    thresh = 0
    max_val = 255
    
    ret, out1 = cv2.threshold(img, thresh,max_val,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret, out2 = cv2.threshold(img, thresh,max_val,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    ret, out3 = cv2.threshold(img, thresh,max_val,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
    ret, out4= cv2.threshold(img, thresh,max_val,cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)
    ret, out5 = cv2.threshold(img, thresh,max_val,cv2.THRESH_TRUNC+cv2.THRESH_OTSU)
    
    ret1, out11 = cv2.threshold(img, thresh1,max_val,cv2.THRESH_BINARY)
    ret2, out22 = cv2.threshold(img, thresh1,max_val,cv2.THRESH_BINARY_INV)
    ret3, out33 = cv2.threshold(img, thresh1,max_val,cv2.THRESH_TOZERO)
    ret4, out44 = cv2.threshold(img, thresh1,max_val,cv2.THRESH_TOZERO_INV)
    ret5, out55 = cv2.threshold(img, thresh1,max_val,cv2.THRESH_TRUNC)
    

    
    output = [ img, out1, out2, out3, out4, out5]
    output1 = [ img, out11, out22, out33, out44, out55]
    
    titles = ['Actual Image1','Binary_Otsu','Binary_inv_Otsu','Zero_Otsu','Zero_inv_Otsu','Trunc_Otsu']
    titles1 = ['Actual Image','Binary','Binary_inv','Zero','Zero_inv','Trunc']
    
    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(output[i],cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()

    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(output1[i],cmap='gray')
        plt.title(titles1[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()
    
if __name__ == '__main__':
    main()