import tkinter as tk
from elementos import ELEMENTOS, CORES

class TabelaPeriodica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tabela Periódica Interativa")
        self.configure(bg="#1e1e1e")

        self.painel_info = tk.Label(
            self, text="Clique em um elemento para ver detalhes",
            font=("Segoe UI", 12), bg="#1e1e1e", fg="white",
            justify="left", anchor="w", height=3
        )
        self.painel_info.grid(row=0, column=1, columnspan=18, sticky="we", padx=10, pady=10)

        for numero, simbolo, nome, massa, grupo, periodo, categoria, config, ano in ELEMENTOS:
            cor = CORES.get(categoria, "#dddddd")
            linha = periodo + 1
            if periodo in (8, 9):
                linha += 1  # espaço extra antes de lantanídeos/actinídeos
            btn = tk.Button(
                self, text=f"{simbolo}\n{numero}",
                width=4, height=2, bg=cor, font=("Segoe UI", 9, "bold"),
                command=lambda n=numero, s=simbolo, nm=nome, m=massa, c=categoria, cf=config, an=ano:
                    self.mostrar_detalhes(n, s, nm, m, c, cf, an )
            )
            btn.grid(row=linha, column=grupo, padx=1, pady=1)

    def mostrar_detalhes(self, numero, simbolo, nome, massa, categoria, config, ano):
        texto = (f"{nome} ({simbolo}) — Número atômico: {numero}\n"
                 f"Massa atômica: {massa}  |  Categoria: {categoria.replace('-', ' ')}")
        self.painel_info.config(text=texto)

        cor = CORES.get(categoria, "#dddddd")

        nova_janela = tk.Toplevel(self)
        nova_janela.title(f"Detalhes: {nome}")
        nova_janela.geometry('320x220')
        nova_janela.configure(bg="#1e1e1e")
        nova_janela.resizable(False, False)

        cabeçalho = tk.Frame(nova_janela, bg=cor)
        cabeçalho.pack(fill='x')

        tk.Label(cabeçalho, text=simbolo, font=("Segoe UI", 28, "bold"),
        bg=cor, fg="#1e1e1e").pack(side="left", padx=15, pady=10)

        tk.Label(cabeçalho, text=f"{nome}\nNúmero atômico: {numero}",
        font=("Segoe UI", 11, "bold"), bg=cor, fg="#1e1e1e",
        justify="left").pack(side="left", pady=10)

        corpo = tk.Frame(nova_janela, bg="#1e1e1e")
        corpo.pack(fill="both", expand=True, padx=15, pady=10)

        detalhes = [
            ("Massa atômica", massa),
            ("Categoria", categoria.replace("-", " ").title()),
            ("Configuração eletrônica", config),
            ("Ano de descoberta", ano),]

        for rotulo, valor in detalhes:
            linha = tk.Frame(corpo, bg="#1e1e1e")
            linha.pack(fill="x", pady=3)
            tk.Label(linha, text=f"{rotulo}:", font=("Segoe UI", 10, "bold"),bg="#1e1e1e", fg="#aaaaaa", anchor="w", width=18).pack(side="left")
            tk.Label(linha, text=str(valor), font=("Segoe UI", 10),bg="#1e1e1e", fg="white", anchor="w", justify="left", wraplength=150).pack(side="left", fill="x")

if __name__ == "__main__":
    app = TabelaPeriodica()
    app.mainloop()