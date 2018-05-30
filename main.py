import os
import face_recognition
from flask import Flask, request, abort, jsonify
from tempfile import mkstemp
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.errorhandler(HTTPException)
def error_handler(error):
    code = error.code if error.code is not None else 500
    data = {
        "error": error.name,
        "code": code,
    }

    if error.description is not None:
        data["description"] = error.description

    response = jsonify(data)
    response.status_code = code

    return response


@app.errorhandler(Exception)
def error_handler(error):
    response = jsonify({
        "error": "Internal Server Error",
        "code": 500,
    })
    response.status_code = 500

    return response


@app.route('/detect-faces', methods=['POST'])
def detect_faces():
    if 'image' not in request.files:
        abort(400, description1="missing 'image' POST field")

    descriptor, path = mkstemp()
    os.close(descriptor)

    try:
        request.files['image'].save(path)

        try:
            image = face_recognition.load_image_file(path)
        except OSError:
            abort(400, description="unable to load image")

        model = request.args.get('model', 'hog')
        number_of_times_to_upsample = int(request.args.get('number_of_times_to_upsample', 1))

        if number_of_times_to_upsample < 0:
            abort(400, description="query parameter 'number_of_times_to_upsample' should be >= 0")

        face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=number_of_times_to_upsample, model=model)
    finally:
        os.remove(path)

    return jsonify(face_locations)


if __name__ == '__main__':
    app.run(debug=False)
