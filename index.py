from flask import Flask, request
from flask_cors import CORS
import pandas as pd  # Import pandas to work with CSV data
from whatsappMessaging import send_messages

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['get'])
def default_message():
    return 'Server is Up and Running'

@app.route('/upload', methods=['POST'])
def upload_file():
    # print('check',request.files['file'])
    if 'file' not in request.files:
        print('No file found')
        return 'No file part'
    
    text_data = request.form.get('textData')
    if not text_data:
        return 'No text data provided'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    df=pd.read_csv(request.files['file'])
    phone_numbers=df['mobile_no']
    send_messages(phone_numbers, text_data)

    # print("Received text data:", text_data)

    return 'File and text data received and processed successfully!'



if __name__ == '__main__':
    app.run(debug=True)
