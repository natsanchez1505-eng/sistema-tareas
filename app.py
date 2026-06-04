from flask import Flask, request
import os

app = Flask(__name__)

tareas = []

@app.route('/')
def inicio():

    html = """
    <h1>Lista de Tareas</h1>

    <form action='/agregar' method='post'>
        <input name='tarea'>
        <button>Agregar</button>
    </form>

    <h2>Tareas Registradas</h2>
    """

    for tarea in tareas:
        html += f"<li>{tarea}</li>"

    return html


@app.route('/agregar', methods=['POST'])
def agregar():

    tarea = request.form['tarea']
    tareas.append(tarea)

    return """
    <script>
    window.location='/'
    </script>
    """


if __name__ == '__main__':
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=puerto)