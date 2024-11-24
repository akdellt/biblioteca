from database import buscar_email, nova_senha_aleatoria, nova_senha_criada, registrar, login, nome_user, add_exemplar, del_exemplar, edit_exemplar, todos_exemplares, filtrar_status, pesquisar
from envios import enviar_email_senha, enviar_email_emprestimo
from tkinter import *


#CONFIGURAÇÕES DA JANELA PRINCIPAL
janela = Tk()
janela.title("Biblioteca Pessoal")


#LIMPA INFORMAÇÕES DA TELA
for widget in janela.winfo_children():
    widget.grid_forget()


def tela_recuperacao():
    for widget in janela.winfo_children():
        widget.grid_forget()

    titulo = Label(janela, text="Digite seu email para recuperação de senha:")
    titulo.grid(column=0, row=0, pady=10)

    label_email = Label(janela, text="Email:")
    label_email.grid(column=0, row=1, sticky="w", padx=10)
    entry_email = Entry(janela)
    entry_email.grid(column=1, row=1, padx=10)

    mensagem = Label(janela, text="")
    mensagem.grid(column=0, row=2, columnspan=2)

    def enviar_senha():
        email = entry_email.get()
        if buscar_email(email): 
            senha_aleatoria = enviar_email_senha(email)
            nova_senha_aleatoria(email, senha_aleatoria)
            mensagem.config(text="Senha enviada para o e-mail. Insira a senha gerada e a nova senha.", fg="green")
            tela_nova_senha()
        else:
            mensagem.config(text="E-mail não cadastrado.", fg="red")

    botao_enviar = Button(janela, text="Enviar senha", command=enviar_senha)
    botao_enviar.grid(column=0, row=3, columnspan=2, pady=10)


def tela_nova_senha():
    for widget in janela.winfo_children():
        widget.grid_forget()

    titulo = Label(janela, text="Atualize sua senha:")
    titulo.grid(column=0, row=0, columnspan=2, pady=10)

    label_email = Label(janela, text="Email:")
    label_email.grid(column=0, row=1, sticky="w", padx=10)
    entry_email = Entry(janela)
    entry_email.grid(column=1, row=1, padx=10)

    label_senha_gerada = Label(janela, text="Senha gerada:")
    label_senha_gerada.grid(column=0, row=2, sticky="w", padx=10)
    entry_senha_gerada = Entry(janela, show="*")
    entry_senha_gerada.grid(column=1, row=2, padx=10)

    label_nova_senha = Label(janela, text="Nova senha:")
    label_nova_senha.grid(column=0, row=3, sticky="w", padx=10)
    entry_nova_senha = Entry(janela, show="*")
    entry_nova_senha.grid(column=1, row=3, padx=10)

    mensagem = Label(janela, text="")
    mensagem.grid(column=0, row=4, columnspan=2)

    def atualizar_senha():
        email = entry_email.get()
        senha_gerada = entry_senha_gerada.get()
        nova_senha = entry_nova_senha.get()

        if len(nova_senha) < 6:
            mensagem.config(text="A nova senha deve ter pelo menos 6 caracteres.", fg="red")
            return

        resultado = nova_senha_criada(email, senha_gerada, nova_senha)
        if resultado == True:
            mensagem.config(text="Senha atualizada com sucesso! Faça login novamente.", fg="green")
            tela_login()
        elif resultado == "Senha gerada incorreta":
            mensagem.config(text="Senha gerada incorreta. Tente novamente.", fg="red")
        elif resultado == "Usuário não encontrado":
            mensagem.config(text="Usuário não encontrado. Verifique o e-mail.", fg="red")
        else:
            mensagem.config(text="Erro ao atualizar a senha.", fg="red")

    botao_atualizar = Button(janela, text="Atualizar senha", command=atualizar_senha)
    botao_atualizar.grid(column=0, row=5, columnspan=2, pady=10)



# TELA DE INICIAL DE REGISTRO
def tela_registro():
    for widget in janela.winfo_children():
        widget.grid_forget()

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

    #FUNÇÃO DE REGISTRAR
    def registro():
        nome =  entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()

        resultado = registrar(nome, email, senha)
        if resultado == True:
            mensagem.config(text="Usuário registrado, seja bem vindo!", fg="green")
        elif resultado == "Formato inválido":
            mensagem.config(text="Erro ao registrar, e-mail inválido.", fg="red")
        elif len(senha) < 6:
            mensagem.config(text="A senha deve conter no mínimo 6 caracteres.", fg="red")
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

        resultado = login(email, senha)
        if resultado == True:
            mensagem.config(text="Login realizado com sucesso!", fg="green")
            tela_acervo()
        elif resultado == "Formato inválido":
            mensagem.config(text="E-mail inválido.", fg="red")
        else:
            mensagem.config(text="E-mail ou senha incorretos.", fg="red")

    botao_login = Button(janela, text="Login", command=entrar)
    botao_login.grid(column=0, row=4, columnspan=2, pady=10)

    botao_registrar = Button(janela, text="Registrar", command=tela_registro)
    botao_registrar.grid(column=0, row=5, columnspan=2, pady=10)

    botao_senha = Button(janela, text="Recuperar senha", command=tela_recuperacao)
    botao_senha.grid(column=1, row=5, columnspan=2, pady=10)



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

    botao_adicionar = Button(bloco_botoes, text="Adicionar", width=25, command=tela_adicionar)
    botao_adicionar.grid(column=1, row=0)

    botao_editar = Button(bloco_botoes, text="Editar", width=25, command=tela_editar)
    botao_editar.grid(column=2, row=0)

    botao_excluir = Button(bloco_botoes, text="Excluir", width=25, command=tela_excluir)
    botao_excluir.grid(column=3, row=0)

    botao_excluir = Button(bloco_botoes, text="Devolução", width=25, command=tela_devolucao)
    botao_excluir.grid(column=4, row=0)


    #BLOCO DE FILTROS E BUSCA
    bloco_filtros = Frame(janela, bg="grey", width=150, padx=5, pady=5)
    bloco_filtros.grid(column=0, row=2, padx=10, pady=10)

    filtro_todos = Button(bloco_filtros, text="Todos", width=20, command=atualizar)
    filtro_todos.grid(column=0, row=0)

    filtro_disponiveis = Button(bloco_filtros, text="Disponíveis", width=20, command=lambda: filtrar_exemplares(0))
    filtro_disponiveis.grid(column=1, row=0)

    filtro_emprestados = Button(bloco_filtros, text="Emprestados", width=20, command=lambda: filtrar_exemplares(1))
    filtro_emprestados.grid(column=2, row=0)

    entry_pesquisa = Entry(bloco_filtros, width=31)
    entry_pesquisa.grid(column=3, row=0, padx=10)
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


#FUNÇÃO DE ENVIAR EMAIL DE DEVOLUÇÃO
def tela_devolucao():
    janela_devol = Toplevel(janela)
    janela_devol.title("Devolução")

    titulo = Label(janela_devol, text="Envio de lembrete de devolução de livro")
    titulo.grid(row=0, column=0, columnspan=2, pady=10)

    label_nome = Label(janela_devol, text="Nome do destinatário:")
    label_nome.grid(row=1, column=0, sticky="w", padx=10)
    entry_nome = Entry(janela_devol)
    entry_nome.grid(row=1, column=1, padx=10)

    label_email = Label(janela_devol, text="E-mail do destinatário:")
    label_email.grid(row=2, column=0, sticky="w", padx=10)
    entry_email = Entry(janela_devol)
    entry_email.grid(row=2, column=1, padx=10)

    label_livro = Label(janela_devol, text="Nome do livro:")
    label_livro.grid(row=3, column=0, sticky="w", padx=10)
    entry_livro = Entry(janela_devol)
    entry_livro.grid(row=3, column=1, padx=10)

    def enviar_email_devolucao():
        nome_destinatario = entry_nome.get()
        destinatario = entry_email.get()
        nome_livro = entry_livro.get()
        nome_usuario = nome_user()
        
        livro = pesquisar(nome_livro)

        if destinatario and nome_destinatario and livro and nome_usuario:
            enviar_email_emprestimo(destinatario, nome_usuario, nome_livro, nome_destinatario)
            janela_devol.destroy()
        elif livro is None:
            mensagem.config(text="Você não possui esse livro no acervo.", fg="red")
        else:
            mensagem.config(text="Por favor, preencha todos os campos.", fg="red")

    botao_enviar = Button(janela_devol, text="Enviar Lembrete", command=enviar_email_devolucao)
    botao_enviar.grid(row=4, column=0, columnspan=2, pady=20)

    mensagem = Label(janela_devol, text="")
    mensagem.grid(row=5, column=0, columnspan=2)


# MOSTRA TELA INICIAL DE REGISTRO
tela_registro()


janela.mainloop()