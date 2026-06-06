from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'title': '나는 오늘 퇴사',
        'content': '쿠팡 2조 투자 유치!!!',
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
