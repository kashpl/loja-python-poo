# pyrefly: ignore [missing-import]
import json
from datetime import datetime
from pathlib import Path
from tkinter import messagebox

import customtkinter as ctk


# ========== CONFIGURACAO VISUAL ==========
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

CORES = {
    "fundo": "#0a0510",
    "painel": "#160d21",
    "card": "#1c1229",
    "card_hover": "#2d1b46",
    "primaria": "#9333ea",
    "primaria_hover": "#a855f7",
    "sucesso": "#22c55e",
    "sucesso_hover": "#15803d",
    "perigo": "#f43f5e",
    "perigo_hover": "#b91c1c",
    "neutra": "#6b21a8",
    "neutra_hover": "#7e22ce",
    "texto": "#f5f3ff",
    "texto_fraco": "#a78bfa",
}

FONTE_TITULO = ("Segoe UI", 24, "bold")
FONTE_SUBTITULO = ("Segoe UI", 13)
FONTE_SECAO = ("Segoe UI", 16, "bold")
FONTE_TEXTO = ("Segoe UI", 12)
FONTE_BOTAO = ("Segoe UI", 12, "bold")


# ========== DADOS DA LOJA ==========
PRODUTOS = [
    {"id": 1, "nome": "Camiseta", "preco": 79.99, "categoria": "Camisetas"},
    {"id": 2, "nome": "Calça Jeans", "preco": 199.99, "categoria": "Calças"},
    {"id": 3, "nome": "Tênis", "preco": 399.99, "categoria": "Calçados"},
    {"id": 4, "nome": "Jaqueta", "preco": 250.00, "categoria": "Casacos"},
    {"id": 5, "nome": "Regata", "preco": 70.00, "categoria": "Camisetas"},
    {"id": 6, "nome": "Calça Baggy", "preco": 299.99, "categoria": "Calças"},
    {"id": 7, "nome": "Calça Flare", "preco": 199.99, "categoria": "Calças"},
    {"id": 8, "nome": "Calça Reta", "preco": 199.99, "categoria": "Calças"},
    {"id": 9, "nome": "Camisa Social", "preco": 100.00, "categoria": "Camisas"},
]

REGIOES_FORTALEZA = [
    {"bairro": "Aldeota", "frete": 15.00},
    {"bairro": "Centro", "frete": 10.00},
    {"bairro": "Messejana", "frete": 20.00},
    {"bairro": "Benfica", "frete": 12.00},
]

FORMAS_PAGAMENTO = ["Pix", "Cartão de crédito", "Cartão de débito", "Dinheiro"]


def formatar_moeda(valor):
    texto = f"R$ {valor:,.2f}"
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")


class LojaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.carrinho = {}
        self.pasta_saida = Path(__file__).resolve().parent
        self.title("Loja C & IA - Assistente de vendas")
        self.geometry("1120x720")
        self.minsize(1000, 650)
        self.configure(fg_color=CORES["fundo"])
        self.criar_layout()
        self.mostrar_catalogo()
        self.atualizar_resumo_carrinho()
        self.bot_fala(
            "Olá! Seja bem-vindo à Loja C & IA. Escolha os produtos no catálogo, "
            "acompanhe o carrinho ao lado e finalize quando estiver pronto."
        )

    # ========== MONTAGEM DA INTERFACE ==========
    def criar_layout(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.criar_cabecalho()

        self.conteudo = ctk.CTkFrame(self, fg_color="transparent")
        self.conteudo.grid(row=1, column=0, sticky="nsew", padx=18, pady=(0, 18))
        self.conteudo.grid_columnconfigure(0, weight=1)
        self.conteudo.grid_columnconfigure(1, minsize=340)
        self.conteudo.grid_rowconfigure(0, weight=1)

        self.coluna_esquerda = ctk.CTkFrame(self.conteudo, fg_color="transparent")
        self.coluna_esquerda.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
        self.coluna_esquerda.grid_columnconfigure(0, weight=1)
        self.coluna_esquerda.grid_rowconfigure(0, weight=3)
        self.coluna_esquerda.grid_rowconfigure(1, weight=2)

        self.criar_area_catalogo()
        self.criar_area_chat()
        self.criar_area_carrinho()

    def criar_cabecalho(self):
        self.cabecalho = ctk.CTkFrame(self, height=86, corner_radius=0, fg_color=CORES["painel"])
        self.cabecalho.grid(row=0, column=0, sticky="ew", padx=0, pady=(0, 18))
        self.cabecalho.grid_columnconfigure(0, weight=1)

        bloco_titulo = ctk.CTkFrame(self.cabecalho, fg_color="transparent")
        bloco_titulo.grid(row=0, column=0, sticky="w", padx=24, pady=16)

        ctk.CTkLabel(
            bloco_titulo,
            text="Loja C & IA",
            font=FONTE_TITULO,
            text_color=CORES["texto"],
        ).pack(anchor="w")

        ctk.CTkLabel(
            bloco_titulo,
            text="Moda, atendimento rápido e compra organizada",
            font=FONTE_SUBTITULO,
            text_color=CORES["texto_fraco"],
        ).pack(anchor="w", pady=(2, 0))

        bloco_status = ctk.CTkFrame(self.cabecalho, fg_color="transparent")
        bloco_status.grid(row=0, column=1, sticky="e", padx=24, pady=16)

        self.status_itens_label = ctk.CTkLabel(
            bloco_status,
            text="0 itens",
            font=FONTE_BOTAO,
            text_color=CORES["texto"],
            fg_color=CORES["card"],
            corner_radius=8,
            width=90,
            height=32,
        )
        self.status_itens_label.pack(side="left", padx=(0, 8))

        self.status_total_label = ctk.CTkLabel(
            bloco_status,
            text="Total: R$ 0,00",
            font=FONTE_BOTAO,
            text_color=CORES["texto"],
            fg_color=CORES["primaria"],
            corner_radius=8,
            width=150,
            height=32,
        )
        self.status_total_label.pack(side="left")

    def criar_area_catalogo(self):
        painel = ctk.CTkFrame(self.coluna_esquerda, corner_radius=12, fg_color=CORES["painel"])
        painel.grid(row=0, column=0, sticky="nsew", pady=(0, 12))
        painel.grid_columnconfigure(0, weight=1)
        painel.grid_rowconfigure(1, weight=1)

        topo = ctk.CTkFrame(painel, fg_color="transparent")
        topo.grid(row=0, column=0, sticky="ew", padx=16, pady=(14, 8))
        topo.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            topo,
            text="Catálogo",
            font=FONTE_SECAO,
            text_color=CORES["texto"],
        ).grid(row=0, column=0, sticky="w")

        self.busca_var = ctk.StringVar()
        self.busca_var.trace_add("write", lambda *_: self.mostrar_catalogo())

        self.busca_entry = ctk.CTkEntry(
            topo,
            textvariable=self.busca_var,
            placeholder_text="Buscar produto ou categoria",
            height=36,
            border_width=1,
            fg_color=CORES["fundo"],
        )
        self.busca_entry.grid(row=0, column=1, sticky="ew", padx=(16, 0))

        self.catalogo_lista = ctk.CTkScrollableFrame(
            painel,
            fg_color=CORES["fundo"],
            corner_radius=10,
        )
        self.catalogo_lista.grid(row=1, column=0, sticky="nsew", padx=16, pady=(0, 16))
        self.catalogo_lista.grid_columnconfigure(0, weight=1)

    def criar_area_chat(self):
        painel = ctk.CTkFrame(self.coluna_esquerda, corner_radius=12, fg_color=CORES["painel"])
        painel.grid(row=1, column=0, sticky="nsew")
        painel.grid_columnconfigure(0, weight=1)
        painel.grid_rowconfigure(1, weight=1)

        topo = ctk.CTkFrame(painel, fg_color="transparent")
        topo.grid(row=0, column=0, sticky="ew", padx=16, pady=(14, 8))
        topo.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            topo,
            text="Conversa",
            font=FONTE_SECAO,
            text_color=CORES["texto"],
        ).grid(row=0, column=0, sticky="w")

        acoes = ctk.CTkFrame(topo, fg_color="transparent")
        acoes.grid(row=0, column=1, sticky="e")

        ctk.CTkButton(
            acoes,
            text="Ver carrinho",
            width=110,
            height=34,
            font=FONTE_BOTAO,
            fg_color=CORES["neutra"],
            hover_color=CORES["neutra_hover"],
            command=self.ver_carrinho_no_chat,
        ).pack(side="left", padx=(0, 8))

        ctk.CTkButton(
            acoes,
            text="Suporte",
            width=90,
            height=34,
            font=FONTE_BOTAO,
            fg_color=CORES["neutra"],
            hover_color=CORES["neutra_hover"],
            command=self.abrir_suporte,
        ).pack(side="left", padx=(0, 8))

        ctk.CTkButton(
            acoes,
            text="Limpar",
            width=90,
            height=34,
            font=FONTE_BOTAO,
            fg_color=CORES["perigo"],
            hover_color=CORES["perigo_hover"],
            command=self.limpar_chat,
        ).pack(side="left")

        self.chat_textbox = ctk.CTkTextbox(
            painel,
            font=FONTE_TEXTO,
            wrap="word",
            corner_radius=10,
            fg_color=CORES["fundo"],
            text_color=CORES["texto"],
        )
        self.chat_textbox.grid(row=1, column=0, sticky="nsew", padx=16, pady=(0, 16))
        self.chat_textbox.configure(state="disabled")

    def criar_area_carrinho(self):
        self.carrinho_painel = ctk.CTkFrame(
            self.conteudo,
            width=340,
            corner_radius=12,
            fg_color=CORES["painel"],
        )
        self.carrinho_painel.grid(row=0, column=1, sticky="nsew")
        self.carrinho_painel.grid_propagate(False)
        self.carrinho_painel.grid_columnconfigure(0, weight=1)
        self.carrinho_painel.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(
            self.carrinho_painel,
            text="Seu carrinho",
            font=FONTE_SECAO,
            text_color=CORES["texto"],
        ).grid(row=0, column=0, sticky="w", padx=16, pady=(14, 8))

        self.carrinho_lista = ctk.CTkScrollableFrame(
            self.carrinho_painel,
            fg_color=CORES["fundo"],
            corner_radius=10,
        )
        self.carrinho_lista.grid(row=1, column=0, sticky="nsew", padx=16, pady=(0, 12))
        self.carrinho_lista.grid_columnconfigure(0, weight=1)

        resumo = ctk.CTkFrame(self.carrinho_painel, fg_color="transparent")
        resumo.grid(row=2, column=0, sticky="ew", padx=16, pady=(0, 14))
        resumo.grid_columnconfigure(0, weight=1)

        self.subtotal_label = ctk.CTkLabel(
            resumo,
            text="Subtotal: R$ 0,00",
            font=FONTE_TEXTO,
            text_color=CORES["texto_fraco"],
        )
        self.subtotal_label.grid(row=0, column=0, sticky="w")

        self.total_label = ctk.CTkLabel(
            resumo,
            text="Total: R$ 0,00",
            font=("Segoe UI", 18, "bold"),
            text_color=CORES["texto"],
        )
        self.total_label.grid(row=1, column=0, sticky="w", pady=(4, 12))

        ctk.CTkButton(
            resumo,
            text="Finalizar compra",
            height=44,
            font=FONTE_BOTAO,
            fg_color=CORES["sucesso"],
            hover_color=CORES["sucesso_hover"],
            command=self.abrir_checkout,
        ).grid(row=2, column=0, sticky="ew")

    # ========== CATALOGO ==========
    def mostrar_catalogo(self):
        for widget in self.catalogo_lista.winfo_children():
            widget.destroy()

        termo = self.busca_var.get().strip().lower() if hasattr(self, "busca_var") else ""

        produtos_filtrados = [
            produto
            for produto in PRODUTOS
            if termo in produto["nome"].lower() or termo in produto["categoria"].lower()
        ]

        if not produtos_filtrados:
            ctk.CTkLabel(
                self.catalogo_lista,
                text="Nenhum produto encontrado.",
                font=FONTE_TEXTO,
                text_color=CORES["texto_fraco"],
            ).grid(row=0, column=0, padx=12, pady=20)
            return

        for linha, produto in enumerate(produtos_filtrados):
            self.criar_card_produto(linha, produto)

    def criar_card_produto(self, linha, produto):
        card = ctk.CTkFrame(self.catalogo_lista, corner_radius=8, fg_color=CORES["card"])
        card.grid(row=linha, column=0, sticky="ew", padx=8, pady=6)
        card.grid_columnconfigure(0, weight=1)

        info = ctk.CTkFrame(card, fg_color="transparent")
        info.grid(row=0, column=0, sticky="ew", padx=14, pady=12)

        ctk.CTkLabel(
            info,
            text=produto["nome"],
            font=("Segoe UI", 14, "bold"),
            text_color=CORES["texto"],
        ).pack(anchor="w")

        ctk.CTkLabel(
            info,
            text=f'{produto["categoria"]}  |  ID {produto["id"]}',
            font=("Segoe UI", 11),
            text_color=CORES["texto_fraco"],
        ).pack(anchor="w", pady=(2, 0))

        ctk.CTkLabel(
            card,
            text=formatar_moeda(produto["preco"]),
            font=("Segoe UI", 14, "bold"),
            text_color=CORES["texto"],
        ).grid(row=0, column=1, padx=12, pady=12)

        ctk.CTkButton(
            card,
            text="Adicionar",
            width=108,
            height=36,
            font=FONTE_BOTAO,
            fg_color=CORES["primaria"],
            hover_color=CORES["primaria_hover"],
            command=lambda produto_id=produto["id"]: self.adicionar_produto(produto_id),
        ).grid(row=0, column=2, padx=(0, 14), pady=12)

    # ========== CHAT ==========
    def escrever_chat(self, remetente, mensagem):
        hora = datetime.now().strftime("%H:%M")
        self.chat_textbox.configure(state="normal")
        self.chat_textbox.insert("end", f"[{hora}] {remetente}: {mensagem}\n\n")
        self.chat_textbox.see("end")
        self.chat_textbox.configure(state="disabled")

    def bot_fala(self, mensagem):
        self.escrever_chat("Assistente virtual", mensagem)

    def usuario_fala(self, mensagem):
        self.escrever_chat("Você", mensagem)

    def limpar_chat(self):
        self.chat_textbox.configure(state="normal")
        self.chat_textbox.delete("1.0", "end")
        self.chat_textbox.configure(state="disabled")
        self.bot_fala("Chat limpo. Como posso ajudar agora?")

    def ver_carrinho_no_chat(self):
        self.usuario_fala("Ver carrinho")

        if not self.carrinho:
            self.bot_fala("Seu carrinho está vazio.")
            return

        linhas = ["Resumo do carrinho:"]
        for item in self.carrinho.values():
            produto = item["produto"]
            quantidade = item["quantidade"]
            total_item = produto["preco"] * quantidade
            linhas.append(
                f"- {quantidade}x {produto['nome']} = {formatar_moeda(total_item)}"
            )

        linhas.append(f"Subtotal: {formatar_moeda(self.calcular_subtotal())}")
        self.bot_fala("\n".join(linhas))

    # ========== CARRINHO ==========
    def buscar_produto(self, produto_id):
        return next((produto for produto in PRODUTOS if produto["id"] == produto_id), None)

    def adicionar_produto(self, produto_id):
        produto = self.buscar_produto(produto_id)

        if produto is None:
            self.bot_fala("Produto não encontrado.")
            return

        if produto_id not in self.carrinho:
            self.carrinho[produto_id] = {"produto": produto, "quantidade": 0}

        self.carrinho[produto_id]["quantidade"] += 1
        self.usuario_fala(f"Adicionar {produto['nome']}")
        self.bot_fala(f"{produto['nome']} foi adicionado ao carrinho.")
        self.atualizar_resumo_carrinho()

    def alterar_quantidade(self, produto_id, diferenca):
        if produto_id not in self.carrinho:
            return

        self.carrinho[produto_id]["quantidade"] += diferenca

        if self.carrinho[produto_id]["quantidade"] <= 0:
            nome = self.carrinho[produto_id]["produto"]["nome"]
            del self.carrinho[produto_id]
            self.bot_fala(f"{nome} foi removido do carrinho.")
        else:
            produto = self.carrinho[produto_id]["produto"]
            quantidade = self.carrinho[produto_id]["quantidade"]
            self.bot_fala(f"{produto['nome']} agora tem quantidade {quantidade}.")

        self.atualizar_resumo_carrinho()

    def remover_produto(self, produto_id):
        if produto_id not in self.carrinho:
            return

        nome = self.carrinho[produto_id]["produto"]["nome"]
        del self.carrinho[produto_id]
        self.bot_fala(f"{nome} foi removido do carrinho.")
        self.atualizar_resumo_carrinho()

    def calcular_subtotal(self):
        return sum(
            item["produto"]["preco"] * item["quantidade"]
            for item in self.carrinho.values()
        )

    def contar_itens(self):
        return sum(item["quantidade"] for item in self.carrinho.values())

    def atualizar_resumo_carrinho(self):
        for widget in self.carrinho_lista.winfo_children():
            widget.destroy()

        if not self.carrinho:
            ctk.CTkLabel(
                self.carrinho_lista,
                text="Carrinho vazio",
                font=FONTE_TEXTO,
                text_color=CORES["texto_fraco"],
            ).grid(row=0, column=0, padx=12, pady=20)
        else:
            for linha, produto_id in enumerate(self.carrinho):
                self.criar_card_carrinho(linha, produto_id)

        subtotal = self.calcular_subtotal()
        quantidade = self.contar_itens()
        palavra_item = "item" if quantidade == 1 else "itens"

        self.subtotal_label.configure(text=f"Subtotal: {formatar_moeda(subtotal)}")
        self.total_label.configure(text=f"Total: {formatar_moeda(subtotal)}")
        self.status_itens_label.configure(text=f"{quantidade} {palavra_item}")
        self.status_total_label.configure(text=f"Total: {formatar_moeda(subtotal)}")

    def criar_card_carrinho(self, linha, produto_id):
        item = self.carrinho[produto_id]
        produto = item["produto"]
        quantidade = item["quantidade"]
        total_item = produto["preco"] * quantidade

        card = ctk.CTkFrame(self.carrinho_lista, corner_radius=8, fg_color=CORES["card"])
        card.grid(row=linha, column=0, sticky="ew", padx=8, pady=6)
        card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            card,
            text=produto["nome"],
            font=("Segoe UI", 13, "bold"),
            text_color=CORES["texto"],
        ).grid(row=0, column=0, sticky="w", padx=12, pady=(10, 0))

        ctk.CTkLabel(
            card,
            text=f"{quantidade}x  |  {formatar_moeda(total_item)}",
            font=("Segoe UI", 11),
            text_color=CORES["texto_fraco"],
        ).grid(row=1, column=0, sticky="w", padx=12, pady=(2, 10))

        controles = ctk.CTkFrame(card, fg_color="transparent")
        controles.grid(row=0, column=1, rowspan=2, sticky="e", padx=10, pady=10)

        ctk.CTkButton(
            controles,
            text="-",
            width=30,
            height=30,
            font=FONTE_BOTAO,
            fg_color=CORES["neutra"],
            hover_color=CORES["neutra_hover"],
            command=lambda pid=produto_id: self.alterar_quantidade(pid, -1),
        ).pack(side="left", padx=(0, 4))

        ctk.CTkButton(
            controles,
            text="+",
            width=30,
            height=30,
            font=FONTE_BOTAO,
            fg_color=CORES["primaria"],
            hover_color=CORES["primaria_hover"],
            command=lambda pid=produto_id: self.alterar_quantidade(pid, 1),
        ).pack(side="left", padx=(0, 4))

        ctk.CTkButton(
            controles,
            text="X",
            width=30,
            height=30,
            font=FONTE_BOTAO,
            fg_color=CORES["perigo"],
            hover_color=CORES["perigo_hover"],
            command=lambda pid=produto_id: self.remover_produto(pid),
        ).pack(side="left")

    # ========== SUPORTE ==========
    def abrir_suporte(self):
        janela = ctk.CTkToplevel(self)
        janela.title("Suporte ao cliente")
        janela.geometry("470x420")
        janela.transient(self)
        janela.grab_set()
        janela.configure(fg_color=CORES["fundo"])

        ctk.CTkLabel(
            janela,
            text="Suporte ao cliente",
            font=FONTE_SECAO,
            text_color=CORES["texto"],
        ).pack(anchor="w", padx=22, pady=(20, 8))

        ctk.CTkLabel(
            janela,
            text="Mensagem",
            font=FONTE_TEXTO,
            text_color=CORES["texto_fraco"],
        ).pack(anchor="w", padx=22)

        mensagem_entry = ctk.CTkTextbox(janela, height=130, corner_radius=8)
        mensagem_entry.pack(fill="x", padx=22, pady=(4, 12))

        ctk.CTkLabel(
            janela,
            text="Contato (e-mail ou WhatsApp)",
            font=FONTE_TEXTO,
            text_color=CORES["texto_fraco"],
        ).pack(anchor="w", padx=22)

        contato_entry = ctk.CTkEntry(janela, placeholder_text="Opcional", height=36)
        contato_entry.pack(fill="x", padx=22, pady=(4, 18))

        def enviar_suporte():
            mensagem = mensagem_entry.get("1.0", "end").strip()
            contato = contato_entry.get().strip()

            if not mensagem:
                messagebox.showwarning("Aviso", "Digite uma mensagem antes de enviar.")
                return

            arquivo = self.pasta_saida / "suporte_contatos.txt"
            with arquivo.open("a", encoding="utf-8") as f:
                f.write(
                    f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} | "
                    f"Mensagem: {mensagem} | Contato: {contato or 'Não informado'}\n"
                )

            self.usuario_fala(f"Enviar suporte: {mensagem[:50]}")
            self.bot_fala(f"Sua mensagem foi registrada em {arquivo.name}.")
            janela.destroy()

        ctk.CTkButton(
            janela,
            text="Enviar mensagem",
            height=42,
            font=FONTE_BOTAO,
            fg_color=CORES["sucesso"],
            hover_color=CORES["sucesso_hover"],
            command=enviar_suporte,
        ).pack(fill="x", padx=22)

    # ========== CHECKOUT ==========
    def abrir_checkout(self):
        if not self.carrinho:
            self.bot_fala("Você não pode finalizar com o carrinho vazio.")
            return

        janela = ctk.CTkToplevel(self)
        janela.title("Finalizar compra")
        janela.geometry("520x610")
        janela.transient(self)
        janela.grab_set()
        janela.configure(fg_color=CORES["fundo"])

        ctk.CTkLabel(
            janela,
            text="Finalizar compra",
            font=FONTE_SECAO,
            text_color=CORES["texto"],
        ).pack(anchor="w", padx=22, pady=(20, 12))

        nome_entry = self.criar_campo(janela, "Nome do cliente", "Ex: Ana Souza")
        telefone_entry = self.criar_campo(janela, "Telefone", "Ex: (85) 99999-9999")
        endereco_entry = self.criar_campo(janela, "Endereço de entrega", "Rua, número e complemento")

        ctk.CTkLabel(
            janela,
            text="Região de entrega",
            font=FONTE_TEXTO,
            text_color=CORES["texto_fraco"],
        ).pack(anchor="w", padx=22)

        regiao_var = ctk.StringVar(value=REGIOES_FORTALEZA[0]["bairro"])
        regiao_menu = ctk.CTkOptionMenu(
            janela,
            values=[regiao["bairro"] for regiao in REGIOES_FORTALEZA],
            variable=regiao_var,
            height=36,
            fg_color=CORES["card"],
            button_color=CORES["primaria"],
            button_hover_color=CORES["primaria_hover"],
        )
        regiao_menu.pack(fill="x", padx=22, pady=(4, 12))

        ctk.CTkLabel(
            janela,
            text="Forma de pagamento",
            font=FONTE_TEXTO,
            text_color=CORES["texto_fraco"],
        ).pack(anchor="w", padx=22)

        pagamento_var = ctk.StringVar(value=FORMAS_PAGAMENTO[0])
        pagamento_menu = ctk.CTkOptionMenu(
            janela,
            values=FORMAS_PAGAMENTO,
            variable=pagamento_var,
            height=36,
            fg_color=CORES["card"],
            button_color=CORES["primaria"],
            button_hover_color=CORES["primaria_hover"],
        )
        pagamento_menu.pack(fill="x", padx=22, pady=(4, 14))

        resumo_label = ctk.CTkLabel(
            janela,
            text=self.texto_resumo_checkout(regiao_var.get()),
            justify="left",
            font=FONTE_TEXTO,
            text_color=CORES["texto"],
            fg_color=CORES["painel"],
            corner_radius=8,
            padx=14,
            pady=12,
        )
        resumo_label.pack(fill="x", padx=22, pady=(0, 16))

        def atualizar_resumo_por_regiao(*_):
            resumo_label.configure(text=self.texto_resumo_checkout(regiao_var.get()))

        regiao_var.trace_add("write", atualizar_resumo_por_regiao)

        def confirmar_compra():
            nome = nome_entry.get().strip()
            telefone = telefone_entry.get().strip()
            endereco = endereco_entry.get().strip()

            if not nome or not telefone or not endereco:
                messagebox.showwarning(
                    "Dados incompletos",
                    "Preencha nome, telefone e endereço antes de finalizar.",
                )
                return

            nota = self.criar_nota_fiscal(
                nome=nome,
                telefone=telefone,
                endereco=endereco,
                regiao=regiao_var.get(),
                pagamento=pagamento_var.get(),
            )
            arquivo = self.salvar_nota_fiscal(nota)

            self.usuario_fala(f"Finalizar compra para {regiao_var.get()}")
            self.bot_fala(
                f"Compra finalizada com sucesso. Total pago: "
                f"{formatar_moeda(nota['total_pago'])}. Nota salva em {arquivo.name}."
            )

            self.carrinho.clear()
            self.atualizar_resumo_carrinho()
            janela.destroy()
            messagebox.showinfo("Compra finalizada", f"Nota fiscal salva em:\n{arquivo}")

        ctk.CTkButton(
            janela,
            text="Confirmar compra",
            height=44,
            font=FONTE_BOTAO,
            fg_color=CORES["sucesso"],
            hover_color=CORES["sucesso_hover"],
            command=confirmar_compra,
        ).pack(fill="x", padx=22)

    def criar_campo(self, janela, label, placeholder):
        ctk.CTkLabel(
            janela,
            text=label,
            font=FONTE_TEXTO,
            text_color=CORES["texto_fraco"],
        ).pack(anchor="w", padx=22)

        entry = ctk.CTkEntry(janela, placeholder_text=placeholder, height=36)
        entry.pack(fill="x", padx=22, pady=(4, 12))
        return entry

    def obter_regiao(self, bairro):
        return next(regiao for regiao in REGIOES_FORTALEZA if regiao["bairro"] == bairro)

    def texto_resumo_checkout(self, bairro):
        subtotal = self.calcular_subtotal()
        frete = self.obter_regiao(bairro)["frete"]
        total = subtotal + frete
        return (
            f"Subtotal: {formatar_moeda(subtotal)}\n"
            f"Frete para {bairro}: {formatar_moeda(frete)}\n"
            f"Total final: {formatar_moeda(total)}"
        )

    def criar_nota_fiscal(self, nome, telefone, endereco, regiao, pagamento):
        subtotal = self.calcular_subtotal()
        frete = self.obter_regiao(regiao)["frete"]
        total_final = subtotal + frete

        itens = []
        for item in self.carrinho.values():
            produto = item["produto"]
            quantidade = item["quantidade"]
            itens.append(
                {
                    "id": produto["id"],
                    "produto": produto["nome"],
                    "categoria": produto["categoria"],
                    "preco_unitario": produto["preco"],
                    "quantidade": quantidade,
                    "total_item": produto["preco"] * quantidade,
                }
            )

        return {
            "loja": "Loja C & IA",
            "data_compra": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "cliente": {
                "nome": nome,
                "telefone": telefone,
                "endereco": endereco,
                "regiao": regiao,
            },
            "pagamento": pagamento,
            "itens_comprados": itens,
            "subtotal": subtotal,
            "frete": frete,
            "total_pago": total_final,
        }

    def salvar_nota_fiscal(self, nota):
        pasta_notas = self.pasta_saida / "notas_fiscais"
        pasta_notas.mkdir(exist_ok=True)

        data_arquivo = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        arquivo = pasta_notas / f"nota_fiscal_{data_arquivo}.json"

        with arquivo.open("w", encoding="utf-8") as f:
            json.dump(nota, f, ensure_ascii=False, indent=4)

        return arquivo


if __name__ == "__main__":
    app = LojaApp()
    app.mainloop()
