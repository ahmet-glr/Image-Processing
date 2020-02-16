from PIL import Image
import pytesseract

img_adress = "C:\\Users\\AhmetGuler\\Desktop\\ROVER\\Image Processing\\OpenCV A-Z™  Uygulamalarla Görüntü İşleme  2019  21 Saat\\20. Resimdeki Metni Okuma (text reading)\\Cpp_Photo.png"
img = Image.open(img_adress)

my_text = pytesseract.image_to_string(img)

notepad_text = open("Img_To_Notepad.txt","w")

notepad_text.write(my_text)

notepad_text.close()