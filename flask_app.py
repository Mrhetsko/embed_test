from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Flask + JS Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                padding: 20px;
                background: #f0f0f0;
                text-align: center;
            }
            h1 {
                color: #333;
            }
            .cube {
                display: inline-block;
                width: 80px;
                height: 80px;
                margin: 10px;
                background-color: teal;
                cursor: pointer;
                transition: transform 0.3s ease;
                border-radius: 8px;
            }
            .cube.enlarged {
                transform: scale(1.5);
                background-color: orange;
            }
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
            // JS: при кліку збільшити кубик
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

    response = make_response(html)
    response.headers['X-Frame-Options'] = 'ALLOW-FROM https://www.notion.so'
    response.headers['Content-Security-Policy'] = "frame-ancestors 'self' https://www.notion.so"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
