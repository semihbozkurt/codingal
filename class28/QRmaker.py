import qrcode

x=qrcode.QRCode()
data=input("enter the data")

x.add_data(data)
x.make()

file=input("write the file name:")
img=x.make_image()

img.save(file+".png")