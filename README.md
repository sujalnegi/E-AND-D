
# E AND D

**E AND D is short for Encryption and Decryption. It is a tool which uses custom encryption model to encrypt and decrypt a messege using a secret key.**


## Features

*   **Secure Encryption:**
    *   **Custom Secret Formula:** Uses a strong custom method (KPD-Cipher) to mix up your text so no one can read it.
    *   **Key Protection:** You need a special password (Key) to lock and unlock things, so only people you trust can see it.
    *   **Works with Files:** You can encrypt whole `.txt` files, not just typed messages.

*   **Reliable Decryption:**
    *   **Get It Back:** Turns your scrambled code back into the original message exactly how it was, as long as you have the right key.
    *   **Smart Error Handling:** If you type the wrong key, it won't crash; it just won't work (obviously!).

*   **Easy to Use Interface:**
    *   **Popups:** Cool popup results let you copy, download, or try again without reloading the whole page.
    *   **Help Guide:** There's a "How It Works" button that explains everything if you get stuck.
    *   **Looks Good:** Made with Tailwind CSS so it looks modern and formatted nicely on your phone or laptop.

*   **Privacy Focused:**
    *   **Example:** We don't save anything! Your messages and keys happen right then and there and aren't stored on any server.
    *   **Fast:** Everything feels instant because it's built to be quick.

## Demo and Live Links

- Demo Video is [here]().

- Live link is [here]().


## Usage

1.  **Start:** Click "Encryption" on the main page (or click the left arrow).
2.  **Encrypt:**
    *   Type your message or upload a text file.
    *   Make up a strong key (password).
    *   Click "Encrypt" to get your secret code.
    *   Copy it or Download it as a file.
3.  **Decrypt:**
    *   Go to the "Decryption" page (or click the right arrow from home).
    *   Paste the secret code or upload the encrypted file.
    *   Type the **SAME** key you used to lock it.
    *   Click "Decrypt" to see your original message.

**NOTE:** Don't lose your KEY! If it's gone, your data is gone forever. Seriously.

## Technologies Used

*   **Backend:** Python, Flask
*   **Frontend:** HTML5, CSS3, JavaScript
*   **Styling:** Tailwind CSS
*   **Fonts:** Wagon Serif, Barlow Condensed
*   **Deployment:** Ready to host online

## Local Setup and Installation

Follow these steps to get this running on your own computer.

### 1. What You Need

*   Python 3.7 or newer
*   `pip` (to install python stuff)

### 2. Get the Code

Clone this repo to your computer:

```bash
git clone https://github.com/sujalnegi/E-AND-D.git
cd E-AND-D
```
*

### 3. Install the Stuff

Install the requirements:

```bash
pip install -r requirements.txt
```

### 4. Run It

Start the server:

```bash
python app.py
```

Now open your browser and go here:

```
http://127.0.0.1:5000/
```

Now just go to your browser and paste the above link 

## Author

- **Sujal Negi**
- Email: [sujal1negi@gmail.com](mailto:sujal1negi@gmail.com)
- Instagram: [@_sujal1negi_](https://www.instagram.com/_sujal1negi_/)

## Acknowledgments

- Wagon Serif Font Providers