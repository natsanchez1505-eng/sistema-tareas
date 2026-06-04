from flask import Flask, request
import os

app = Flask(__name__)

tareas = []

@app.route('/')
def inicio():

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sistema de Tareas Cloud</title>

        <style>

            body{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg,#0f172a,#1e3a8a);
                color:white;
                text-align:center;
                margin:0;
                padding:40px;
            }

            .contenedor{
                max-width:700px;
                margin:auto;
                background:white;
                color:#333;
                padding:30px;
                border-radius:15px;
                box-shadow:0px 0px 20px rgba(0,0,0,0.3);
            }

            h1{
                color:#2563eb;
            }

            input{
                width:70%;
                padding:12px;
                border-radius:8px;
                border:1px solid #ccc;
                margin-right:10px;
            }

            button{
                padding:12px 20px;
                background:#2563eb;
                color:white;
                border:none;
                border-radius:8px;
                cursor:pointer;
            }

            button:hover{
                background:#1d4ed8;
            }

            ul{
                list-style:none;
                padding:0;
            }

            li{
                background:#eff6ff;
                margin:10px 0;
                padding:12px;
                border-radius:8px;
                font-weight:bold;
            }

            .titulo{
                font-size:18px;
                color:#64748b;
            }

        </style>

    </head>

    <body>

        <div class="contenedor">

            <h1>☁️ Sistema de Tareas en la Nube</h1>

            <p class="titulo">
                Proyecto de Desarrollo Ágil + DevOps + PaaS
            </p>

            <form action="/agregar" method="post">

                <input
                    type="text"
                    name="tarea"
                    placeholder="Ingrese una tarea..."
                    required>

                <button type="submit">
                    Agregar
                </button>

            </form>

            <hr>

            <h2>📋 Tareas Registradas</h2>

            <ul>
    """

    for tarea in tareas:
        html += f"<li>✅ {tarea}</li>"

    html += """
            </ul>

        </div>

    </body>
    </html>
    """

    return html


@app.route('/agregar', methods=['POST'])
def agregar():

    tarea = request.form['tarea']
    tareas.append(tarea)

    return """
    <script>
        window.location.href='/';
    </script>
    """


if __name__ == '__main__':
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=puerto, debug=True)
    