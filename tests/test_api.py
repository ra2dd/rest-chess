from solver.app import app


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


def test_valid_move():
    client = app.test_client()
    response = client.get("/api/v1/knight/d4/c6")
    content = response.get_json()
    expected_content = {
        "move": "valid",
        "figure": "knight",
        "error": None,
        "currentField": "D4",
        "destField": "C6",
    }
    assert response.status_code == 200
    assert expected_content == content


def test_invalid_move():
    client = app.test_client()
    response = client.get("/api/v1/knight/d4/c8")
    content = response.get_json()
    expected_content = {
        "move": "invalid",
        "figure": "knight",
        "error": "Current move is not permitted.",
        "currentField": "D4",
        "destField": "C8",
    }
    assert response.status_code == 409
    assert expected_content == content


def test_valid_move_invalid_fields():
    client = app.test_client()
    response = client.get("/api/v1/knight/k10/c6")
    content = response.get_json()
    expected_content = {
        "move": None,
        "figure": "knight",
        "error": "Current field does not exist.",
        "currentField": "K10",
        "destField": "C6",
    }
    assert response.status_code == 409
    assert expected_content == content

    response = client.get("/api/v1/knight/d4/c13")
    content = response.get_json()
    expected_content = {
        "move": None,
        "figure": "knight",
        "error": "Destination field does not exist.",
        "currentField": "D4",
        "destField": "C13",
    }
    assert response.status_code == 409
    assert expected_content == content


def test_valid_move_invalid_figure():
    client = app.test_client()
    response = client.get("/api/v1/tower/d4/c6")
    content = response.get_json()
    expected_content = {
        "move": None,
        "figure": "tower",
        "error": "Figure does not exist.",
        "currentField": "D4",
        "destField": "C6",
    }
    assert response.status_code == 404
    assert expected_content == content
