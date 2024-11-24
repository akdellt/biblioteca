import smtplib
import random
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def gerar_senha(tamanho = 6):
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def enviar_email(destinatario, assunto, mensagem):
    #CONFIGURAÇÃO
    port = 587
    smtp_server = "smtp.gmail.com"
    remetente = "pessoalbiblioteca684@gmail.com"
    senha = "ozfc nxyo rhvw aktc"

    #MENSAGEM
    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = assunto

    msg.attach(MIMEText(mensagem, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(remetente, senha)

        server.sendmail(remetente, destinatario, msg.as_string())
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
    finally:
        server.quit()


def enviar_email_senha(destinatario):
    senha_aleatoria = gerar_senha()
    assunto = "Recuperação de senha"

    mensagem = f"""\
        Você solicitou a recuperação de senha do seu perfil na Biblioteca Pessoal. 
        Faça login com a senha gerada e crie sua nova senha.
        Senha gerada: {senha_aleatoria}
        """
    enviar_email(destinatario, assunto, mensagem)

    return senha_aleatoria

    

    

    

def enviar_email_emprestimo(destinatario, nome_usuario, nome_livro, nome_destinatario):
    assunto = "Devolução de livro"

    mensagem = f"""\
        Olá {nome_destinatario},

        Tudo bem? Só passando para lembrar que o prazo para devolver o livro {nome_livro} que lhe emprestei está chegando. 
        Se puder, me avise quando conseguir fazer a devolução, ou entre em contato comigo para resolvermos essa questão.

        Atenciosamente,
        {nome_usuario}
        """
    enviar_email(destinatario, assunto, mensagem)
    
