from flask import Flask, request

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
    app.run()