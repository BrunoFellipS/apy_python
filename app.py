# Objetivo:
    # A aplicação receberá dois parâmetros bucket_name e object_key, referente a um arquivo CSV em um bucket do s3, via requisição HTTP.
    # A função deverá ler o arquivo no bucket, tratar as informações e salvar em um banco de sua preferência.
    # • Campos de cpf e cnpj deverá ser salvo sem máscara no banco;
    # • E colunas de datas devem ser salvas no padrão: yyyy-MM-dd;
# URL base
    # A definir
# Endpoits
    #host/bucket_name-and-object_key (post)
    #host/bucket_name-and-object_key (get)
    #host/bucket_name-and-object_key (delete)
# Quais recursos 
    # nome e chave
    
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

df_data_user = pd.read_csv(r"files\arquivo_exemplo.csv", encoding='ISO-8859-1', delimiter =';')

list_lines = []

list_dict = []

for itens in df_data_user.iterrows():
    list_lines.append(itens)
cont = 1
for row in range(len(list_lines)):
    itens = df_data_user.loc[row]
    print(type(itens[0]))
    dic_data = {'id': cont,
                'Originador': itens[0] ,
                'Doc Originador': itens[1] ,
                'Cedente': itens[2],
                'Doc Cedente': itens[3],
                'CCB': itens[4],
                'Id': itens[5],
                'Cliente': itens[6],
                'CPF/CNPJ': itens[7],
                'Endereço': itens[8],
                'CEP': itens[9],
                'Cidade': itens[10],
                'UF': itens[11],
                'Valor do Empréstimo': itens[12],
                'Taxa de Juros (a.m.)': itens[13],
                'Parcela R$': itens[14],
                'Principal R$': itens[15],
                'Juros R$': itens[16],
                'IOF R$':itens[17] ,
                'Comissão R$': itens[18],
                'Total Parcelas': itens[19],
                'Parcela #': itens[20],
                'Multa': itens[21],
                'Mora': itens[22],
                'Data de Emissão':itens[23] ,
                'Data de Vencimento': itens[24],
                'Data de Compra CCB': itens[25],
                'Preço de Aquisição': itens[26]
                }
    list_dict.append(dic_data)
    cont+=1
    break


print(type(dic_data))

# @app.route('/finddados')
# def buscar_dados():
#     return jsonify(list_dict)


# app.run(port=5000,host='localhost', debug=True)
