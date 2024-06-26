import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from encoder_decoder import encode, decode

class EncodeDecodeForm(FlaskForm):
    input_string = StringField('Input String', validators=[DataRequired()])
    shift_value = IntegerField('Shift Value', validators=[DataRequired()])
    substitution_key = StringField('Substitution Key', validators=[DataRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SESSION_REFRESH_EACH_REQUEST'] = False
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = EncodeDecodeForm()
    result = None
    action = None
    if form.validate_on_submit():
        input_string = form.input_string.data
        shift_value = form.shift_value.data
        substitution_key = form.substitution_key.data
        action = request.form.get('action')

        try:
            if action == 'encode':
                result = encode(input_string, shift_value, substitution_key)
            elif action == 'decode':
                result = decode(input_string, shift_value, substitution_key)
            flash('Operation successful!', 'success')
        except Exception as e:
            flash(f'An error occurred: {e}', 'danger')

    return render_template('index.html', form=form, result=result, action=action)

@app.after_request
def add_security_headers(response):
    response.cache_control.no_cache = True
    response.cache_control.no_store = True
    response.cache_control.must_revalidate = True
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
