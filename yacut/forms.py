from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

from settings import MAX_LENGHT_USER_URL


class URLMapForm(FlaskForm):
    original = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Это поле обязательно для заполнения'),
            URL(message='Введите ссылку в корректном формате')
        ]
    )
    short = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(
                min=1,
                max=MAX_LENGHT_USER_URL,
                message=f'Количество символов больше {MAX_LENGHT_USER_URL}'
            ),
            Regexp(
                regex='[0-9A-Za-z]+',
                message='Ссылка содержит недопустимые символы'
            )
        ]
    )
    submit = SubmitField('Создать')
