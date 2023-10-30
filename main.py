from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image
import os
import pixellib
from pixellib.tune_bg import alter_bg
#from rembg import remove

pth = os.getcwd()

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = pth
app.config['UPLOAD_FOLDER'] = 92222222


#input_path =  '/content/drive/MyDrive/pics/pic-sep-2023.jpg'

# Store path of the output image in the variable output_path
#output_path = '/content/drive/MyDrive/pics/pic-sep-2023-chg_bg.jpg'


#change_bg.load_pascalvoc_model("/content/drive/MyDrive/pics/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
#change_bg.color_bg(input_path, colors = (255,255,255), output_image_name=output_path)

@app.route('/')
def hello_world():
	return 'Hello World - I am Rising!'

@app.route('/upload')
def upload_file1():
	return render_template('upload.html')

@app.route('/uploader', methods=['GET','POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		sec_fname = secure_filename(f.filename)
		input_path = os.path.join('static',sec_fname)
		fname_output = os.path.join('output_img', sec_fname)
		output_path = os.path.join('static',fname_output)
		f.save(input_path)
		change_bg = alter_bg()
		change_bg.load_pascalvoc_model(os.path.join('static','deeplabv3_xception_tf_dim_ordering_tf_kernels.h5'))
		change_bg.color_bg(input_path, colors = (255,255,255), output_image_name=output_path)
		################ for rembg module
		# Processing the image
		#input = Image.open(input_path)
        	# Removing the background from the given Image
		#output = remove(input)
		#output = output.convert('RGB')
        	#Saving the image in the given path
		#output.save(output_path)
		####################
		return render_template('upload.html',fname=sec_fname, fname_output = fname_output )
		#return 'File uploaded successfully'

if __name__ == '__main__':
	app.run()