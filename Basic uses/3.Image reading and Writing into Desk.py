import cv2

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Dataset\\New folder\\4.2.04.tiff"
    img = cv2.imread(source,0) # 0 indiactes the gray scale image in converts color image to gray scale
    
    output = "C:\\Users\\Srikanth\\Desktop\\Dataset\\New folder\\output\\4.2.04.jpg" #Changing into JPG format
        
    cv2.imshow('Lena', img)
    cv2.imwrite(output, img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
    
    
if __name__ == "__main__":
    main()
