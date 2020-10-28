from flask import Flask
from flask import request,redirect,render_template,url_for
from werkzeug.utils import secure_filename
import os
import pytesseract
from PIL import ImageFilter
from PIL import Image
from pdf2image import convert_from_path 


import sys


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/Users/zameershaik/Documents'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submitImage/',methods=['POST',])
def submitImage():
    image = request.files['ocrImage']
    text = ''
    filename = secure_filename(image.filename)
    if (filename[-3:]=='pdf'):
        pages = convert_from_path(filenme)
        image= page.save('out.jpg', 'JPEG')
        
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        text = pytesseract.image_to_string(img)
        f = open(os.path.join(app.config['UPLOAD_FOLDER'], filename)+'.txt','w')
        f.write(text)
        f.close()
        return render_template('textFile.html',text=text,filename=f)
    else:
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        text = pytesseract.image_to_string(img)
        f = open(os.path.join(app.config['UPLOAD_FOLDER'], filename)+'.txt','w')
        f.write(text)
        f.close()
        return render_template('textFile.html',text=text,filename=f)

    
    


if __name__ == '__main__':
    app.run('0.0.0.0',8000)
