from flask import Blueprint, request, jsonify, current_app
from . import auth, identifier
from .exception import *
import os

bp = Blueprint("endpoints", __name__)

@bp.errorhandler(ApiException)
def handle_api_exception(e):
    """Catch-all error handler for types deriving from ApiException."""
    return jsonify(e.to_dict())

@bp.route("/upload/<token>", methods=["POST"])
@auth.auth_required
def upload():
    if not "image" in request.files:
        raise MissingImage("No image was provided for upload.")
    image = request.files["image"]
    _, extension = os.path.splitext(image.filename)
    extension = extension[1:] # strip off . from ".<ext>"
    if extension not in current_app.config["ALLOWED_EXTENSIONS"]: # TODO: assumes images match their extension. Should verify.
        raise ImageTypeNotAllowed("The format of the image provided is not allowed.")

    upload_dir = current_app.config["UPLOAD_DIRECTORY"]

    name = f"{identifier.generate_identifier()}.{extension}"
    path = os.path.join(upload_dir, name)

    while os.path.exists(path): # generate new names until we have a unique path
        name = f"{identifier.generate_identifier()}.{extension}"
        path = os.path.join(upload_dir, name)

    try:
        image.save(path) # save the image
    except OSError:
        raise SystemError("The server encountered an error saving the image. Perhaps it is out of space.")
    # TODO: image size checks?

    return jsonify({"status": "success", "url": f"{current_app.config['STATIC_HOST']}/{name}"})
