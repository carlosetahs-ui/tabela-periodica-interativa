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

        for numero, simbolo, nome, massa, grupo, periodo, categoria in ELEMENTOS:
            cor = CORES.get(categoria, "#dddddd")
            linha = periodo + 1
            if periodo in (8, 9):
                linha += 1  # espaço extra antes de lantanídeos/actinídeos
            btn = tk.Button(
                self, text=f"{simbolo}\n{numero}",
                width=4, height=2, bg=cor, font=("Segoe UI", 9, "bold"),
                command=lambda n=numero, s=simbolo, nm=nome, m=massa, c=categoria:
                    self.mostrar_detalhes(n, s, nm, m, c)
            )
            btn.grid(row=linha, column=grupo, padx=1, pady=1)

    def mostrar_detalhes(self, numero, simbolo, nome, massa, categoria):
        texto = (f"{nome} ({simbolo}) — Número atômico: {numero}\n"
                 f"Massa atômica: {massa}  |  Categoria: {categoria.replace('-', ' ')}")
        self.painel_info.config(text=texto)
        tk.Toplevel(self)

if __name__ == "__main__":
    app = TabelaPeriodica()
    app.mainloop()