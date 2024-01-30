red = int(input("Enter Red Value:))
green = int(input("Enter Green Value:))
blue — int(input("Enter Blue Value:))
if and red<=255) and and green<=255) and (blue>=Ø and blue<=255)):
hexred — redX16
hexred2 — int(red/16)X16
hexgreen = greenX16
hexgreen2 =int(green/16)X16
hexblue blueX16
hexb1ue2 =
print( 'Hex Code:
print(t[hexred2]+t[hexred]+t[hexgreen2]+t[hexgreen]+t[hexb1ue2]+t[hexb1ue] )
else:
print("lnput is Invalid. Input Domain is 0 to 255. ")
hex_string = input( Enter the Hex Color Code
hexred =
hexgreen = hex_string[2:4J
hexblue = hex_string[4:6]
end_length = len(hexred) * 2
= int(hexred, 16)
hex as int
hex_as_binary = bin(hex_as_int)
padded_binary = J .zfill(end_length)
+ str(int(padded_binary,2)))
Value is:
end_length = len(hexgreen) * 2
= int(hexgreen, 16)
hex as int
hex as_binary = bin(hex as_int)
padded _ binary = J .zfill(end_length)
+ str(int(padded_binary,2)))
print("Green Value is:
end_length = len(hexblue) * 2
_ int = int(hexblue, 16)
hex as
_ binary = bin(hex_as_int)
hex as
padded_binary = ] .zfill(end_length)
+ str(int(padded binary, 2)) )
rint
"Green Value is: "
from PIL import Image
image = Image. \samp1eØ2.jpg")
pixelmap = image . load()
new image = Image.
pixelsNew = new image. load()
for i in range(new_image.size[Ø]):
for j in range(new_image.size[l]):
r, g, b = image.getpixel((i,j))
new_val= int((r+g+b)/3)
pixelsNew[i,j]
= 255)
new image. show()
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
img =
kernel
= np.ones((5,5),np.f10at32)/25
dst = cv2.fi1ter2D(img,-1,kerne1)
plt. subplot(121) , pl t. imshow( img) , plt. title( 'Original ' )
plt.xticks([]), plt.yticks([])
p1t.subp10t(122) •spatial smoothing')
plt.xticks([]), plt.yticks([])
plt. show()
directory = r "H: \\ "
os . chdir(directory)
cv2. imwrite( "IMG_Spatia1_Smoothed. jpg" ,dst)
import cv2
import numpy as np
img = cv2.
kernel_sharpening = 1,
sharpened
= cv2.fi1ter2D(img,-1,kerne1_sharpening)
cv2. imshow( ' Sharpened' , sharpened)
cv2. waitKeyOøhøø)l
cv2. destroyA11Windows()
import cv2
from PIL import Image
img =
doma ter
= cv2. edgepreservingFi1ter(img, flags—I,
cv2. imshow( 'Domain Filter' ,domainFilter)
cv2.waitKey(2øøøe)
import numpy as np
import cv2 as cv
from matplotlib import pyplot as pl t
def :
Image _ Height
= Image. shape[øl
Image_Width
= Image. shape[l]
Image_channels
= Image. shape[2]
Histogram - np.zeros([256, Image_Channe1s], np.int32)
for x in range(ø, Image_Height):
for y in range(ø, Image_Width) :
for c in range(ø, Image_Channe1s):
Histogram[lmage[x,y,c], c] +=1
return Histograln
def Plot_Histogram(Histogram) :
plt. figure()
p1t.tit1e("C010r Image Histogram")
plt.xlabel("lntensity Level")
plt.ylabel("lntensity Frequency")
pit.
256])
p1t.p10t(Histogram[ : ,ø], 'b )
plt. plot (Hi stogram[ : ,
plt. : , 2],

plt. savefig( "color _ Histogram. jpg" )
def main():
Input_lmage =
Histogram = Histogram_computation(lnput_lmage)
for i in range(ø, Histogram. shape[ø]):
for c in range(ø, Histogram. shape[l]):
print("Histogram[",
i,
Plot_Histogram(Histogram)
input("please Enter to Continue...
Histogram[i,c])


