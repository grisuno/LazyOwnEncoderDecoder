import os
import tempfile
from flask import Flask, render_template, request, flash, redirect, url_for, send_file, jsonify
from flask_wtf import FlaskForm
from wtforms import FileField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from lazyown_infinitestorage import encode_file_to_video, decode_video_to_file

class EncodeDecodeForm(FlaskForm):
    input_file = FileField('Input File', validators=[DataRequired()])
    output_file_name = StringField('Output File Name', validators=[DataRequired()])
    frame_width = SelectField('Frame Width', choices=[('640', '640'), ('480', '480')])
    frame_height = SelectField('Frame Height', choices=[('480', '480'), ('360', '360')])
    block_size = SelectField('Block Size', choices=[('4', '4'), ('8', '8'), ('16', '16')])
    action = SelectField('Action', choices=[('encode', 'Encode'), ('decode', 'Decode')], validators=[DataRequired()])
    submit = SubmitField('Start')

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downloads'
ALLOWED_EXTENSIONS = {'zip', 'mp4'}

app.config['SECRET_KEY'] = os.urandom(24)
app.config['UPLOAD_FOLDER'] = os.path.abspath(UPLOAD_FOLDER)
app.config['DOWNLOAD_FOLDER'] = os.path.abspath(DOWNLOAD_FOLDER)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

Bootstrap(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    form = EncodeDecodeForm()
    if form.validate_on_submit():
        if 'input_file' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        file = request.files['input_file']
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            action = form.action.data
            block_size = int(form.block_size.data)
            
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                file.save(temp_file.name)
                try:
                    if action == 'encode':
                        frame_width = int(form.frame_width.data)
                        frame_height = int(form.frame_height.data)
                        output_filename = f"encoded_{frame_width}x{frame_height}.mp4"
                        output_path = os.path.join(app.config['DOWNLOAD_FOLDER'], output_filename)
                        encode_file_to_video(temp_file.name, output_path, (frame_width, frame_height), 30, block_size)
                    elif action == 'decode':
                        output_filename = secure_filename(form.output_file_name.data)
                        output_path = os.path.join(app.config['DOWNLOAD_FOLDER'], output_filename)
                        decode_video_to_file(temp_file.name, output_path, block_size)
                    flash('Operation successful!', 'success')
                    return redirect(url_for('download_file', filename=output_filename))
                except Exception as e:
                    flash(f'An error occurred: {str(e)}', 'danger')
                finally:
                    os.unlink(temp_file.name)
        else:
            flash('File type not allowed', 'danger')
    return render_template('index.html', form=form)

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['DOWNLOAD_FOLDER'], filename), as_attachment=True)

@app.after_request
def add_header(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
# Uncomment the following lines if you want to run the app locally without Gunicorn
# if __name__ == '__main__':
#     app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
