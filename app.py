from flask import Flask, render_template, request, flash
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf import FlaskForm
import encoder_decoder as ed
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

class EncodeDecodeForm(FlaskForm):
    input_string = StringField('Input String', validators=[DataRequired(), Length(min=1, max=100)])
    shift_value = IntegerField('Shift Value', validators=[DataRequired(), NumberRange(min=0, max=25)])
    substitution_key = StringField('Substitution Key', validators=[DataRequired(), Length(min=1, max=26)])
    encode = SubmitField('Encode')
    decode = SubmitField('Decode')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = EncodeDecodeForm()
    result = ''
    if form.validate_on_submit():
        input_string = form.input_string.data
        shift_value = form.shift_value.data
        substitution_key = form.substitution_key.data
        if form.encode.data:
            result = ed.encode(input_string, shift_value, substitution_key)
        elif form.decode.data:
            result = ed.decode(input_string, shift_value, substitution_key)
    return render_template('index.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
