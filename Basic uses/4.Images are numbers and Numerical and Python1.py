import cv2

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Dataset\\New folder\\4.2.04.tiff"
    img = cv2.imread(source,1) 
    
    print(img) 
    
    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
    
    
if __name__ == "__main__":
    main()
