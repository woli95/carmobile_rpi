from flask.wrappers import Request
from main import app
from flask import request, jsonify, send_file

@app.route('/utils/infobar', methods=['GET'])
def utils():
    return jsonify({
        'isConnected': True,
        'isRearCameraOn': False,
        'isFrontCameraOn': True,
        'isRearPlateRecoginitionOn': False,
        'isFrontPlateRecoginitionOn': True,
        'isMemoryCloseToFull': False,
    }), 200


@app.route('/', methods=['GET'])
def x():
    return jsonify(True), 200