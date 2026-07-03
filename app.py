from flask import Flask, jsonify, request

app = Flask(__name__)

dispositivos = [
    {
        "id": 1,
        "nome": "Roteador",
        "ip": "192.168.1.1"
    }
]

@app.route("/")
def home():
    return jsonify({
        "mensagem": "API HTTP funcionando"
    })

@app.route("/dispositivos", methods=["GET"])
def listar():
    return jsonify(dispositivos)

@app.route("/dispositivos/<int:id>", methods=["GET"])
def buscar(id):
    for d in dispositivos:
        if d["id"] == id:
            return jsonify(d)
    return jsonify({"erro": "Nao encontrado"}), 404

@app.route("/dispositivos", methods=["POST"])
def adicionar():

    dados = request.json

    novo = {
        "id": len(dispositivos)+1,
        "nome": dados["nome"],
        "ip": dados["ip"]
    }

    dispositivos.append(novo)

    return jsonify(novo), 201

@app.route("/dispositivos/<int:id>", methods=["PUT"])
def atualizar(id):

    dados = request.json

    for d in dispositivos:

        if d["id"] == id:

            d["nome"] = dados["nome"]
            d["ip"] = dados["ip"]

            return jsonify(d)

    return jsonify({"erro":"Nao encontrado"}),404

@app.route("/dispositivos/<int:id>", methods=["DELETE"])
def remover(id):

    for d in dispositivos:

        if d["id"] == id:

            dispositivos.remove(d)

            return jsonify({
                "mensagem":"Removido"
            })

    return jsonify({"erro":"Nao encontrado"}),404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
