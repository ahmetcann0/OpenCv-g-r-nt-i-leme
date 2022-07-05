from gettext import npgettext
from cv2 import destroyAllWindows
import numpy as np
import cv2


img_first = cv2.imread("dolu.jpg")
opening=cv2.cvtColor(img_first,cv2.COLOR_BGR2GRAY)
#Filtreleme işlemleri
kernel = np.ones((11, 11), np.uint8)

meanFilter = cv2.blur(opening,(15,15))
ret,thresh1=cv2.threshold(meanFilter,121,255,cv2.THRESH_BINARY) 
opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN,kernel,iterations=1)

#Contour filling
des = cv2.bitwise_not(opening)
contour,hier = cv2.findContours(des,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contour:
    cv2.drawContours(des,[cnt],0,255,-1)

opening = cv2.bitwise_not(des)


# Find the contours
contours, _ = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# For each contour approximate the curve and
# detect the shapes.
for cnt in contours:
    epsilon = 0.01*cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    cv2.drawContours(opening, [approx], 0, (0), 4)
    # Position for writing text
    x,y = approx[0][0]
 
    if len(approx) == 3:
        cv2.putText(opening, "Triangle", (x,y+150), cv2.FONT_HERSHEY_COMPLEX, 5, 0,3)
    elif len(approx) == 4:
      xCoo,yCoo,w,h = cv2.boundingRect(approx)
      if abs(w-h) <= 4: # 3 fark var karenin kenarları arasında
            cv2.putText(opening, "Square", (x, y-50), cv2.FONT_HERSHEY_COMPLEX, 5, 0,3)
      else:    
           cv2.putText(opening, "Rectangle", (x, y-40), cv2.FONT_HERSHEY_COMPLEX, 5, 0,3)
    elif len(approx) == 5:
        cv2.putText(opening, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 5, 0,3)
    elif   10 < len(approx) < 14:
        cv2.putText(opening, "Ellipse", (x, y-100), cv2.FONT_HERSHEY_COMPLEX, 5, 0,3) #14
    elif   len(approx) == 10:
        cv2.putText(opening, "Star", (x-80,y+160), cv2.FONT_HERSHEY_COMPLEX , 5, 0 ,3)
    else:
        cv2.putText(opening, "Circle", (x, y-50), cv2.FONT_HERSHEY_COMPLEX, 5, 0,3)



cv2.imshow("orjinal görüntü",img_first)
cv2.imshow("final",opening)


cv2.waitKey(0)
destroyAllWindows()
