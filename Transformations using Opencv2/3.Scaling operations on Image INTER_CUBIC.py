import cv2

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    
    imgpath1 = source + "4.2.01.tiff"
    
    img1 = cv2.imread(imgpath1,1)
    
    output = cv2.resize(img1,None,fx = 0.5,fy = 0.5,interpolation = cv2.INTER_AREA) #Shrinking image
        
    cv2.imshow('Output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    
if __name__ == '__main__':
    main()