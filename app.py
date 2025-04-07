from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello!"

if __name__ == "__main__":
    app.run(host='192.168.1.208', port=8000) # "host='192.168.1.208:8000'" is gunicorn-nginx interface
                                             # '192.168.1.208' is Raspberry's IP
                                             # '8000' specifies gunicorn-nginx port
