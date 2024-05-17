import pytesseract
from PIL import Image
from fpdf import FPDF
import os
from flask import Flask, request, render_template, send_file, redirect, url_for, flash
from werkzeug.utils import secure_filename
import zipfile
import tempfile

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'zip'}
app.secret_key = 'supersecretkey'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def rotate_images(directory):
    pdf = FPDF()
    imageFiles = [file for file in os.listdir(directory) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for imageFile in imageFiles:
        img = Image.open(os.path.join(directory, imageFile))
        grayImg = img.convert('L')
        orientation = pytesseract.image_to_osd(grayImg)
        angle = int(orientation.split('\n')[1].split(':')[1])
        # print(angle)
        # rotImg = img.rotate(angle)
        if angle > 0:
            angle -= 180
        
        rotImg = img.rotate(angle)

        # if angle != 0 or angle !=180:
        #     rotImg = img.rotate(360-angle, expand= True)
        # else:
        #     rotImg = img

        if rotImg.mode == 'RGBA':
            rotImg = rotImg.convert('RGB')

        # if img.mode == 'RGBA':
        #     img = img.convert('RGB')
        
        temp_file = os.path.join(directory, f'temp_{imageFile}')
        rotImg.save(temp_file)
        
        pdf.add_page()
        pdf.image(temp_file, 0, 0, pdf.w, pdf.h)
        os.remove(temp_file)
    
    pdf_file = os.path.join(directory, 'notes.pdf')
    print("Temporary directory:", directory)
    print("PDF file path:", pdf_file)
    pdf.output(pdf_file, 'F')
    return pdf_file


@app.route('/', methods = ['GET','POST'])
def notesFormate():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No files')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        # print('working..........')
        if file and allowed_file(file.filename):
            print('working..........')
            filename = secure_filename(file.filename)
            tempDir = tempfile.mkdtemp()
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(tempDir)
            pdfFile = rotate_images(tempDir)
            print('working..........')
            pdfName = os.path.basename(pdfFile)
            
            return redirect(url_for('downloadPage', filename = pdfName))
    return render_template('homepage.html')

@app.route('/downloadsuccess/<filename>')
def downloadPage(filename):
    return render_template('downloadpage.html', filename = filename)

@app.route('/download/<filename>')
def download(filename, tempDir):
    pdf_file = os.path.join(tempfile.gettempdir(),filename)
    print(pdf_file)
    return send_file(pdf_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

