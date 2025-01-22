from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'movie' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['movie']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            flash('File successfully uploaded')
            return redirect(url_for('process', filename=filename))
    return render_template('index.html')

@app.route('/process/<filename>', methods=['GET', 'POST'])
def process(filename):
    if request.method == 'POST':
        selected_rating = request.form.get('rating')
        flash(f'Movie processed with rating: {selected_rating}')
        return redirect(url_for('index'))
    return render_template('process.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)

