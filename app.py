from flask import Flask, jsonify, request, abort

app = Flask(__name__)

news = [
    {"id": 0, "title": "Bienvenida", "content": "Esta es la primera noticia"},
    {"id": 1, "title": "Hello Flask", "content": "My first post"},
    {"id": 2, "title": "Breaking News", "content": "Flask API funcionando"},
]

next_id = 3


@app.route("/", methods=["GET"])
def index():
	pass

@app.route("/news", methods=["GET"])
def list_news():
	return jsonify({"count": len(news), "items": news})

@app.route("/news", methods=["POST"])
def create_news():
    global next_id, news

    data = request.json
    if not data or "title" not in data or "content" not in data:
        abort(400, description="Se requiere 'title' y 'content'")

    # construir la nueva noticia
    new_item = {
        "id": next_id,
        "title": data["title"],
        "content": data["content"]
    }

    # guardar en la lista
    news.append(new_item)
    next_id += 1

    return jsonify(new_item), 201


@app.route("/news/<int:item_id>", methods=["PUT"])
def update_news(item_id: int):
	item = news[item_id]
	data = request.json
	for key in ("title", "content"):
		if key in data:
			item[key] = data[key]
	return jsonify(item)

@app.route("/news/<int:item_id>", methods=["DELETE"])
def delete_news(item_id: int):
	del news[item_id]
	return jsonify({"status": "deleted", "id": item_id})

if __name__ == "__main__":
	app.run(threaded=True, host="0.0.0.0", port=3000)
