import cv2

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Dataset\\New folder\\4.2.04.tiff"
    img = cv2.imread(source,1) 
    
    print(img) 
    print(type(img))
    print(img.dtype)
    print(img.shape)    #(512,512,3)
    print(img.ndim)         
    print(img.shape)   #(512*512*3)
    
    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
    
    
if __name__ == "__main__":
    main()
