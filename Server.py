import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, Request, jsonify, Response
from werkzeug.utils import secure_filename
import pickledb
from datetime import datetime

app = Flask(__name__, static_folder='public', static_url_path='')
UPLOAD_FOLDER = './public/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# db = pickledb.load('recipes.db', True)
# if not db.get('images'):
#    db.dcreate('images')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# @app.route('/upload-photo', methods=['POST'])
# def upload():
#     if 'file' not in request.files or 'caption' not in request.form or 'timestamp' not in request.form:
#         return jsonify({"success": False, "message": "Missing file, caption or timestamp"}), 400
    
#     file = request.files['file']
#     caption = request.form['caption']
#     timestamp = request.form['timestamp']

#     if file.filename == '':
#         return jsonify({"success": False, "message": "No selected file"}), 400
    
#     if not allowed_file(file.filename):
#         return jsonify({"success": False, "message": "File type not allowed"}), 400
        
#     filename = secure_filename(file.filename)
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#     image_specs = {
#         "name" : filename,
#         "caption": caption,
#         "timestamp" : timestamp
#     }

#     db.dadd('images', (filename, image_specs))
#     return redirect('index.html', 302, Response(None))


# @app.route('/images', methods=['GET'])
# def get_photos():
#     images_specs = db.dgetall("images")
#     return jsonify(list(images_specs.values()))

# @app.route('/images/<name>', methods=['PUT'])
# def update_photo(name):

#     if not db.dexists('images', name):
#         return "Photo not found", 404
    
#     data = request.json

#     if 'caption' not in data or 'timestamp' not in data:
#         return "Missing caption or timestamp", 400
    
#     caption = data['caption']
#     timestamp = data['timestamp']
    
#     image_specs = {
#         "name" : name,
#         "caption" : caption,
#         "timestamp" : timestamp
#     }

#     db.dadd('images', (name, image_specs))

#     return "Image specifications updated", 200

# @app.route('/images/<name>', methods=['DELETE'])
# def delete_photo(name):
#     if not db.dexists('images', name):
#         return "Image not found", 404

#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], name)
#     if os.path.exists(file_path):
#        os.remove(file_path)

#     db.dpop('images', name)

#     return "Image deleted", 200

# @app.route('/images/<name>')
# def uploaded_file(name):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], name)


# @app.route('/toUpload')
# def toUpload():
#     return send_from_directory(app.static_folder, 'upload.html')


@app.route('/')
def start():
    return send_from_directory(app.static_folder, 'Home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=22020, debug=True)
