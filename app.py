from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados de exemplo
usuarios = [
    {"id": 1, "nome": "Gabriel"},
    {"id": 2, "nome": "Felipe"}
]

# Rota GET - listar todos os usuários
@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)

# Rota GET - obter um usuário pelo ID
@app.route("/usuarios/<int:id>", methods=["GET"])
def obter_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if usuario:
        return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

# Rota POST - adicionar um novo usuário
@app.route("/usuarios", methods=["POST"])
def adicionar_usuario():
    novo_usuario = request.get_json()
    usuarios.append(novo_usuario)
    return jsonify(novo_usuario), 201

# Rota PUT - atualizar um usuário
@app.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    dados = request.get_json()
    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["nome"] = dados["nome"]
            return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

# Rota DELETE - remover um usuário
@app.route("/usuarios/<int:id>", methods=["DELETE"])
def remover_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return jsonify({"mensagem": "Usuário removido com sucesso!"})
    return jsonify({"erro": "Usuário não encontrado"}), 404

# Inicia a API
if __name__ == "__main__":
    app.run(debug=True)


