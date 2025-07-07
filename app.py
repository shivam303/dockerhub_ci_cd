from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Flask Styling Demo</title>
    </head>
    <body style="background-color:#f4f4f9; text-align:center; padding-top:100px;">
        <h1 style="color:#4a90e2; font-family:Arial, sans-serif;">Welcome to My Styled Flask App!</h1>
        <p style="color:#333; font-size:20px; font-family:'Courier New', monospace;">
            Flask + HTML + Colors = ❤️
        </p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port = 5000)