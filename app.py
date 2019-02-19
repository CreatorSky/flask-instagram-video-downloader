from flask import Flask, render_template, request
from instadown import getdata

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', found=False)


@app.route('/get_post', methods=['POST'])
def get_post():
    url = request.form['url']
    try:
        v_url = getdata(url)
        return render_template('index.html', found=True, video=v_url)
    except:
        print('not found')
        return render_template('index.html', found=True, video="Not found")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
