#importing the opencv module
import cv2
# using imread('path') and 1 denotes read as  color image
# Mode flag (1): Determines how the image is read:
# 1 (default): Read in color (ignoring alpha channel if present).
# 0: Read as a grayscale image.
# -1: Read the image as-is, including the alpha channel.
img = cv2.imread(r'C:\Users\njamil\Desktop\Nabeel RND\ren-data-gerator\resource\passport.png', 1)
if img is None:
    print("Error: Image not found or could not be loaded.")
else:
    #This is using for display the image
    cv2.imshow('image', img)
    cv2.waitKey()
    # This is necessary to be required so that the image doesn't close immediately.
    #It will run continuously until the key press.
    cv2.destroyAllWindows()