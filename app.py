# app.py
from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    html = render_template('index.html')
    response = make_response(html)
    # Дозволити вбудовування в iframe з notion.so
    response.headers['X-Frame-Options'] = 'ALLOW-FROM https://www.notion.so'
    # Новіший варіант CSP для iframe
    response.headers['Content-Security-Policy'] = "frame-ancestors 'self' https://www.notion.so"
    # Дозволити CORS для API, якщо треба (можна підключити flask-cors, але поки так)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
