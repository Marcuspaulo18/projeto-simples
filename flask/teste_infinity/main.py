from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder="templates")

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://seu_usuario:@localhost/test_inf_bd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definição dos modelos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False)

class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(60), nullable=False)
    endereco = db.Column(db.String(60), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('enderecos', lazy=True))

class Entrega(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    endereco_entrega = db.Column(db.String(60), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('entregas', lazy=True))

# Rota para lidar com todas as requisições de atualização do banco de dados
@app.route('/atualizar_banco', methods=['POST'])
def atualizar_banco():
    try:
        data = request.form
        if 'nome' in data and 'email' in data:
            nome = data['nome']
            email = data['email']
            usuario = Usuario(nome=nome, email=email)
            db.session.add(usuario)
            db.session.commit()
            return "Usuário cadastrado com sucesso!"
        elif 'cep' in data and 'endereco' in data and 'usuario_id' in data:
            cep = data['cep']
            endereco = data['endereco']
            usuario_id = data['usuario_id']
            endereco = Endereco(cep=cep, endereco=endereco, usuario_id=usuario_id)
            db.session.add(endereco)
            db.session.commit()
            return "Endereço cadastrado com sucesso!"
        elif 'endereco_entrega' in data and 'usuario_id' in data:
            endereco_entrega = data['endereco_entrega']
            usuario_id = data['usuario_id']
            entrega = Entrega(endereco_entrega=endereco_entrega, usuario_id=usuario_id)
            db.session.add(entrega)
            db.session.commit()
            return "Entrega cadastrada com sucesso!"
        else:
            return "Dados inválidos"
    except Exception as err:
        return f"Erro ao atualizar banco de dados: {err}"

if __name__ == '__main__':
    app.run(debug=True)
