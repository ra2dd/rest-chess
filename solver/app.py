from flask import Flask, jsonify
from solver.utils import validate_field, get_figure_object

app = Flask(__name__)


@app.route("/api/v1/<figure>/<field>", methods=["GET"])
def get_moves(figure: str, field: str):
    if validate_field(field) is False:
        return "bad field"
    field = field.upper()

    object = get_figure_object(figure, field)
    if object is False:
        return "bad figure"

    moves = object.list_available_moves()

    response_data = {
        "availableMoves": list(moves),
        "error": None,
        "figure": figure.lower(),
        "currentField": field,
    }
    return jsonify(response_data), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
