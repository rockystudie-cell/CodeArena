from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    # Get text input from form
    data = request.form.get('qrtext')
    
    # Create a QR code from the input data
    qr = qrcode.make(data)
    
    # Save the QR code image to a BytesIO buffer
    img_io = io.BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)

    # Send the image back to the browser as a download
    return send_file(img_io, mimetype='image/png', download_name='qr-code.png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
