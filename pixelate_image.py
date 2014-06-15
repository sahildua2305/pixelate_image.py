from PIL import Image

image = Image.open("C://users/Ck7/Desktop/ti.jpg")

x = int(raw_input("Enter the number of column: "))
y = int(raw_input("Enter the number of rows: "))
w,h = image.size
sqx = w/x
sqy = h/y
sqx2 = sqx//2
sqy2 = sqy//2

backgroundColor = (255,)*3

pix = image.load()

for x in range(0, w-sqx, sqx):
    for y in range(0, h-sqy, sqy):
        R,G,B = image.getpixel((x+sqx2, y+sqy2))
        #print R,G,B
        
        for p in range(x,x+sqx):
            for q in range(y,y+sqy):
                #pix[p,q] = (R,G,B)
                if R>90 and G>90 and B>90:
                    #LED OFF
                    pix[p,q] = (255,255,255)
                else:
                    #LED ON
                    pix[p,q] = (0,0,0)

pixel = image.load()
for i in range(0,w,sqx):
    for j in range(0,h,sqy):
        for r in range(sqx):
            #print i,j,r
            if i+r < w and j+r < h:
                pixel[i+r,j] = backgroundColor
                pixel[i,j+r] = backgroundColor

image.save("C://users/Ck7/Desktop/ti_pixelate_32.jpg")
