from flask import Flask, request, redirect, url_for, session, render_template_string
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "chave-local-desenvolvimento")
DB = "cadastro.db"

HTML = """
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{{ titulo }}</title>
<style>
body{font-family:Arial;background:#f2f4f7;max-width:420px;margin:60px auto;padding:20px}
main{background:white;padding:30px;border-radius:12px;box-shadow:0 4px 20px #ccc}
input,button{width:100%;padding:12px;margin:8px 0;box-sizing:border-box}
button{background:#222;color:white;border:0;border-radius:6px}
a{display:block;text-align:center;margin-top:15px}
.erro{color:#b00020}.ok{color:#16733b}
</style>
</head><body><main>{{ conteudo|safe }}</main></body></html>
"""

def db():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c

def iniciar_banco():
    c = db()
    c.execute("""CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    )""")
    c.commit()
    c.close()

def pagina(titulo, conteudo):
    return render_template_string(HTML, titulo=titulo, conteudo=conteudo)

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    erro = ""
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")
        if not nome or not email or not senha:
            erro = "Preencha todos os campos."
        elif len(senha) < 6:
            erro = "A senha deve ter pelo menos 6 caracteres."
        else:
            try:
                c = db()
                c.execute(
                    "INSERT INTO usuarios(nome,email,senha) VALUES(?,?,?)",
                    (nome, email, generate_password_hash(senha))
                )
                c.commit()
                c.close()
                return redirect(url_for("login", cadastro="ok"))
            except sqlite3.IntegrityError:
                erro = "Este e-mail já está cadastrado."

    conteudo = f"""
    <h1>Criar cadastro</h1>
    <form method="post">
      <input name="nome" placeholder="Nome" required>
      <input name="email" type="email" placeholder="E-mail" required>
      <input name="senha" type="password" placeholder="Senha" required>
      <button>Cadastrar</button>
    </form>
    <p class="erro">{erro}</p>
    <a href="{url_for('login')}">Já tenho uma conta</a>
    """
    return pagina("Cadastro", conteudo)

@app.route("/login", methods=["GET", "POST"])
def login():
    mensagem = '<p class="ok">Cadastro realizado! Faça login.</p>' if request.args.get("cadastro") == "ok" else ""
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")
        c = db()
        usuario = c.execute("SELECT * FROM usuarios WHERE email=?", (email,)).fetchone()
        c.close()
        if usuario and check_password_hash(usuario["senha"], senha):
            session["usuario_id"] = usuario["id"]
            session["usuario_nome"] = usuario["nome"]
            return redirect(url_for("home"))
        mensagem = '<p class="erro">E-mail ou senha inválidos.</p>'

    conteudo = f"""
    <h1>Login</h1>
    {mensagem}
    <form method="post">
      <input name="email" type="email" placeholder="E-mail" required>
      <input name="senha" type="password" placeholder="Senha" required>
      <button>Entrar</button>
    </form>
    <a href="{url_for('cadastro')}">Criar uma conta</a>
    """
    return pagina("Login", conteudo)

@app.route("/home")
def home():
    if "usuario_id" not in session:
        return redirect(url_for("login"))
    conteudo = f"""
    <h1>Home</h1>
    <p>Olá, <strong>{session["usuario_nome"]}</strong>!</p>
    <p>Login realizado com sucesso.</p>
    <p>Esta é a tela inicial protegida do sistema.</p>
    <a href="{url_for('logout')}">Sair</a>
    """
    return pagina("Home", conteudo)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    iniciar_banco()
    app.run(debug=True)
