from flask import *
from lrc import *

app = Flask(__name__)
port = 17001


def load_lrc(content: str):
    mlrc = Lrc2()
    mlrc.load(content)
    # print(str(mlrc.data))


@app.route('/')
def test():
    with open('test.lrc', encoding='UTF8') as f:
        load_lrc(f.read())
    return 'TEST!'

# 注册设备
# 参数：需求的字数(英文x2)，IP（已经提供），即将连接的端口号（暂时用固定的）
@app.route('/sign', methods=['GET'])
def sign():
    args0 = dict(request.args)
    args = {}
    for arg in args0:
        val = args0[arg]
        if type(val) is list:
            args[arg] = val[0]
        else:
            args[arg] = val


if __name__ == '__main__':
    app.run(port=17001, debug=False)