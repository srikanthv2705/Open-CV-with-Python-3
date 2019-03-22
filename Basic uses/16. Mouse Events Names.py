import cv2

def main():
    
    Mouse_events = [i for i in dir(cv2) if 'EVENT' in i]  #it will fetch 'EVENT' Name from CV2 Directory
    print(Mouse_events)
    
if __name__ == "__main__":
    main()