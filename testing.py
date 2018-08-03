try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

def processReceipt(imageFile):
    imageText = pytesseract.image_to_string(Image.open(imageFile))
    lines = imageText.splitlines()
    for line in lines:
        words = line.split()
        if(len(words) > 0):
            if(len(words[len(words)-1]) == 1):
                #Most likely a food line item
                foodName = ''
                for word in words:
                    try:
                        float(word)
                        break
                    except ValueError:
                        foodName += ' ' + word
                print('Item name: ' + foodName)
                print('Item: ' + line)


processReceipt('receipt.png')
# Simple image to string
#print(pytesseract.image_to_string(Image.open('receipt.png')))