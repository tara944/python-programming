from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

photo = Image.open("Screenshot (3).png")

text = pytesseract.image_to_string(photo)

print(text)