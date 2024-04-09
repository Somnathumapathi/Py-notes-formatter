import pytesseract
from PIL import Image
from fpdf import FPDF
import os

def rotateImage(directory):
    
    pdf = FPDF()
    
    imageFiles = [file for file in os.listdir(directory) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
    # sz = len(imageFiles)
    # print(sz)
    
    for imageFile in imageFiles:
        img = Image.open(os.path.join(directory, imageFile))
        
        greyImg = img.convert('L')
        
        orientation = pytesseract.image_to_osd(greyImg)
        
        angle = int(orientation.split('\n')[1].split(':')[1])
        print(angle)
        # rotImg = img.rotate(angle)
        if angle > 0:
            angle -= 180
        
        rotImg = img.rotate(angle, expand=True)

        # if angle != 0 or angle !=180:
        #     rotImg = img.rotate(360-angle, expand= True)
        # else:
        #     rotImg = img
        
        if rotImg.mode == 'RGBA':
            rotImg = rotImg.convert('RGB')
        
        temp_file = os.path.join(directory, f'temp_{imageFile}')
        rotImg.save(temp_file)
        
        pdf.add_page()
        pdf.image(temp_file, 0, 0, pdf.w, pdf.h)
        
        os.remove(temp_file)
    
    pdf_file = os.path.join(directory, 'notes.pdf')
    pdf.output(pdf_file, 'F')
    print(f"PDF file generated: {pdf_file}")

#Use your path
rotateImage(r'C:\Users\exuser\Testfolder')
