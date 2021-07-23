from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


@app.route('/calc/<int:x>/<int:y>/<string:opr>')
def calc(x, y, opr):
    if opr == 'dif':
        return render_template('calc.html', x=x, y=y, opr="-", result=x - y)
    elif opr == 'sum':
        return render_template('calc.html', x=x, y=y, opr="+", result=x + y)
    elif opr == 'div':
        if y == 0:
            return render_template('calc.html', y=y)
        else:
            return render_template('calc.html', x=x, y=y, opr="/", result=x / y)
    elif opr == 'mult':
        return render_template('calc.html', x=x, y=y, opr="*", result=x * y)
    else:
        return render_template('calc.html', opr="Null")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')