import customtkinter as ctk

from cryptography.fernet import Fernet

#gerando chave
chave = Fernet.generate_key()

print(f"essa é a chave:{chave}")

f = Fernet(chave)




#definição de padrão
ctk.set_appearance_mode('dark')


#criar janela
janela = ctk.CTk() 

janela.title('Seu decodificador de mensagens')

janela.geometry('1500x500')
#criptografando_--------------------------------------------------------------------------------
#criar campos

#campo mensagem
mensagem=ctk.CTkEntry(janela,placeholder_text="Digite sua mensagem",width=200,height=50,) 

mensagem.pack(pady=10)
 
def cripto(): 
    rcoleta =mensagem.get() #recebe mensagem e passa para coleta
    
    b = bytes(rcoleta, 'utf-8')#passa coleta para bytes
    
    
   
    mensagem_cripto = f.encrypt(b)#criptografa a coleta
    
    
    
    sucesso=ctk.CTkLabel(janela,text="criptografia feita com sucesso",text_color="green")
    
    sucesso.pack()
    
    sucesso=ctk.CTkLabel(janela,text=f'guarde essa chave: {chave.decode("utf-8")} essa é sua mensagem :{mensagem_cripto}',text_color="green")
    print(f"essa é a mensagem{mensagem_cripto}")
    
    sucesso.pack()


#campo botão
botao= ctk.CTkButton(janela,text="criptografar",command=cripto)

botao.pack(pady=10)

#---------------------------------------------------------------------------------------------------






#descriptografando---------------------------------------------------------------------------------------
#campo chave do usuário
campo_chave=ctk.CTkEntry(janela,placeholder_text="Digite sua chave",width=200,height=50,) 

campo_chave.pack()

#campo cmensagem criptografado do usuário
campo_decript=ctk.CTkEntry(janela,placeholder_text="Digite sua mensagem criptografada ",width=200,height=50,) 

campo_decript.pack(pady=10)

def decript():
    ccampo_chave =campo_chave.get() #coleta campo chave
    print (ccampo_chave)
    
    ccampo_decript=campo_decript.get() #coleta campo da mensagem encriptada
    print(ccampo_decript)

    chave_usuario = campo_chave.get().encode('utf-8')  # pega a chave e converte para bytes
    f_usuario = Fernet(chave_usuario)  # cria Fernet com a chave do usuário
    
    mensagem_descriptografada = f_usuario.decrypt(ccampo_decript).decode('utf-8')#descriptografa com chave do usuário
    
    #ccampo_decript.encode("utf-8")#passa os dados para bytes
    #mensagem_descriptografada = f.decrypt(ccampo_decript)#decripta sua mensagem
    
    
    sucesso_decript=ctk.CTkLabel(janela,text=f'essa é sua mensagem descriptografada:{mensagem_descriptografada}',text_color="green")#exibe sua mensagem descriptografada
    
    sucesso_decript.pack()


#campo botão
botao_decript= ctk.CTkButton(janela,text="descripitorafar",command=decript)



botao_decript.pack(pady=10)


import pyfiglet

assinatura = pyfiglet.figlet_format("@jgbarreiros")#prompzinho de assinatura
print(assinatura)









#iniciar
janela.mainloop()

#feito por jgbarreiros
#https://github.com/jgbarreiros