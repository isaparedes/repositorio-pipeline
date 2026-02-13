from flask import Flask
import os

app = Flask(__name__)

FILE_PATH = "/data/notes.txt"

@app.get("/")
def hello():
    return "API activa"

@app.post("/add/<note>")
def add(note):
    with open(FILE_PATH, "a") as f:
        f.write(note + "\n")
    return "Nota agregada"

@app.get("/list")
def get_all():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as f:
        notes = f.read().splitlines()

    return notes

@app.delete("/clear")
def clear_notes():
    open(FILE_PATH, "w").close()
    return "Notas eliminadas"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
