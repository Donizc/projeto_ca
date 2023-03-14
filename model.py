import fasttext

model = fasttext.load_model('model_category.bim')
result = model.predict('praia do bonete')

if (result[0][0] == '__label____bad'):
    print('Texto com boa chances de engajamento' )
else:
    print('Texto com baixa probabilidade de engajamento')

# @app.route('/ckeck',methods = ["POST","GET"])
# def check():
#     text = request.form['text']
#     model = fasttext.load_model('.model_balance.bim')

#     print('::::::::::::Teste de sentimento do texto :::::::::::::')
#     print(f'Insirá o texto:{text}')

#     classe = model.predict(text)
#     print(f"Resultado da análise{classe}")

#     return make_response(
#         jsonify(classe)
#     )
# if __name__ == "__main__":
#     port = int(os.environ.get("PORT",3001))
    