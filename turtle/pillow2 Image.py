from PIL import Image

size=(200,200)
형태=input('형태를 입력하세요.')

img=Image.open('plane.png')

img_rotate=img.rotate(90)

img_convert=img.convert('L')

img_transpose=img.transpose(Image.FLIP_LEFT_RIGHT)

img.thumbnail(size)

print('plane_convert.mode =',img_convert.mode)

print('plane.size =',img.size)

img_convert.show()
img_transpose.show()
img_transpose.save('plane 흑백.%s'% 형태)
img_rotate.save('plane rotated.%s'% 형태)
img.save('plane image.%s'%형태)