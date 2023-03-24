from flask import Flask, request, jsonify, render_template
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/img/resize', methods=['POST'])
def resize_image():
    width = request.form.get('width')
    height = request.form.get('height')
    quality = request.form.get('quality')
    print('w={}, h={}, q={}'.format(width, height, quality))
    
    # Save image to temporary file
    file = request.files['file']
    img_path = '/tmp/' + file.filename
    file.save(img_path)

    img = Image.open(img_path)
    img_format = img.format

    # Resize image
    if width and height and int(width) != 0 and int(height) != 0:
        img = img.resize((int(width), int(height)))
    # Convert image to bytes
    img_bytes = io.BytesIO()
    if quality and int(quality) != 0:
        img.save(img_bytes, format=img_format, quality=int(quality))
    else:
        img.save(img_bytes, format=img_format)
    img_bytes.seek(0)
    # Return image as response
    return jsonify({'image': base64.b64encode(img_bytes.read()).decode('utf-8')});


if __name__ == '__main__':
    app.run(debug=True, port=8000)
