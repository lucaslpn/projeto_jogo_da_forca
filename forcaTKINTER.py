from tkinter import *

root = Tk()

class App:
    
    def __init__(self):
        
        self.root = root
        self.tela()
        self.frames()
        self.botoes()
        root.mainloop()
        
    def tela(self):
        self.root.title('JOGO DA FORCA') # definir titulo do app
        self.root.configure(background='#BEBEBE') # definir a cor de fundo
        self.root.geometry('1000x600') # definir tamanho da janela

    def frames(self):
        self.frame_1 = Frame(self.root, bd=4, bg='white', highlightbackground='black', highlightthickness=2)
        self.frame_1.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.4)

        #self.frame_2 = Frame(self.root, bd=4, bg='black', highlightbackground='black', highlightthickness=2)
        #self.frame_2.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.5)
    
    def botoes(self):
        self.bt_limpar = Button(text='SAIR', command=root.destroy, border=4, fg='black', font=('Arial', 9, 'bold'))
        self.bt_limpar.place(relx=0.45, rely=0.8, relwidth=0.1, relheight=0.1) # y = altura, x = comprimento

        # criação da label e entrada do código
        self.lb_codigo = Label(text='INSIRA UMA LETRA', background='#BEBEBE', font=('Arial', 10, 'bold'))
        self.lb_codigo.place(relx=0.44, rely=0.45)

        # metodo input do tkinter
        self.input_entry = Entry()
        self.input_entry.place(relx=0.48, rely=0.49, relwidth=0.04)
    
    
    

    
App()