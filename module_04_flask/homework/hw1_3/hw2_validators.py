"""
Довольно неудобно использовать встроенный валидатор NumberRange для ограничения числа по его длине.
Создадим свой для поля phone. Создайте валидатор обоими способами.
Валидатор должен принимать на вход параметры min и max — минимальная и максимальная длина,
а также опциональный параметр message (см. рекомендации к предыдущему заданию).
"""
from typing import Optional

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import ValidationError


def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form, field):
        if field.data is not None and not min <= len(field.data) <= max:
            if message is None:
                message = f'Field must be between {min} and {max} characters long.'
            raise ValidationError(message)

    return _number_length


class PhoneNumberForm(FlaskForm):
    phone_number = StringField('Phone Number', validators=[number_length(10, 15, message='Invalid phone number length.')])
