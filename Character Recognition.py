import cv2
import pytesseract as pyt              #pytesseract is used to work with Tesseract-OCR

pyt.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('test_img.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)              #changing image from BGR to RGB colorspace

#Detecting Words
img_h, img_w, _ = img.shape
boxes = pyt.image_to_data(img)                          #save details of the image in string "boxes"
# print(boxes)
# The structure of boxes is like:
# [   0          1           2           3           4          5         6       7       8        9        10       11 ]
# ['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height', 'conf', 'text']
for i, a in enumerate(boxes.splitlines()):
    if i != 0:                                 #the first row of boxes is ignored i.e the heading row
        a = a.split()                                   
        print(a)
        if len(a) == 12:                       #only these rows contain the actual words present in the image
            x, y, w, h = int(a[6]), int(a[7]), int(a[8]), int(a[9])     #saving coordinates and width and height for the rectangles
            cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)             #creating rectangle around words
            cv2.putText(img, a[11], (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)      #include corresponding texts

cv2.imshow('Result', img)             #showing the results
cv2.waitKey(0)
if  ord('q'):
    cv2.destroyAllWindows()
