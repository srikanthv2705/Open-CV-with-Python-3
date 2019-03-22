import cv2

def main():
    
    i = 0
    for filename in dir(cv2):
        if filename.startswith('COLOR_'):
            print(filename)
            i += 1
            
    print('There are ' + str((i+1)) + ' color conversion flags in opencv directory')
    
if __name__ == "__main__":
    main()
    