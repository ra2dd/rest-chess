# REST Chess solver

Prosta aplikacja REST wspomagająca grę w szachy.

## Uruchomienie

### Z użyciem Dockera

```sh
docker compose up
```

### Lokalnie

```sh
mkvirtualenv {nazwa_środowiska}
pip3 install -r requirements.txt
python3 -m solver.app
```

## Testowanie
```sh
pytest ./tests
```

## Formatowanie i Lintowanie

Automatycznie przy każdym commicie przy użyciu hooka git

```sh
pre-commit install
```

## Przykładowe zapytania

```
curl http://localhost:5000/api/v1/knight/e4
curl http://localhost:5000/api/v1/knight/e4/d6
```
