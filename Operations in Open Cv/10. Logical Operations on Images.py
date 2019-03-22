import cv2
import matplotlib.pyplot as plt

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    
    imgpath1 = source + "4.2.01.tiff"
    imgpath2 = source + "4.2.02.tiff"
    
    img1 = cv2.imread(imgpath1,1)
    img2 = cv2.imread(imgpath2,1)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    img3 = cv2.bitwise_and(img1,img2)
    img4 = cv2.bitwise_not(img1)    
    img5 = cv2.bitwise_or(img1,img2)
    img6 = cv2.bitwise_xor(img1,img2)
    
    titles = ['image1','image2','AND','Image Not','OR','XOR']
    images = [img1,img2,img3,img4,img5,img6]

    for i in range(6):
        plt.subplot(2, 3, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
        
if __name__ == '__main__':
    main()