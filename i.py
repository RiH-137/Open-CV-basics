import cv2
import numpy as np



''' working with image '''

# img = cv2.imread('resources/img1.jpg')
# cv2.imshow("image", img)
# cv2.waitKey(0)                              ## delay in milliseconds
# cv2.destroyAllWindows()



''' Working with videos '''
'''since videos are nothing but a sequence of images,
 we can use the same code as above to work with videos'''

# frameWidth = 640
# frameHeight = 480

# cap1= cv2.VideoCapture('resources/vid1.mp4')
# cap = cv2.VideoCapture(0)  # 0 for default camera, 1 for external camera

# while True:
#     success, img = cap.read()
#     cv2.imshow("video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cv2.destroyAllWindows()



''' GreyScale '''
# path= 'resources/img1.jpg'
# img = cv2.imread(path)
# imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Grey Image", imgGrey)
# cv2.waitKey(0)                              ## delay in milliseconds

'''blur'''
# img_blur=cv2.GaussianBlur(imgGrey, (7,7), 0)
# cv2.imshow("Blur Image", img_blur)
# cv2.waitKey(0)                              ## delay in milliseconds


'''image edge detection'''
# img_canny=cv2.Canny(img, 100, 100)
# cv2.imshow("Canny Image", img_canny)
# cv2.waitKey(0)                              ## delay in milliseconds


'''dilating the image'''
# imgDialation = cv2.dilate(img_canny, (5,), iterations=1)
# cv2.imshow("Dilated Image", imgDialation)
# cv2.waitKey(0)                              ## delay in milliseconds

'''eroding the image'''
# imgEroded = cv2.erode(imgDialation, (5,), iterations=1)
# cv2.imshow("Eroded Image", imgEroded)
# cv2.waitKey(0)                              ## delay in milliseconds



'''resizing'''
# path= 'resources/img1.jpg'
# img= cv2.imread(path)
# print("original image size", img.shape) ## gives the shape of the image

# width, height = 300, 200
# imgResize = cv2.resize(img, (width, height))
# print('resized image size',imgResize.shape) ## gives the shape of the image
# cv2.imshow("Resized Image", imgResize)
# cv2.waitKey(0)                              ## delay in milliseconds
# cv2.destroyAllWindows()


'''cropping'''
# imgCropped = img[0:200, 200:500]
# cv2.imshow("Cropped Image", imgCropped)
# cv2.waitKey(0)                              ## delay in milliseconds
# cv2.destroyAllWindows()



'''black-image'''
img=np.zeros((512,512,3), np.uint8)
# print(img)
# print(img.shape)

# cv2.imshow("Black Image", img)
# cv2.waitKey(0)                              ## delay in milliseconds
# cv2.destroyAllWindows()

'''blue-image'''
# img[:]=255,0,0
# cv2.imshow("Blue Image", img)
# cv2.waitKey(0)                              ## delay in milliseconds

'''green-image'''
# img[:]=0,255,0
# cv2.imshow("Green Image", img)
# cv2.waitKey(0)                              ## delay in milliseconds

'''red-image'''

# img[:]=0,0,255
# cv2.imshow("Red Image", img)
# cv2.waitKey(0)                              ## delay in milliseconds
# cv2.destroyAllWindows

'''drawing shapes'''
# img[:]=255,0,0
# cv2.line(img, (0,0), (300,300), (0,255,0), 3)
# cv2.imshow("Line Image", img)
# cv2.waitKey(0)                              ## delay in milliseconds
# cv2.destroyAllWindows

'''rectangle'''
# cv2.rectangle(img, (0,0), (250,350), (0,0,255), 2)
# cv2.imshow("Rectangle Image", img)
# cv2.waitKey(0)                              ## delay in milliseconds
# cv2.destroyAllWindows

'''circle'''
# cv2.circle(img, (400,50), 30, (255,255,0), 5)
# cv2.imshow("Circle Image", img)
# cv2.waitKey(0)                              ## delay in milliseconds
# cv2.destroyAllWindows
# CV2.fillPoly(img, np.array([[]]), (0,0,255))  ## for polygon

'''text'''
# cv2.putText(img, "OpenCV", (300,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0), 1)
# cv2.imshow("Text Image", img)
# cv2.waitKey(0)                              ## delay in milliseconds
# cv2.destroyAllWindows

'''stacking images'''
# img = cv2.imread('resources/img1.jpg')
# img2 = cv2.imread('resources/img2.jpg')
# imgHor = np.hstack((img, img2))
# imgVer = np.vstack((img, img2))
# cv2.imshow("Horizontal", imgHor)
# cv2.imshow("Vertical", imgVer)
# cv2.waitKey(0)                              ## delay in milliseconds\
# cv2.destroyAllWindows

























