from PIL import Image

형태=input('형태를 입력하세요.')
area=(100,100,200,200)
size=(640,200)

img=Image.open('plane.png')
img2=Image.open('fruit.png')

print(img.size,img.format,img.mode)
print(img2.size,img2.format,img2.mode)

img2_resz=img2.resize(size)

img_cropped=img.crop(area)

img.show()

img_cropped.save('plane cropped.%s'% 형태)
img2_resz.save('fruit resized.%s'% 형태)