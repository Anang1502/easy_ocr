import cv2 as cv
import sys
import easyocr
reader = easyocr.Reader(['en'])

# try:
#     img = cv.imread("starry_night.jpg")
#     if img is None:
#         sys.exit("Could not read the image.")
#     cv.imshow("Display window", img)
#     k = cv.waitKey(0)
#     if k == ord("s"):
#         cv.imwrite("starry_night.png", img)
# except Exception as err:
#     print(err)


try:
    reader = easyocr.Reader(['en'])
    img = cv.imread("text_image.jpg")
    if img is None:
        sys.exit("Could not read the image.")
    cv.imshow("Display window", img)
    cv.waitKey(10000)
    cv.destroyAllWindows()
    # if k == ord("s"):
    #     cv.imwrite("starry_night.png", img)
except Exception as err:
    print(err)