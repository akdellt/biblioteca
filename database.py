import re
import bcrypt
import sqlite3
usuario_logado = None

biblioteca =  sqlite3.connect('biblioteca.db')
cursor = biblioteca.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id integer primary key, nome text not null, email text unique not null, senha text not null)")
cursor.execute("CREATE TABLE IF NOT EXISTS exemplares (id integer primary key, titulo text unique not null, categoria text not null, autor text, ano integer, paginas integer, emprestado boolean default 0, usuario_id integer not null, FOREIGN KEY (usuario_id) REFERENCES usuarios (id))")

#FUNÇÕES DE AUTENTICAÇÃO
def validar_email(email):
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) is not None


def buscar_email(email):
    cursor.execute("SELECT email FROM usuarios WHERE email = ?", (email,))
    return True


def registrar(nome, email, senha):
    if not validar_email(email):
        return "Formato inválido"

    hashed_senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()
    
    try:
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, hashed_senha))
        biblioteca.commit()
        return True
    
    except sqlite3.IntegrityError:
        return False


def login(email, senha):
    global usuario_logado
    if not validar_email(email):
        return "Formato inválido"

    cursor.execute("SELECT id, senha FROM usuarios WHERE email = ?", (email,))
    usuario = cursor.fetchone()

    if usuario:
        usuario_id, hashed_senha = usuario
        if bcrypt.checkpw(senha.encode(), hashed_senha.encode()):
            usuario_logado = usuario_id  
            return True
        else:
            return False
    else:
        return False


def nova_senha_aleatoria(email, senha):
    if not validar_email(email):
        return "Formato inválido"

    hashed_senha_gerada = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

    try:
        cursor.execute("UPDATE usuarios SET senha = ? WHERE email = ?", (hashed_senha_gerada, email))
        biblioteca.commit()
        return True
    
    except sqlite3.IntegrityError:
        return False


def nova_senha_criada(email, senha_gerada, nova_senha):
    if not validar_email(email):
        return "Formato inválido"
    
    cursor.execute("SELECT senha FROM usuarios WHERE email = ?", (email,))
    usuario = cursor.fetchone()

    if usuario:
        senha_atual = usuario[0]
        if bcrypt.checkpw(senha_gerada.encode(), senha_atual.encode()):
            hashed_nova_senha = bcrypt.hashpw(nova_senha.encode(), bcrypt.gensalt()).decode()
            try:
                cursor.execute("UPDATE usuarios SET senha = ? WHERE email = ?", (hashed_nova_senha, email))
                biblioteca.commit()
                return True
            except sqlite3.IntegrityError:
                return False
        else:
            return "Senha gerada incorreta"
    else:
        return "Usuário não encontrado"
    


#FUNÇÃO PARA RESGATAR NOME E QUANTIDADE DE EXEMPLARES
def nome_user():
    cursor.execute("SELECT nome FROM usuarios WHERE id = ?", (usuario_logado,))
    return cursor.fetchone()[0]


# FUNÇÃO DE ADICIONAR EXEMPLAR
def add_exemplar(titulo, categoria, autor, ano, paginas, emprestado):
    try:
        print(f"Usuário logado: {usuario_logado}")  
        cursor.execute("INSERT INTO exemplares (titulo, categoria, autor, ano, paginas, emprestado, usuario_id) VALUES (?, ?, ?, ?, ?, ?, ?)" , (titulo, categoria, autor, ano, paginas, emprestado, usuario_logado))
        biblioteca.commit()
        return True
    except sqlite3.IntegrityError:
        return False


# FUNÇÃO DE EDITAR EXEMPLAR
def edit_exemplar(id, titulo, categoria, autor, ano, paginas, emprestado):
    try:
        cursor.execute("UPDATE exemplares SET titulo = ?, categoria = ?, autor = ?, ano = ?, paginas = ?, emprestado = ? WHERE id = ? AND usuario_id = ?", (titulo, categoria, autor, ano, paginas, emprestado, id, usuario_logado)
        )
        biblioteca.commit()
        return cursor.rowcount > 0  
    except sqlite3.IntegrityError:
        return False


# FUNÇÃO DE DELETAR EXEMPLAR  
def del_exemplar(id):
    try:
        cursor.execute("DELETE FROM exemplares WHERE id = ? AND usuario_id = ?", (id, usuario_logado))
        biblioteca.commit()
        return cursor.rowcount > 0
    except sqlite3.IntegrityError:
        return False


#FUNÇÃO DE VER TODOS EXEMPLARES
def todos_exemplares():
    cursor.execute("SELECT * FROM exemplares WHERE usuario_id = ?", (usuario_logado,))
    exemplares = cursor.fetchall()
    return exemplares


#FUNÇÃO DE FILTRAR EXEMPLARES POR STATUS
def filtrar_status(emprestado):
    cursor.execute("SELECT * FROM exemplares WHERE emprestado = ? AND usuario_id = ?", (emprestado, usuario_logado) )
    exemplares = cursor.fetchall()
    return exemplares


#FUNÇÃO DE BUSCAR EXEMPLARES
def pesquisar(busca):
    cursor.execute("SELECT * FROM exemplares WHERE titulo LIKE ? OR id LIKE ?", (f"%{busca}%", f"%{busca}%"))
    exemplares = cursor.fetchall()
    if not exemplares:
        return None
    return exemplares


