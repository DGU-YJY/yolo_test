from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/') 
def hello(): 
    return 'Hello, World!'

#업로드 HTML 렌더링
@app.route('/upload')
def render_file():
    return render_template('upload.html')

#파일 업로드 처리
@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        #저장할 경로 + 파일명
        f.save(secure_filename('clothes.jpg'))
        line = os.system('python detect.py --source clothes.jpg --weights weights/best.pt --conf 0.25 --save-txt --save-crop')
        with open('./clothes.txt', 'r') as result:
            line= result.readline()
            
        if line == 'skirt':
            line = '치마'
        elif line == 'top':
            line = '상의'
        elif line == 'pants':
            line = '바지'
        
            
        # os.remove(BASE_DIR+'/runs/detect/')
        # os.makedirs(BASE_DIR+'/runs/detect/')
        return str(line)+'<br>uploads 디렉토리 -> 파일 업로드 성공!'

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', debug=True)


# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'hello'



# if __name__ == '__main__':
#     app.run(host = '0.0.0.0', debug = True)