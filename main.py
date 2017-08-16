import os
import face_recognition
from flask import Flask, request, abort, jsonify
from tempfile import mkstemp

app = Flask(__name__)


@app.route('/api/v1/detect-faces', methods=['POST'])
def detect_faces():
    if 'image' not in request.files:
        abort(400)

    descriptor, path = mkstemp()
    os.close(descriptor)

    try:
        request.files['image'].save(path)
        image = face_recognition.load_image_file(path)
        face_locations = face_recognition.face_locations(image)
    finally:
        os.remove(path)

    return jsonify(face_locations)


if __name__ == '__main__':
    app.run(debug=False)
