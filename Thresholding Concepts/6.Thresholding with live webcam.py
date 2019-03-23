import cv2

def main():
    
    vid_cap = cv2.VideoCapture(0)
    
    if vid_cap.isOpened():
        ret, frame = vid_cap.read()
    else:
        ret = False


    while ret:
    
        ret, frame = vid_cap.read()
        
        Thresh = 127
        max_val = 255
    
        ret, out1 = cv2.threshold(frame, Thresh, max_val, cv2.THRESH_BINARY)
        ret, out2 = cv2.threshold(frame, Thresh, max_val, cv2.THRESH_BINARY_INV)
        ret, out3 = cv2.threshold(frame, Thresh, max_val, cv2.THRESH_TOZERO)
        ret, out4 = cv2.threshold(frame, Thresh, max_val, cv2.THRESH_TOZERO_INV)
        ret, out5 = cv2.threshold(frame, Thresh, max_val, cv2.THRESH_TRUNC)
                
        cv2.imshow('Binary', out1)
        cv2.imshow('Binary_Inv', out2)
        cv2.imshow('Zero', out3)
        cv2.imshow('Zero_inv', out4)
        cv2.imshow('Trunc', out5)
        
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    vid_cap.release()

if __name__ == "__main__":
    main()