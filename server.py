from flask import Flask, render_template, request, redirect
import analyze_fragment
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/submitted')
def submitted():
    return render_template('submitted.html')

@app.route('/submission', methods = ['GET', 'POST'])
def upload_file():
	# return "Hello world"
	if request.method == 'POST':
		f = request.files['file']
    	f.save(secure_filename(f.filename))
    	file_name, file_extension = f.filename.split(".")
    	file_name += "_output"
    	new_name = file_name + "." + file_extension
    	analyze_fragment.stitch_fragments(f.filename, new_name)
    	return redirect("/submitted")

if __name__ == '__main__':
	app.run(debug = True) 