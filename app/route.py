from flask import Flask, request, render_template,abort, make_response, jsonify, Blueprint
import fasttext
import pandas as pd
import numpy as np
import os

sentimental_analysis = Blueprint('sentimental_analysis', __name__)


@sentimental_analysis.route('/message', methods=["POST", "GET"])
def post_message():
    msg = request.json

    def ansower(result):
        if (result[0][0] == '__label____good'):
            return {
                "text": "Texto com boas chances de engajamento"
            }
        else:
            return {
                "text": "Texto com baixa probabilidade de engajamento"
            }

    if not msg.get('text'):
        abort(400,"The object key is different of: text)")
        
    else:
        try:
            model = fasttext.load_model('model/model_balance_update.bim')
            result = model.predict(msg['text'])
            classe = ansower(result)
        except:
            abort(500,"Error loading model")

    return make_response(
        jsonify(classe)
    )
