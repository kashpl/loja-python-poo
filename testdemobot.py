# pyrefly: ignore [missing-import]
import customtkinter as ctk
import json
from datetime import datetime
from tkinter import messagebox

# ========== CONFIGURAÇÃO DE TEMA ==========
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ========== DADOS ==========
produtos = [
    ["Camiseta", 79.99], ["Calça Jeans", 199.99], ["Tênis", 399.99],
    ["Jaqueta", 250.00], ["Regata", 70.00], ["Calça baggy", 299.99],
    ["Calça Flare", 199.99], ["Calça Reta", 199.99], ["Camisa Social", 100.00]
]
regionais_fortaleza = [
    ["Aldeota", 15.00], ["Centro", 10.00], ["Messejana", 20.00], ["Benfica", 12.00]
]

carrinho = []

# ========== JANELA PRINCIPAL ==========
app = ctk.CTk()
app.title("🛍️ Loja C & IA - Chatbot")
app.geometry("850x650")
app.minsize(1000, 600)

# ========== FRAME PRINCIPAL  ==========
main_frame = ctk.CTkFrame(app, corner_radius=0)
main_frame.pack(fill="both", expand=True, padx=15, pady=15)

# Coluna esquerda: chat + botões
left_frame = ctk.CTkFrame(main_frame, corner_radius=15)
left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

# Coluna direita: resumo do carrinho 
right_frame = ctk.CTkFrame(main_frame, width=250, corner_radius=15)
right_frame.pack(side="right", fill="y", padx=(10, 0))
right_frame.pack_propagate(False)

# ========== ÁREA DE CHAT ==========
chat_label = ctk.CTkLabel(left_frame, text="💬 Conversa", font=("Segoe UI", 16, "bold"))
chat_label.pack(anchor="w", padx=15, pady=(10, 5))

chat_textbox = ctk.CTkTextbox(left_frame, font=("Segoe UI", 12), wrap="word", corner_radius=10)
chat_textbox.pack(fill="both", expand=True, padx=15, pady=5)

def bot_fala(mensagem):
    """Adiciona mensagem do bot ao chat com timestamp"""
    chat_textbox.configure(state="normal")
    hora = datetime.now().strftime("%H:%M")
    chat_textbox.insert(ctk.END, f"[{hora}] 🤖 **Assistente virtual:** {mensagem}\n\n")
    chat_textbox.see(ctk.END)
    chat_textbox.configure(state="disabled")

def usuario_fala(mensagem):
    """Adiciona mensagem do usuário ao chat"""
    chat_textbox.configure(state="normal")
    hora = datetime.now().strftime("%H:%M")
    chat_textbox.insert(ctk.END, f"[{hora}] 👤 **Você:** {mensagem}\n\n")
    chat_textbox.see(ctk.END)
    chat_textbox.configure(state="disabled")

def limpar_chat():
    """Limpa a área de chat (exceto a mensagem de boas‑vindas)"""
    chat_textbox.configure(state="normal")
    chat_textbox.delete("1.0", ctk.END)
    chat_textbox.configure(state="disabled")
    bot_fala("Chat limpo! Como posso ajudar?")

# ========== RESUMO DO CARRINHO ==========
resumo_label = ctk.CTkLabel(right_frame, text="🛒 Seu Carrinho", font=("Segoe UI", 16, "bold"))
resumo_label.pack(pady=(15, 5))

cart_listbox = ctk.CTkTextbox(right_frame, height=200, font=("Segoe UI", 11), corner_radius=8)
cart_listbox.pack(fill="both", expand=True, padx=15, pady=5)
cart_listbox.configure(state="disabled")

total_label = ctk.CTkLabel(right_frame, text="Total: R$ 0.00", font=("Segoe UI", 14, "bold"))
total_label.pack(pady=10)

def atualizar_resumo_carrinho():
    """Atualiza o painel lateral com itens e total"""
    cart_listbox.configure(state="normal")
    cart_listbox.delete("1.0", ctk.END)
    if not carrinho:
        cart_listbox.insert(ctk.END, "Carrinho vazio")
    else:
        for item in carrinho:
            cart_listbox.insert(ctk.END, f"• {item[0]} - R$ {item[1]:.2f}\n")
    cart_listbox.configure(state="disabled")
    total = sum(item[1] for item in carrinho)
    total_label.configure(text=f"Total: R$ {total:.2f}")

# ========== FUNÇÕES DO BOT  ==========
def ver_catalogo():
    usuario_fala("Ver catálogo")
    texto = "🛍️ **CATÁLOGO DE PRODUTOS:**\n"
    for i, item in enumerate(produtos):
        texto += f"  ID {i+1} → {item[0]} - R$ {item[1]:.2f}\n"
    bot_fala(texto)

def add_carrinho():
    dialog = ctk.CTkInputDialog(text="Digite o ID do produto que deseja comprar:", title="Adicionar ao Carrinho")
    escolha = dialog.get_input()
    if escolha and escolha.isdigit():
        idx = int(escolha) - 1
        if 0 <= idx < len(produtos):
            carrinho.append(produtos[idx])
            usuario_fala(f"Adicionar produto ID {escolha}")
            bot_fala(f"✅ '{produtos[idx][0]}' adicionado ao carrinho!")
            atualizar_resumo_carrinho()
        else:
            bot_fala("❌ Produto não encontrado. Verifique o ID no catálogo.")
    else:
        bot_fala("❌ ID inválido.")

def ver_carrinho():
    usuario_fala("Ver carrinho")
    if not carrinho:
        bot_fala("🛒 Seu carrinho está vazio.")
        return
    texto = "🛒 **SEU CARRINHO ATUAL:**\n"
    total = 0
    for item in carrinho:
        texto += f"  - {item[0]} (R$ {item[1]:.2f})\n"
        total += item[1]
    texto += f"\n💰 **Total parcial:** R$ {total:.2f}"
    bot_fala(texto)
    atualizar_resumo_carrinho()

def suporte():
    """Janela para envio de sugestões/reclamações com contato"""
    suporte_win = ctk.CTkToplevel(app)
    suporte_win.title("Suporte ao Cliente")
    suporte_win.geometry("450x400")
    suporte_win.grab_set()
    
    ctk.CTkLabel(suporte_win, text="📢 Suporte – Conte-nos seu problema ou sugestão", 
                 font=("Segoe UI", 14, "bold")).pack(pady=15)
    
    ctk.CTkLabel(suporte_win, text="Mensagem:").pack(anchor="w", padx=20)
    msg_entry = ctk.CTkTextbox(suporte_win, height=120, corner_radius=8)
    msg_entry.pack(padx=20, pady=5, fill="x")
    
    ctk.CTkLabel(suporte_win, text="Seu contato (e-mail ou WhatsApp):").pack(anchor="w", padx=20)
    contato_entry = ctk.CTkEntry(suporte_win, placeholder_text="opcional")
    contato_entry.pack(padx=20, pady=5, fill="x")
    
    def enviar_suporte():
        mensagem = msg_entry.get("1.0", ctk.END).strip()
        contato = contato_entry.get().strip()
        if not mensagem:
            messagebox.showwarning("Aviso", "Digite uma mensagem.")
            return
        # Salva em arquivo de suporte
        with open("suporte_contatos.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - Mensagem: {mensagem} | Contato: {contato}\n")
        bot_fala("✅ Sua mensagem foi registrada. Em breve entraremos em contato.")
        usuario_fala(f"Enviar suporte: {mensagem[:50]}...")
        suporte_win.destroy()
    
    ctk.CTkButton(suporte_win, text="Enviar", command=enviar_suporte, fg_color="#2e7d32", hover_color="#1b5e20").pack(pady=20)

def finalizar_compra():
    if not carrinho:
        bot_fala("❌ Você não pode finalizar com o carrinho vazio!")
        return
    
    # Mostra opções de região
    regioes_str = "\n".join([f"{i+1} → {regionais_fortaleza[i][0]} (Frete R$ {regionais_fortaleza[i][1]:.2f})" 
                              for i in range(len(regionais_fortaleza))])
    dialog_reg = ctk.CTkInputDialog(text=f"Escolha a região de entrega:\n{regioes_str}\nDigite o número:", title="Frete")
    reg_escolha = dialog_reg.get_input()
    
    if reg_escolha and reg_escolha.isdigit():
        idx_reg = int(reg_escolha) - 1
        if 0 <= idx_reg < len(regionais_fortaleza):
            bairro, frete = regionais_fortaleza[idx_reg]
            subtotal = sum(item[1] for item in carrinho)
            total_final = subtotal + frete
            
            # Gera nota fiscal
            nota_fiscal = {
                "loja": "🛍️ Loja C & IA",
                "data_compra": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "cliente_regional": bairro,
                "itens_comprados": carrinho.copy(),
                "subtotal": subtotal,
                "frete": frete,
                "total_pago": total_final
            }
            with open("nota_fiscal.json", "w", encoding="utf-8") as f:
                json.dump(nota_fiscal, f, ensure_ascii=False, indent=4)
            
            bot_fala(f"🎉 Compra finalizada com sucesso!\n"
                     f"📦 Região: {bairro}\n"
                     f"💰 Total: R$ {total_final:.2f}\n"
                     f"📄 Nota fiscal salva em 'nota_fiscal.json'")
            usuario_fala(f"Finalizar compra para {bairro}")
            carrinho.clear()
            atualizar_resumo_carrinho()
        else:
            bot_fala("❌ Opção inválida. Compra cancelada.")
    else:
        bot_fala("❌ Entrada inválida. Compra cancelada.")

# ========== PAINEL DE BOTÕES PRINCIPAIS ==========
btn_frame = ctk.CTkFrame(left_frame, corner_radius=10, fg_color="transparent")
btn_frame.pack(fill="x", padx=15, pady=(5, 15))

# Configurar grid responsivo (5 botões na primeira linha, 1 na segunda)
for i in range(5):
    btn_frame.columnconfigure(i, weight=1)

btn_catalogo = ctk.CTkButton(btn_frame, text="📋 Catálogo", command=ver_catalogo, height=38, corner_radius=8)
btn_catalogo.grid(row=0, column=0, padx=4, pady=4, sticky="ew")

btn_add = ctk.CTkButton(btn_frame, text="➕ Adicionar", command=add_carrinho, height=38, corner_radius=8)
btn_add.grid(row=0, column=1, padx=4, pady=4, sticky="ew")

btn_ver_car = ctk.CTkButton(btn_frame, text="🛒 Ver Carrinho", command=ver_carrinho, height=38, corner_radius=8)
btn_ver_car.grid(row=0, column=2, padx=4, pady=4, sticky="ew")

btn_suporte = ctk.CTkButton(btn_frame, text="🎧 Suporte", command=suporte, height=38, corner_radius=8)
btn_suporte.grid(row=0, column=3, padx=4, pady=4, sticky="ew")

btn_limpar = ctk.CTkButton(btn_frame, text="🗑️ Limpar Chat", command=limpar_chat, height=38, corner_radius=8, fg_color="#546e7a", hover_color="#37474f")
btn_limpar.grid(row=0, column=4, padx=4, pady=4, sticky="ew")

btn_finalizar = ctk.CTkButton(btn_frame, text="💰 Finalizar Compra", command=finalizar_compra, 
                              fg_color="#2e7d32", hover_color="#1b5e20", height=42, corner_radius=8, font=("Segoe UI", 12, "bold"))
btn_finalizar.grid(row=1, column=0, columnspan=5, padx=4, pady=10, sticky="ew")

# Mensagem de boas‑vindas
bot_fala("Olá! Eu sou o seu assistente de vendas da Loja C & IA.\n"
         "Use os botões acima para navegar pelo catálogo, adicionar itens ao carrinho e finalizar sua compra.\n"
         "Estamos em Fortaleza – regiões: Aldeota, Centro, Messejana e Benfica.\n"
         "Precisando de ajuda, clique em 'Suporte'.")

# Inicializa resumo do carrinho
atualizar_resumo_carrinho()

app.mainloop()