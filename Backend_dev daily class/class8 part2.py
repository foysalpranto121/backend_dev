import cv2
img = cv2.imread(r"C:\Users\moonp\OneDrive\Pictures\pranto.jpg")
if img is None:
    print("Error: Could not load image. Check if 'pranto.jpg' exists in the current directory.")
else:
    cv2.imshow("My picture", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    ## cv2.IMREAD_GRAYSCALE flag is converting the image to black and white 
    print(img.shape)
    print(len(img[0]))

    resize_image = cv2.resize(img, (500, 500), interpolation=cv2.INTER_AREA)
    cv2.imshow("My picture", resize_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

