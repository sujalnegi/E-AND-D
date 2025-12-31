from flask import Flask, render_template, request, send_file, Response
import io

app = Flask(__name__)
def kpd_encrypt(plaintext, key):
    if not plaintext:
        return ""
    if not key:
        key = "default"
    if isinstance(plaintext, bytes):
        try:
            plaintext = plaintext.decode('utf-8')
        except:
            plaintext = plaintext.decode('latin-1')
            
    p_indices = [ord(c) for c in plaintext]
    text_len = len(p_indices)
    
    k_indices = [ord(c) for c in key]
    key_len = len(k_indices)
    
    encrypted_chars = []
    for i in range(text_len):
        p_val = p_indices[i]
        k_val = k_indices[i % key_len]
        s_val = p_val + k_val
        d_val = s_val + i        
        e_val = ((d_val - 32) % 95) + 32
        
        encrypted_chars.append(chr(e_val))
        block_size = 8
        final_output = []
    
    for i in range(0, text_len, block_size):
        block = encrypted_chars[i : i + block_size]
        final_output.extend(reversed(block))
    return "".join(final_output)

def kpd_decrypt(ciphertext, key):
    if not ciphertext:
        return ""
    if not key:
        key = "default"

    if isinstance(ciphertext, bytes):
        try:
            ciphertext = ciphertext.decode('utf-8')
        except:
            ciphertext = ciphertext.decode('latin-1')

    block_size = 8
    chars = list(ciphertext)
    text_len = len(chars)
    
    reversed_chars = []
    for i in range(0, text_len, block_size):
        block = chars[i : i + block_size]
        reversed_chars.extend(reversed(block))
        
    p_indices = []
    k_indices = [ord(c) for c in key]
    key_len = len(k_indices)
    
    for i in range(text_len):
        e_val = ord(reversed_chars[i])
        
        d_val = ((e_val - 32) % 95) + 32        
        k_val = k_indices[i % key_len]

        raw_p = d_val - i - k_val
        p_val = ((raw_p - 32) % 95) + 32
        
        p_indices.append(chr(p_val))
        
    return "".join(p_indices)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encryption')
def encryption():
    return render_template('encryption.html')

@app.route('/decryption')
def decryption():
    return render_template('decryption.html')

from flask import jsonify

@app.route('/encrypt_text', methods=['POST'])
def encrypt_text():
    key = request.form.get('key', '')
    message = ""
    if 'file' in request.files and request.files['file'].filename != '':
        f = request.files['file']
        message = f.read().decode('utf-8', errors='ignore')
    else:
        message = request.form.get('message', '')
    
    encrypted_data = kpd_encrypt(message, key)
    
    return jsonify({'result': encrypted_data})

@app.route('/decrypt_text', methods=['POST'])
def decrypt_text():
    key = request.form.get('key', '')    
    ciphertext = ""
    if 'file' in request.files and request.files['file'].filename != '':
        f = request.files['file']
        ciphertext = f.read().decode('utf-8', errors='ignore')
    else:
        ciphertext = request.form.get('encrypted_message', '')
    
    decrypted_data = kpd_decrypt(ciphertext, key)
    
    return jsonify({'result': decrypted_data})

if __name__ == '__main__':
    app.run(debug=True)
