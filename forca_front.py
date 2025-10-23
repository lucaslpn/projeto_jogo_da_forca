import customtkinter as ctk
import random
import os

class ForcaGame(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("JOGO DA FORCA")
        self.geometry("800x600")
        self.resizable(False, False)
        self.configure(fg_color="#2b2b2b") # Cor de fundo escura

        self.palavras = self.carregar_palavras("palavras.txt")
        if not self.palavras:
            print("Erro: Nenhuma palavra carregada. Verifique o arquivo palavras.txt")
            self.destroy()
            return

        self.palavra_secreta = ""
        self.letras_corretas = set()
        self.letras_erradas = set()
        self.tentativas_restantes = 5
        self.jogo_ativo = False

        self.criar_widgets()
        self.iniciar_novo_jogo()

    def carregar_palavras(self, filename):
        script_dir = os.path.dirname(__file__)
        filepath = os.path.join(script_dir, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return [palavra.strip().upper() for palavra in f if palavra.strip()]
        except FileNotFoundError:
            print(f"Arquivo '{filename}' não encontrado em {filepath}.")
            return []

    def iniciar_novo_jogo(self):
        self.palavra_secreta = random.choice(self.palavras)
        self.letras_corretas = set()
        self.letras_erradas = set()
        self.tentativas_restantes = 5
        self.jogo_ativo = True
        self.atualizar_interface()
        self.entrada_letra.delete(0, ctk.END)
        self.entrada_letra.focus_set()
        self.mensagem_label.configure(text="")
        self.entrada_palavra.delete(0, ctk.END)

    def criar_widgets(self):
        self.title_label = ctk.CTkLabel(self, text="JOGO DA FORCA", font=("Arial", 30, "bold"), text_color="#00BFFF")
        self.title_label.pack(pady=20)

        self.palavra_label = ctk.CTkLabel(self, text="", font=("Arial", 40, "bold"), text_color="white")
        self.palavra_label.pack(pady=20)

        self.tentativas_label = ctk.CTkLabel(self, text="", font=("Arial", 20), text_color="#FFD700")
        self.tentativas_label.pack(pady=10)

        self.erradas_label = ctk.CTkLabel(self, text="", font=("Arial", 20), text_color="#FF4500")
        self.erradas_label.pack(pady=10)

        self.entrada_frame = ctk.CTkFrame(self, fg_color="transparent")
        
        self.entrada_letra = ctk.CTkEntry(self.entrada_frame, width=50, height=40, font=("Arial", 24), justify="center", fg_color="#343638", text_color="white", border_color="#00BFFF", border_width=2)
        self.entrada_letra.pack(side=ctk.LEFT, padx=10)
        self.entrada_letra.bind("<Return>", self.processar_palpite_event)

        self.btn_adivinhar = ctk.CTkButton(self.entrada_frame, text="Tentar Letra", command=self.processar_palpite_letra, font=("Arial", 20, "bold"), fg_color="#00BFFF", hover_color="#008ECC")
        self.btn_adivinhar.pack(side=ctk.LEFT, padx=10)

        self.palavra_frame = ctk.CTkFrame(self, fg_color="transparent")
        
        self.entrada_palavra = ctk.CTkEntry(self.palavra_frame, width=250, height=40, font=("Arial", 20), justify="center", fg_color="#343638", text_color="white", border_color="#FFD700", border_width=2)
        self.entrada_palavra.pack(side=ctk.LEFT, padx=10)
        self.entrada_palavra.bind("<Return>", self.processar_palpite_palavra_event)

        self.btn_palavra = ctk.CTkButton(self.palavra_frame, text="Adivinhar Palavra", command=self.processar_palpite_palavra, font=("Arial", 20, "bold"), fg_color="#FFD700", hover_color="#C0A000", text_color="black")
        self.btn_palavra.pack(side=ctk.LEFT, padx=10)

        self.mensagem_label = ctk.CTkLabel(self, text="", font=("Arial", 20, "italic"), text_color="white")
        self.mensagem_label.pack(pady=10)

        self.btn_novo_jogo = ctk.CTkButton(self, text="Novo Jogo", command=self.iniciar_novo_jogo, font=("Arial", 20, "bold"), fg_color="#32CD32", hover_color="#228B22")
        self.btn_novo_jogo.pack(pady=20)

    def atualizar_interface(self):
        palavra_exibida = "".join([letra if letra in self.letras_corretas else "_" for letra in self.palavra_secreta])
        letras_ocultas = palavra_exibida.count("_")
        
        self.palavra_label.configure(text=" ".join(palavra_exibida))
        self.tentativas_label.configure(text=f"Tentativas restantes: {self.tentativas_restantes}")
        self.erradas_label.configure(text=f"Letras erradas: {', '.join(sorted(list(self.letras_erradas)))}")

        if self.jogo_ativo and letras_ocultas <= 4:
            self.palavra_frame.pack(pady=10)
            self.entrada_palavra.configure(state=ctk.NORMAL)
            self.btn_palavra.configure(state=ctk.NORMAL)
            
            self.entrada_frame.pack_forget()
        else:
            self.palavra_frame.pack_forget()
            self.entrada_palavra.configure(state=ctk.DISABLED)
            self.btn_palavra.configure(state=ctk.DISABLED)
            
            if self.jogo_ativo:
                self.entrada_frame.pack(pady=20)
            else:
                self.entrada_frame.pack_forget()


        if not self.jogo_ativo:
            self.entrada_letra.configure(state=ctk.DISABLED)
            self.btn_adivinhar.configure(state=ctk.DISABLED)
            self.palavra_frame.pack_forget() 
            self.entrada_frame.pack_forget() 


    def processar_palpite_event(self, event=None):
        self.processar_palpite_letra()

    def processar_palpite_letra(self):
        if not self.jogo_ativo:
            return

        palpite = self.entrada_letra.get().strip().upper()
        self.entrada_letra.delete(0, ctk.END)

        if not palpite.isalpha() or len(palpite) != 1:
            self.mensagem_label.configure(text="Por favor, insira uma única letra.", text_color="red")
            return

        if palpite in self.letras_corretas or palpite in self.letras_erradas:
            self.mensagem_label.configure(text=f"Você já tentou '{palpite}'.", text_color="orange")
            return

        if palpite in self.palavra_secreta:
            self.letras_corretas.add(palpite)
            self.mensagem_label.configure(text=f"Correto! '{palpite}' está na palavra.", text_color="#32CD32")
        else:
            self.letras_erradas.add(palpite)
            self.tentativas_restantes -= 1
            self.mensagem_label.configure(text=f"Errado! '{palpite}' não está na palavra.", text_color="#FF4500")

        self.verificar_estado_jogo()
        self.atualizar_interface()
        
    def processar_palpite_palavra_event(self, event=None):
        self.processar_palpite_palavra()

    def processar_palpite_palavra(self):
        if not self.jogo_ativo:
            return

        palpite = self.entrada_palavra.get().strip().upper()
        self.entrada_palavra.delete(0, ctk.END)
        
        if not palpite.isalpha() or len(palpite) != len(self.palavra_secreta):
            self.mensagem_label.configure(text="Insira a palavra completa corretamente.", text_color="red")
            return

        if palpite == self.palavra_secreta:
            for letra in self.palavra_secreta:
                self.letras_corretas.add(letra)
            self.mensagem_label.configure(text=f"VITÓRIA! A palavra era '{self.palavra_secreta}'.", text_color="#32CD32")
            self.jogo_ativo = False
        else:
            self.tentativas_restantes = 0
            self.mensagem_label.configure(text=f"Palavra incorreta! Você perdeu.", text_color="red")
            self.jogo_ativo = False

        self.verificar_estado_jogo()
        self.atualizar_interface()

    def verificar_estado_jogo(self):
        palavra_completa = "".join([letra if letra in self.letras_corretas else "_" for letra in self.palavra_secreta])

        if "_" not in palavra_completa:
            self.mensagem_label.configure(text=f"Parabéns! Você ganhou! A palavra era '{self.palavra_secreta}'.", text_color="#32CD32")
            self.jogo_ativo = False
        elif self.tentativas_restantes <= 0:
            self.mensagem_label.configure(text=f"Você perdeu! A palavra era '{self.palavra_secreta}'.", text_color="red")
            self.jogo_ativo = False

if __name__ == "__main__":
    app = ForcaGame()
    app.mainloop()