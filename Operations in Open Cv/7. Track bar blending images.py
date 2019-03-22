import cv2

def empty_function():
    pass

def main():
    
    path = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    
    img_path1 = path + "4.2.01.tiff"
    img_path2 = path + "4.2.03.tiff"
    
    img1 = cv2.imread(img_path1,1)
    img2 = cv2.imread(img_path2,1)
    
    output = cv2.addWeighted(img1,0.5,img2,0.5,0)
    
    windowname = "Transition Trackbar"
    cv2.namedWindow(windowname)
    
    cv2.createTrackbar('Alpha',windowname,0,10,empty_function)
    
    while True:
        cv2.imshow(windowname,output)
        
        if cv2.waitKey(1)==27:
            break
        alpha = cv2.getTrackbarPos('Alpha',windowname)/10
        beta = 1 - alpha
        
        output =cv2.addWeighted(img1,alpha,img2,beta,0)
        
        print(alpha,beta)
        
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
            