from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image

img=Image.open('plane.png')
fruit_img=Image.open('fruit.png')
fruit_img.thumbnail((120,120))
draw=ImageDraw.Draw(img)

stx,sty=(0,0)
c3x,c3y=fruit_img.size
msg1='The               is'
msg2='the best!'

#mfont=ImageFont.truetype('FRADM.TTF',40)

#m2font=ImageFont.truetype('BROADW.TTF',52)

draw.text((70,280),msg1,(255,255,0),align='Left')
draw.text((70,330),msg2,(255,0,0),align='Left')

img.paste(fruit_img,(stx,sty,stx+c3x,sty+c3y))

img.show()
img.save('plane2.png')