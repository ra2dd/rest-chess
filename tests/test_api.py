import pytest
from solver.app import app
from solver.move_endpoints_helpers import validate_field


def test_get_moves():
    client = app.test_client()
    response = client.get("/api/v1/knight/d4")
    content = response.get_json()
    content["availableMoves"] = set(content["availableMoves"])
    expected_content = {
        "availableMoves": {"C6", "E6", "F3", "F5", "C2", "E2", "B3", "B5"},
        "error": None,
        "figure": "knight",
        "currentField": "D4",
    }
    assert response.status_code == 200
    assert expected_content == content


def test_get_moves_invalid_field():
    client = app.test_client()
    response = client.get("/api/v1/knight/d11")
    content = response.get_json()
    expected_content = {
        "availableMoves": [],
        "error": "Field does not exist.",
        "figure": "knight",
        "currentField": "D11",
    }
    assert response.status_code == 409
    assert expected_content == content


def test_get_moves_invalid_figure():
    client = app.test_client()
    response = client.get("/api/v1/tower/d4")
    content = response.get_json()
    expected_content = {
        "availableMoves": [],
        "error": "Figure does not exist.",
        "figure": "tower",
        "currentField": "D4",
    }
    assert response.status_code == 404
    assert expected_content == content


@pytest.mark.parametrize(
    "url, expected_content, status_code",
    [
        # Valid move
        (
            "/api/v1/knight/d4/c6",
            {
                "move": "valid",
                "figure": "knight",
                "error": None,
                "currentField": "D4",
                "destField": "C6",
            },
            200,
        ),
        # Invalid move
        (
            "/api/v1/knight/d4/c8",
            {
                "move": "invalid",
                "figure": "knight",
                "error": "Current move is not permitted.",
                "currentField": "D4",
                "destField": "C8",
            },
            409,
        ),
        # Invalid current field
        (
            "/api/v1/knight/k10/c6",
            {
                "move": None,
                "figure": "knight",
                "error": "Current field does not exist.",
                "currentField": "K10",
                "destField": "C6",
            },
            409,
        ),
        # Invalid dest field
        (
            "/api/v1/knight/d4/c13",
            {
                "move": None,
                "figure": "knight",
                "error": "Destination field does not exist.",
                "currentField": "D4",
                "destField": "C13",
            },
            409,
        ),
        # Invalid figure
        (
            "/api/v1/tower/d4/c6",
            {
                "move": None,
                "figure": "tower",
                "error": "Figure does not exist.",
                "currentField": "D4",
                "destField": "C6",
            },
            404,
        ),
    ],
)
def test_valid_move(url, status_code, expected_content):
    client = app.test_client()
    response = client.get(url)
    content = response.get_json()

    assert response.status_code == status_code
    assert expected_content == content


def test_validate_field():
    assert validate_field("DD") is False
    assert validate_field("K9") is False
