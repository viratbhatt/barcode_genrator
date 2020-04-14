import barcode 
barcode.PROVIDED_BARCODES
from barcode.writer import ImageWriter
type = barcode.get_barcode_class('code39')
#ean =EAN('1234567890')
#full = ean.save('ean13_barcode')
print(" Enter Test that you want to make barcode")
code = type(input(), writer=ImageWriter())
print(" Enter Name of the barcode file")
fullname = code.save(input())
