from flask import Flask, send_file, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('config.html')  # config.html은 templates/config.html 에 위치해야 함.


@app.route('/config')
def config():
    resolution = request.args.get('resolution', '')
    annotate = request.args.get('annotate', '')
    print(resolution, annotate)

    # TODO: resolution, annotate 설정을 특정 파일에 저장한다. 저장 방법은 xml이나 pickle 등을 사용
    # 캡쳐 프로그램이 설정을 다시 읽도록 SIGUSR1 시그널을 보낸다.

    return 'OK'


@app.route('/capture')
def capture():
    return send_file('foo.jpg')  # 캡쳐 프로그램이 캡쳐한 파일 전송


if __name__ == '__main__':
    app.run('0.0.0.0')