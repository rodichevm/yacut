from flask_wtf import FlaskForm
from wtforms import URLField
from wtforms.validators import DataRequired, Length, Optional

from settings import MAX_LENGHT_USER_URL


class URLMap(FlaskForm):
    original = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Это поле обязательно для заполнения')]
    )
    short = URLField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(
                max=MAX_LENGHT_USER_URL,
                message=f'Количество символов не больше {MAX_LENGHT_USER_URL}')
        ]
    )