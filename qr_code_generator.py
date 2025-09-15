import qrcode
img = qrcode.make('https://github.com/acheronx0577')
type(img)  # qrcode.image.pil.PilImage
img.save("My github page.png")
