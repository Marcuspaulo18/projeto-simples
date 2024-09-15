from flask import Flask, render_template, request, jsonify, redirect, url_for
import banco  # Módulo contendo funções de interação com o banco de dados
import pymysql
import requests
import googlemaps

# Inicialização do aplicativo Flask
app = Flask(__name__, template_folder="templates")

# Chave de API do Google Maps
API_KEY = 'vai no site da google:3'

# Inicialização do cliente Google Maps
gmaps = googlemaps.Client(key=API_KEY)


# Rota principal, redireciona para a rota de login
@app.route('/')
def home():
    return redirect(url_for('login'))


# Rota para calcular a entrega
@app.route('/calcular_entrega', methods=["POST"])
def calcular_entrega():
    if request.method == "POST":
        # Obter os dados do formulário
        cep_pi = request.form.get('cep_pi')
        endereco_pi = request.form.get('endereco_pi')
        cep_pf = request.form.get('cep_pf')
        endereco_pf = request.form.get('endereco_pf')

        # Consulta à API do Google Maps para obter a distância e o tempo
        url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={cep_pi},{endereco_pi}&destinations={cep_pf},{endereco_pf}&key={API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Verifica se a resposta da API contém dados
        if 'rows' in data and len(data['rows']) > 0 and 'elements' in data['rows'][0] and len(
                data['rows'][0]['elements']) > 0 and data['status'] == 'OK':
            # Extrai a distância e o tempo da resposta da API
            distancia = data['rows'][0]['elements'][0].get('distance', {}).get('text', 'N.O')
            tempo = data['rows'][0]['elements'][0].get('duration', {}).get('text', 'N.O')
        else:
            distancia = 'N.O'
            tempo = 'N.O'
        try:
            banco.inserir_dados_em_tabela('entrega', 'distan, temp', f"'{distancia}', '{tempo}'")
        except Exception as e:
            return jsonify({'error': str(e)})

        # Retorne os dados para exibição no frontend
        return jsonify({'distancia': distancia, 'tempo': tempo})

    else:
        return jsonify({'error': 'Método não permitido'})


# Rota de login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Capturar os dados do formulário
        email_l = request.form['email_l']
        senha_l = request.form['senha_l']

        # Verificar autenticação do usuário
        if banco.autenticar_usuario(email_l, senha_l):
            banco.inserir_dados_em_tabela('logins', 'login_email, login_senha', f"'{email_l}', '{senha_l}'")
            # Usuário autenticado com sucesso
            return render_template("start.html")
        else:
            # Usuário não autenticado, redireciona para a página de login
            return redirect(url_for('login'))
    else:
        # Renderizar a página de login
        return render_template("login.html")


# Rota de cadastro
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        # Capturar os dados do formulário
        usuario = request.form['usuario']
        email = request.form['email']
        senha = request.form['senha']
        cep = request.form['cep']
        endereco = request.form['endereco']

        try:
            # Inserir os dados no banco de dados
            banco.inserir_dados_em_tabela('cadastro',
                                          'cadastro_usuario, cadastro_email, cadastro_senha, cadastro_cep, cadastro_endereco',
                                          f"'{usuario}', '{email}', '{senha}', '{cep}', '{endereco}'")

            return render_template("cadastro.html", status='success')
        except Exception as e:
            # Se ocorrer uma exceção, redireciona de volta para a página de cadastro
            return render_template("cadastro.html", status='fail')
    else:
        status = request.args.get('status')
        # Renderizar a página de cadastro no caso de requisição GET
        return render_template("cadastro.html", status=status)


# Executar o aplicativo Flask
if __name__ == "__main__":
    app.run(debug=True)
