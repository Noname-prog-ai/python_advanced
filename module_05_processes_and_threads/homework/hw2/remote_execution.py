"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, что исполнение кода не уложилось в данное время.
"""

import subprocess
import time
from flask import Flask, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired

app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(validators=[InputRequired()])


def run_python_code_in_subprocess(code: str, timeout: int):
    try:
        start_time = time.time()
        process = subprocess.Popen(["python", "-c", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        while process.poll() is None and time.time() - start_time < timeout:
            time.sleep(0.1)

        if process.poll() is None:
            process.kill()
            return "execution timed out"

        output, error = process.communicate()
        return output.decode('utf-8') + error.decode('utf-8')

    except Exception as e:
        return str(e)


@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()

    if form.validate_on_submit():
        code = form.code.data
        timeout = form.timeout.data

        result = run_python_code_in_subprocess(code, timeout)

        return jsonify({"result": result})

    else:
        return jsonify({"error": "invalid input"})


if __name__ == '__main__':
    app.run(debug=True)
