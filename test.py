from flask import Flask ,request,render_template,make_response,jsonify,Blueprint
import fasttext
import pandas as pd
import numpy as np
import os 
 
app =Flask(__name__)

@app.route('/message',methods = ["POST","GET"])
def post_message():
    msg = request.json
    def ansower(result):
        if (result[0][0] == '__label____bad'):
            return{
                     "text":"Texto com baixa probabilidade de engajamento"

            }
        else:
            return {
                    "text":"Texto com boas chances de engajamento"

            }
    try:
        model = fasttext.load_model('model/model_category.bim')
        result = model.predict(msg['text'])
        classe = ansower(result)
    except (ValueError):
         print('Error of load model or structor of text')
         
    return make_response(
        jsonify(classe)
    )
app.run()