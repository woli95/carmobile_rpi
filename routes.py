from flask.wrappers import Request
from main import app
from flask import request, jsonify, send_file, abort

import functions

@app.route('/utils/infobar', methods=['GET'])
def utils():
    if request.method == 'GET':
        du_total, du_used, du_free = functions.getHardDiskUsage()
        return jsonify({
            'isRearCameraOn': False,
            'isFrontCameraOn': True,
            'isRearPlateRecoginitionOn': False,
            'isFrontPlateRecoginitionOn': True,
            'diskUsage_total': du_total,
            'diskUsage_free': du_free,
            'diskUsage_used': du_used
        }), 200
    else:
        return abort(404)

@app.route('/utils/videos', methods=['GET'])
def videos():
    if request.method == 'GET':
        return jsonify(functions.getSavedVideoFilenames()), 200
    else:
        return abort(404)

@app.route('/', methods=['GET'])
def x():
    return jsonify(True), 200