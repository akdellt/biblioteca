from database import registrar, login, nome_user, add_exemplar, del_exemplar, edit_exemplar, todos_exemplares, filtrar_status, pesquisar
from tkinter import *


#CONFIGURAÇÕES DA JANELA PRINCIPAL
janela = Tk()
janela.title("Biblioteca Pessoal")


#LIMPA INFORMAÇÕES DA TELA
for widget in janela.winfo_children():
    widget.grid_forget()


# TELA DE INICIAL DE REGISTRO
def tela_registro():
    titulo = Label(janela, text="Organize a sua biblioteca pessoal agora!")
    titulo.grid(column=0, row=0, pady=10)

    label_nome = Label(janela, text="Nome")
    label_nome.grid(column=0, row=1, sticky="w", padx=10)
    entry_nome = Entry(janela)
    entry_nome.grid(column=1, row=1, padx=10)

    label_email = Label(janela, text="Email:")
    label_email.grid(column=0, row=2, sticky="w", padx=10)
    entry_email = Entry(janela)
    entry_email.grid(column=1, row=2, padx=10)

    label_senha = Label(janela, text="Senha:")
    label_senha.grid(column=0, row=3, sticky="w", padx=10)
    entry_senha = Entry(janela, show="*")
    entry_senha.grid(column=1, row=3, padx=10)

    mensagem = Label(janela, text="")
    mensagem.grid(column=0, row=4, columnspan=2)

    def registro():
        nome =  entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()

        if registrar(nome, email, senha):
            mensagem.config(text="Usuário registrado, seja bem vindo!", fg="green")
        else:
            mensagem.config(text="Erro ao registrar, e-mail já existe.", fg="red")

    botao_cadastro = Button(janela, text="Registrar", command=registro)
    botao_cadastro.grid(column=0, row=5, padx=10, pady=10)

    botao_login = Button(janela, text="Login", command=tela_login)
    botao_login.grid(column=1, row=5, padx=10, pady=10)


# CONFIGURAÇÕES TELA DE LOGIN
def tela_login():
    for widget in janela.winfo_children():
        widget.grid_forget()

    titulo = Label(janela, text="Organize a sua biblioteca pessoal agora!")
    titulo.grid(column=0, row=0, pady=10)

    label_email = Label(janela, text="Email:")
    label_email.grid(column=0, row=1, sticky="w", padx=10)
    entry_email = Entry(janela)
    entry_email.grid(column=1, row=1, padx=10)

    label_senha = Label(janela, text="Senha:")
    label_senha.grid(column=0, row=2, sticky="w", padx=10)
    entry_senha = Entry(janela, show="*")
    entry_senha.grid(column=1, row=2, padx=10)

    mensagem = Label(janela, text="")
    mensagem.grid(column=0, row=3, columnspan=2)

    def entrar():
        email = entry_email.get()
        senha = entry_senha.get()

        if login(email, senha):
            mensagem.config(text="Login realizado com sucesso!", fg="green")
            tela_acervo()
        else:
            mensagem.config(text="E-mail ou senha incorretos.", fg="red")

    botao_login = Button(janela, text="Login", command=entrar)
    botao_login.grid(column=0, row=4, columnspan=2, pady=10)



#CONFIGURAÇÕES TELA ACERVO
def tela_acervo():
    for widget in janela.winfo_children():
        widget.grid_forget()


    #FUNÇÃO DE ATUALIZAR LISTA APRESENTADA
    def atualizar():
        for widget in bloco_exemplares.winfo_children():
            widget.destroy()

        exemplares = todos_exemplares()
        for i, exemplar in enumerate(exemplares):
            label_exemplar = Label(bloco_exemplares, text=f"ID: {exemplar[0]} -- Título: {exemplar[1]} -- Categoria: {exemplar[2]} -- Autor: {exemplar[3]}", width=102)
            label_exemplar.grid(column=0, row=i, padx=2, pady=2)


    #FUNÇÃO DE PESQUISAR EXEMPLAR
    def pesquisar_exemplar():
        busca = entry_pesquisa.get()
        exemplares = pesquisar(busca)

        mensagem = Label(janela, text="")
        mensagem.grid(column=0, row=1, columnspan=2)
        
        for widget in bloco_exemplares.winfo_children():
            widget.destroy()

        if exemplares:
            for i, exemplar in enumerate(exemplares):
                label_exemplar = Label(bloco_exemplares, text=f"ID: {exemplar[0]} -- Título: {exemplar[1]} -- Categoria: {exemplar[2]} -- Autor: {exemplar[3]}", width=102)
                label_exemplar.grid(row=i, column=0, padx=2, pady=2)
        else:
            print("")


    #FUNÇÃO DE FILTRAR EXEMPLARES POR SEU STATUS (EMPRESTADO OU DISPONÍVEL)
    def filtrar_exemplares(status):
        exemplares = filtrar_status(status)
        
        for widget in bloco_exemplares.winfo_children():
            widget.destroy()

        if exemplares:
            for i, exemplar in enumerate(exemplares):
                label_exemplar = Label(bloco_exemplares, text=f"ID: {exemplar[0]} -- Título: {exemplar[1]} -- Categoria: {exemplar[2]} -- Autor: {exemplar[3]}", width=102)
                label_exemplar.grid(row=i, column=0, padx=2, pady=2)
        else:
            print("Filtro", "Nenhum exemplar encontrado.")


    #BLOCOS - FRAMES
    #BLOCO 1 DE TÍTULO
    bloco_titulo = Frame(janela, bg="grey", width=150, height=100)
    bloco_titulo.grid(column=0, row=0, padx=10, pady=10)

    titulo_bloco = Label(bloco_titulo, text=f"Biblioteca de {nome_user()}")
    titulo_bloco.grid(column=0, row=0)

    #BLOCO DE BOTÕES
    bloco_botoes = Frame(janela, bg="grey", width=150, padx=5, pady=5)
    bloco_botoes.grid(column=0, row=1, padx=10, pady=10)

    botao_adicionar = Button(bloco_botoes, text="Adicionar", width=33, command=tela_adicionar)
    botao_adicionar.grid(column=1, row=0)

    botao_editar = Button(bloco_botoes, text="Editar", width=33, command=tela_editar)
    botao_editar.grid(column=2, row=0)

    botao_excluir = Button(bloco_botoes, text="Excluir", width=33, command=tela_excluir)
    botao_excluir.grid(column=3, row=0)


    #BLOCO DE FILTROS E BUSCA
    bloco_filtros = Frame(janela, bg="grey", width=150, padx=5, pady=5)
    bloco_filtros.grid(column=0, row=2, padx=10, pady=10)

    filtro_todos = Button(bloco_filtros, text="Todos", width=20, command=atualizar)
    filtro_todos.grid(column=0, row=0)

    filtro_disponiveis = Button(bloco_filtros, text="Disponíveis", width=20, command=lambda: filtrar_exemplares(0))
    filtro_disponiveis.grid(column=1, row=0)

    filtro_emprestados = Button(bloco_filtros, text="Emprestados", width=20, command=lambda: filtrar_exemplares(1))
    filtro_emprestados.grid(column=2, row=0)

    entry_pesquisa = Entry(bloco_filtros, width=30)
    entry_pesquisa.grid(column=3, row=0, padx=5)
    botao_pesquisa = Button(bloco_filtros, width=10, text="Buscar", command=pesquisar_exemplar)
    botao_pesquisa.grid(column=4, row=0)

    #BLOCO DE EXEMPLARES
    bloco_exemplares = Frame(janela, bg="grey", width=150, padx=5, pady=5)
    bloco_exemplares.grid(column=0, row=3, padx=10, pady=10)


#CONFIGURAÇÕES TELA DE ADICIONAR EXEMPLAR
def tela_adicionar():
    janela_add = Toplevel(janela)
    janela_add.title("Adicionar Exemplar")

    label_titulo = Label(janela_add, text="Título:")
    label_titulo.grid(column=0, row=1, sticky="w")
    entry_titulo = Entry(janela_add)
    entry_titulo.grid(column=1, row=1, sticky="w")

    label_categoria = Label(janela_add, text="Categoria:")
    label_categoria.grid(column=0, row=2, sticky="w")
    var_categoria = StringVar()
    var_categoria.set("")
    categorias = ["Livro", "Artigo", "Revista"]
    opcoes_categorias = OptionMenu(janela_add, var_categoria, *categorias)
    opcoes_categorias.grid(column=1, row=2, sticky="w")

    label_autor = Label(janela_add, text="Autor:")
    label_autor.grid(column=0, row=3, sticky="w")
    entry_autor = Entry(janela_add)
    entry_autor.grid(column=1, row=3, sticky="w")

    label_ano = Label(janela_add, text="Ano:")
    label_ano.grid(column=0, row=4, sticky="w")
    entry_ano = Entry(janela_add)
    entry_ano.grid(column=1, row=4, sticky="w")

    label_paginas = Label(janela_add, text="Páginas:")
    label_paginas.grid(column=0, row=5, sticky="w")
    entry_paginas = Entry(janela_add)
    entry_paginas.grid(column=1, row=5, sticky="w")

    emprestado_var = IntVar()
    Checkbutton(janela_add, text="Emprestado", variable=emprestado_var).grid(column=1, row=6, pady=5)

    mensagem = Label(janela_add, text="")
    mensagem.grid(column=0, row=7, columnspan=2)


    #FUNÇÃO DE ADICIONAR EXEMPLAR
    def adicionar():
        titulo = entry_titulo.get()
        categoria = var_categoria.get()
        autor = entry_autor.get()
        ano = entry_ano.get()
        paginas = entry_paginas.get()
        emprestado = emprestado_var.get()

        if add_exemplar(titulo, categoria, autor, ano, paginas, emprestado):
            mensagem.config(text="Exemplar adicionado!", fg="green")
            entry_titulo.delete(0, 'end')
            var_categoria.set("")
            entry_autor.delete(0, 'end')
            entry_ano.delete(0, 'end')
            entry_paginas.delete(0, 'end')
            emprestado_var.set(0)
        else:
            mensagem.config(text="Exemplar já existe.", fg="red")

    botao_add = Button(janela_add, text="Adicionar Exemplar", command=adicionar)
    botao_add.grid(column=0, row=8, pady=10)

    botao_voltar = Button(janela_add, text="Voltar", command=janela_add.destroy)
    botao_voltar.grid(column=1, row=8, pady=10)


#CONFIGURAÇÕES DE TELA DE EXCLUSÃO DE EXEMPLAR
def tela_excluir():
    janela_exc = Toplevel(janela)
    janela_exc.title("Excluir exemplar")

    label_id = Label(janela_exc, text="ID:")
    label_id.grid(column=0, row=2, sticky="w")
    entry_id = Entry(janela_exc)
    entry_id.grid(column=1, row=2, sticky="w")

    mensagem = Label(janela_exc, text="")
    mensagem.grid(column=0, row=3, columnspan=2)

    #FUNÇÃO DE EXCLUIR EXEMPLAR
    def excluir():
        try:
            id = int(entry_id.get())
            if del_exemplar(id):
                mensagem.config(text="Exemplar deletado.", fg="green")
            else:
                mensagem.config(text="Erro a excluir.", fg="red")
        except ValueError:
            mensagem.config(text="Id inválido.", fg="red")

    botao_add = Button(janela_exc, text="Excluir Exemplar", command=excluir)
    botao_add.grid(column=0, row=7, pady=10)

    botao_voltar = Button(janela_exc, text="Voltar", command=janela_exc.destroy)
    botao_voltar.grid(column=1, row=7, pady=10)


#CONFIGURAÇÃO DE TELA DE EDIÇÃO DO EXEMPLAR
def tela_editar():
    janela_edit = Toplevel(janela)
    janela_edit.title("Editar exemplar")

    label_busca = Label(janela_edit, text="Título ou ID:")
    label_busca.grid(column=0, row=0, sticky="w")
    entry_busca = Entry(janela_edit)
    entry_busca.grid(column=1, row=0, sticky="w")

    mensagem_busca = Label(janela_edit, text="")
    mensagem_busca.grid(column=0, row=1, columnspan=2)

    label_id = Label(janela_edit, text="ID:")
    label_id.grid(column=0, row=2, sticky="w")
    entry_id = Entry(janela_edit, state="readonly")
    entry_id.grid(column=1, row=2, sticky="w")

    label_titulo = Label(janela_edit, text="Título:")
    label_titulo.grid(column=0, row=3, sticky="w")
    entry_titulo = Entry(janela_edit)
    entry_titulo.grid(column=1, row=3, sticky="w")

    label_categoria = Label(janela_edit, text="Categoria:")
    label_categoria.grid(column=0, row=4, sticky="w")
    var_categoria = StringVar()
    var_categoria.set("")
    categorias = ["Livro", "Artigo", "Revista"]
    opcoes_categorias = OptionMenu(janela_edit, var_categoria, *categorias)
    opcoes_categorias.grid(column=1, row=4, sticky="w")

    label_autor = Label(janela_edit, text="Autor:")
    label_autor.grid(column=0, row=5, sticky="w")
    entry_autor = Entry(janela_edit)
    entry_autor.grid(column=1, row=5, sticky="w")

    label_ano = Label(janela_edit, text="Ano:")
    label_ano.grid(column=0, row=6, sticky="w")
    entry_ano = Entry(janela_edit)
    entry_ano.grid(column=1, row=6, sticky="w")

    label_paginas = Label(janela_edit, text="Páginas:")
    label_paginas.grid(column=0, row=7, sticky="w")
    entry_paginas = Entry(janela_edit)
    entry_paginas.grid(column=1, row=7, sticky="w")

    emprestado_var = IntVar()
    Checkbutton(janela_edit, text="Emprestado", variable=emprestado_var).grid(column=1, row=8, pady=5)

    mensagem_edicao = Label(janela_edit, text="")
    mensagem_edicao.grid(column=0, row=9, columnspan=2)


    #FUNÇÃO DE BUSCAR EXEMPLAR
    def buscar_exemplar():
        busca = entry_busca.get()
        exemplares = pesquisar(busca)

        if exemplares:
            exemplar = exemplares[0]
            entry_id.config(state="normal")
            entry_id.delete(0, END)
            entry_id.insert(0, exemplar[0])
            entry_id.config(state="readonly")

            entry_titulo.delete(0, END)
            entry_titulo.insert(0, exemplar[1])

            var_categoria.set(exemplar[2])

            entry_autor.delete(0, END)
            entry_autor.insert(0, exemplar[3])

            entry_ano.delete(0, END)
            entry_ano.insert(0, exemplar[4])

            entry_paginas.delete(0, END)
            entry_paginas.insert(0, exemplar[5])

            emprestado_var.set(bool(exemplar[6]))

            mensagem_busca.config(text="Exemplar encontrado!", fg="green")
        else:
            mensagem_busca.config(text="Exemplar não encontrado.", fg="red")

    #FUNÇÃO DE ATUALIZAR INFORMAÇÕES
    def salvar_edicao():
        try:
            id_exemplar = int(entry_id.get())
            titulo = entry_titulo.get()
            categoria = var_categoria.get()
            autor = entry_autor.get()
            ano = entry_ano.get()
            paginas = entry_paginas.get()
            emprestado = emprestado_var.get()

            if edit_exemplar(id_exemplar, titulo, categoria, autor, ano, paginas, emprestado):
                mensagem_edicao.config(text="Exemplar atualizado com sucesso!", fg="green")
            else:
                mensagem_edicao.config(text="Erro ao atualizar o exemplar.", fg="red")
        except ValueError:
            mensagem_edicao.config(text="ID inválido.", fg="red")

    botao_buscar = Button(janela_edit, text="Buscar", command=buscar_exemplar)
    botao_buscar.grid(column=2, row=0, padx=10)

    botao_salvar = Button(janela_edit, text="Salvar Alterações", command=salvar_edicao)
    botao_salvar.grid(column=0, row=10, columnspan=2, pady=10)

    botao_voltar = Button(janela_edit, text="Voltar", command=janela_edit.destroy)
    botao_voltar.grid(column=0, row=11, columnspan=2, pady=5)


# MOSTRA TELA INICIAL DE REGISTRO
tela_registro()


janela.mainloop()