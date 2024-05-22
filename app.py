from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')
    tipo = data.get('tipo')

    if email in users:
        return jsonify({'message': 'E-mail já cadastrado'}), 400

    users[email] = {'nome': nome, 'senha': senha, 'tipo': tipo}
    return jsonify({'message': 'Usuário cadastrado com sucesso'}), 201

@app.route('/login', methods=['POST'])
def fazer_login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')

    if email not in users or users[email]['senha'] != senha:
        return jsonify({'message': 'Credenciais inválidas'}), 401

    return jsonify({'message': 'Login bem-sucedido', 'tipo': users[email]['tipo']}), 200

if __name__ == '__main__':
    app.run(debug=True)
