from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return 'Hello {}'.format(name)


@app.route('/<f>/<number>')
def switch_temp(f='fahrenheit', number=0):
    new_temperature = 0
    if f == 'fahrenheit':
        new_temperature = (int(number) - 32) * 5 / 9
        return '{}: {:.0f}'.format('Celsius', new_temperature)
    elif f == 'celsius':
        new_temperature = (int(number) * 9 / 5) + 32
        return '{}: {:.0f}'.format('Fahrenheit', new_temperature)


if __name__ == '__main__':
    app.run()
