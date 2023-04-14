from PIL import ImageDraw
from PIL import Image

형태=input('형태를 입력하세요.')

canvas_size=(200,200)
rect_area=[(0,0),(100,100)]
line_cor=[(0,200),(200,0)]
circle_area=[(100,100),(200,200)]

new_img=Image.new('RGB',canvas_size,'orange')

draw_img=ImageDraw.Draw(new_img)

draw_img.rectangle(rect_area,fill='red',outline='yellow')

draw_img.line(line_cor,fill='blue',width=4)

draw_img.ellipse(circle_area,fill='green',outline='red')

new_img.show()
new_img.save('Imagedraw.%s'%형태)