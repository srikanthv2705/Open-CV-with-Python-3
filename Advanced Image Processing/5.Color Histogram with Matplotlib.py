import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    impath = path  + "4.2.07.tiff"
    img = cv2.imread(impath, 1)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    R, G, B = cv2.split(img)
    
    plt.subplot(3, 1, 1)
    plt.hist(R.ravel(), 256, [0, 255])
    plt.title('Red Channel Histogram')
    plt.xlim(left=0, right=256)
    plt.show()
    
    plt.subplot(3, 1, 2)
    plt.hist(G.ravel(), 256, [0, 255])
    plt.title('Green Channel Histogram')
    plt.xlim(left=0, right=256)
    plt.show()
    
    plt.subplot(3, 1, 3)
    plt.hist(B.ravel(), 256, [0, 255])
    plt.title('Blue Channel Histogram')
    plt.xlim(left=0, right=256)
    plt.show()

if __name__ == "__main__":
    main()