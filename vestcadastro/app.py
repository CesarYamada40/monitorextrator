from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    loja = request.form['loja']
    ip = request.form['ip']
    dns = request.form['dns']
    http = request.form['http']
    tcp = request.form['tcp']
    gateway = request.form['gateway']
    ddns = request.form['ddns']
    cameras = request.form['cameras']
    horario = request.form['horario']

    # Escrever os dados no arquivo .txt
    with open('dados.txt', 'a') as f:
        f.write(f'{loja}\t{ip}\t{dns}\t{http}\t{tcp}\t{gateway}\t{ddns}\t{cameras}\t{horario}\n')

    # Ler os dados do arquivo .txt
    with open('dados.txt', 'r') as f:
        linhas = f.readlines()

    dados = [linha.strip().split('\t') for linha in linhas]

    # Criar um DataFrame com os dados
    df = pd.DataFrame(dados, columns=['Loja', 'IP', 'DNS', 'Porta HTTP', 'Porta TCP', 'Gateway', 'DDNS', 'Quantidade de câmeras', 'Horário de abertura e fechamento'])

    # Escrever os dados na planilha .xlsx
    df.to_excel('dados.xlsx', index=False)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)