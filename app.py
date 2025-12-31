from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encryption')
def encryption():
    return render_template('encryption.html')

@app.route('/encrypt_text', methods=['POST'])
def encrypt_text():
    return "Encryption Logic Not Implemented Yet"

@app.route('/decryption')
def decryption():
    return render_template('decryption.html')

if __name__ == '__main__':
    app.run(debug=True)
