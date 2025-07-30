from flask import Flask

app = Flask(__name__)

# Ця функція просто повертає HTML
@app.route('/')
def index():
    # Просто повертаємо HTML як рядок. Flask сам створить відповідь.
    return """
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Flask + JS Demo</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; background: #f0f0f0; text-align: center; }
            h1 { color: #333; }
            .cube { display: inline-block; width: 80px; height: 80px; margin: 10px; background-color: teal; cursor: pointer; transition: transform 0.3s ease; border-radius: 8px; }
            .cube.enlarged { transform: scale(1.5); background-color: orange; }
        </style>
    </head>
    <body>
        <h1>Привіт! Це Flask + JavaScript демо 🚀</h1>
        <div id="cubes-container">
            <div class="cube"></div>
            <div class="cube"></div>
            <div class="cube"></div>
        </div>
        <script>
            const cubes = document.querySelectorAll('.cube');
            cubes.forEach(cube => {
                cube.addEventListener('click', () => {
                    cube.classList.toggle('enlarged');
                });
            });
        </script>
    </body>
    </html>
    """

# Цей декоратор перехоплює відповідь ПЕРЕД відправкою клієнту
@app.after_request
def add_security_headers(response):
    # Тепер ми маємо доступ до об'єкту `response` і можемо змінювати його заголовки
    response.headers.pop('X-Frame-Options', None)
    response.headers['Content-Security-Policy'] = "frame-ancestors 'self' https://apption.co"
    return response

if __name__ == "__main__":
    # Для Render.com краще використовувати Gunicorn, але для локального тестування це ок
    app.run(host='0.0.0.0', port=5000)