from flask import flash, redirect, render_template, url_for

from yacut import app, db
from yacut.forms import URLMapForm
from yacut.models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        if URLMap.query.filter_by(original=form.original.data).first():
            flash(
                f'Для этой длинной ссылки уже был использован Укоротитель!')
            return render_template('index.html', form=form)
        if URLMap.query.filter_by(short=form.short.data).first():
            flash('Такая короткая ссылка уже используется!')
            return render_template('index.html', form=form)
        urlmap = URLMap(
            original=form.original.data,
            short=form.short.data
        )
        db.session.add(urlmap)
        db.session.commit()
        return redirect(url_for('urlmap_view', id=urlmap.id))
    return render_template('index.html', form=form)


@app.route('/urlmaps/<int:id>/', methods=['GET'])
def urlmap_view(id):
    return render_template(
        'urlmap.html', urlmap=URLMap.query.get_or_404(id))
