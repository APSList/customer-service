# Customer Service (gRPC)

Ta repozitorij vsebuje gRPC strežnik v Pythonu za upravljanje s podatki o strankah in izmenjavo podatkov preko protobuf/grpc.

## Predpogoji
- Python 3.12+
- pip
- `venv` za navidezna okolja
- (opcijsko) Docker za zagon v kontejnerju

---

## Lokalni zagon

1. Ustvarite in aktivirajte navidezno okolje:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Namestite odvisnosti:
```bash
pip install -r requirements.txt
```

3. (Opcijsko) Generirajte protobuf datoteke, če ste spremenili definicije v `proto/`:
```bash
scripts/generate_proto.sh
```

4. Zaženite strežnik:
```bash
make run
```

Privzeta gRPC vrata so 50051 (če konfiguracija v `src`/`server.py` uporablja drugo, prilagodite).

---

## Docker

1. Zgradi sliko:
```bash
docker build -t customer-service .
```

2. Zaženi kontejner (mapiranje vrat 50051):
```bash
docker run -p 50051:50051 customer-service
```

---

## Testiranje
Testi so v mapi `tests/`.
Zaženite jih z:
```bash
pytest
```
