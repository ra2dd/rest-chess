from flask import Flask, jsonify
from solver.utils import validate_field, get_figure_object, create_moves_res

app = Flask(__name__)


@app.errorhandler(500)
def handle_500_error(e):
    response_data = {
        "error": "Internal error. Try again later or contact site administration."
    }
    return jsonify(response_data), 500


@app.route("/api/v1/<figure>/<field>", methods=["GET"])
def get_moves(figure: str, field: str):
    field = field.upper()
    if validate_field(field) is False:
        return create_moves_res(figure, field, error="Field does not exist."), 409

    object = get_figure_object(figure, field)
    if object is False:
        return create_moves_res(figure, field, error="Figure does not exist."), 404

    moves = object.list_available_moves()
    return create_moves_res(figure, field, moves=moves), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
