from flask.wrappers import Request
from main import app
from flask import request, jsonify, send_file, abort

import functions

@app.route('/utils/infobar', methods=['GET'])
def utils():
    if request.method == 'GET':
        disk_usage = functions.getHardDiskUsage()
        return jsonify({
            'isRearCameraOn': False,
            'isFrontCameraOn': True,
            'isRearPlateRecoginitionOn': False,
            'isFrontPlateRecoginitionOn': True,
            'diskUsage_total': disk_usage["total"],
            'diskUsage_free': disk_usage["free"],
            'diskUsage_used': disk_usage["used"]
        }), 200
    else:
        return abort(404)


@app.route('/', methods=['GET'])
def x():
    return jsonify(True), 200