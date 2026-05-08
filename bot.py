import customtkinter as ctk
import json
from datetime import datetime # Para pegar a hora exata da compra


# --- 1. Dados Iniciais ---
produtos = [["Camiseta", 79.99], ["Calça Jeans", 199.99], ["Tênis", 399.99], ["Jaqueta", 250.00], ["Regata", 70.00], ["Calça baggy", 299.99], ["Calça Flare", 199.99], ["Calça Reta", 199.99], ["Camisa Social", 100.00]]
regionais_fortaleza = [["Aldeota", 15.00], ["Centro", 10.00], ["Messejana", 20.00], ["Benfica", 12.00]]

# O carrinho agora começa vazio e vai enchendo
carrinho = []

# --- 2. Configuração da Janela ---
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("650x600")
app.title("Chatbot Senac - Sistema de Vendas")

tela_chat = ctk.CTkTextbox(app, width=600, height=350, font=("Arial", 14))
tela_chat.pack(pady=20)

def bot_fala(mensagem):
    tela_chat.configure(state="normal")
    tela_chat.insert(ctk.END, f"🤖 Bot: {mensagem}\n\n")
    tela_chat.see(ctk.END)
    tela_chat.configure(state="disabled")

bot_fala("Olá! Bem-vindo à Loja C e IA.\nNavegue pelo menu abaixo para fazer suas compras.")

# --- 3. Funções dos Botões ---

def ver_catalogo():
    texto = "🛍️ CATÁLOGO DE PRODUTOS:\n"
    for i, item in enumerate(produtos):
        texto += f"ID {i+1} - {item[0]} (R$ {item[1]:.2f})\n"
    bot_fala(texto)

def add_carrinho():
    dialog = ctk.CTkInputDialog(text="Digite o ID do produto que deseja comprar:", title="Adicionar ao Carrinho")
    escolha = dialog.get_input()
    
    if escolha and escolha.isdigit():
        idx = int(escolha) - 1
        if 0 <= idx < len(produtos):
            carrinho.append(produtos[idx])
            bot_fala(f"✅ '{produtos[idx][0]}' adicionado ao carrinho com sucesso!")
        else:
            bot_fala("❌ Produto não encontrado. Verifique o ID no catálogo.")

def ver_carrinho():
    if not carrinho:
        bot_fala("🛒 Seu carrinho está vazio.")
        return
        
    texto = "🛒 SEU CARRINHO ATUAL:\n"
    total_parcial = 0
    for item in carrinho:
        texto += f"- {item[0]} (R$ {item[1]:.2f})\n"
        total_parcial += item[1]
    
    texto += f"\nTotal parcial: R$ {total_parcial:.2f}"
    bot_fala(texto)
    
def suporte():
    fala_do_suporte = "Seja Bem Vindo ao Suporte"
    outra_fala_suporte = "Digite seu numero para entrarmos em contato"
    bot_fala(fala_do_suporte)
    bot_fala("Fale o seu problema ou Sugestão")
    bot_fala(outra_fala_suporte)
    
    input_suporte = ctk.CTkEntry(app,
    placeholder_text="Digite sua Reclamação ou Sugestão",
    width=300)
    input_suporte.pack(pady=10)
    
    
    input_suporte = ctk.CTkEntry(app,
    placeholder_text="Seu número",
    width=300)
    input_suporte.pack(pady=10)
    
        

def finalizar_compra():
    if not carrinho:
        bot_fala("❌ Você não pode finalizar com o carrinho vazio!")
        return
        
    dialog_reg = ctk.CTkInputDialog(text="Entrega em Fortaleza:\n1. Aldeota\n2. Centro\n3. Messejana\n4. Benfica\nDigite o número:", title="Frete")
    reg_escolha = dialog_reg.get_input()
    
    if reg_escolha and reg_escolha.isdigit() and 1 <= int(reg_escolha) <= 3:
        idx_reg = int(reg_escolha) - 1
        bairro = regionais_fortaleza[idx_reg][0]
        frete = regionais_fortaleza[idx_reg][1]
        
        subtotal = sum([item[1] for item in carrinho])
        total_final = subtotal + frete
        
        # --- A MÁGICA DO JSON: CRIANDO A NOTA FISCAL ---
        # Criamos um "Dicionário" em Python, que se traduz perfeitamente para JSON
        nota_fiscal = {
            "loja": "Loja DevCE",
            "data_compra": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "cliente_regional": bairro,
            "itens_comprados": carrinho,
            "subtotal": subtotal,
            "frete": frete,
            "total_pago": total_final
        }
        
        # Abrimos (ou criamos) o arquivo e salvamos os dados lá dentro
        with open("nota_fiscal.json", "w", encoding="utf-8") as arquivo:
            json.dump(nota_fiscal, arquivo, ensure_ascii=False, indent=4)
            
        bot_fala(f"🎉 Compra finalizada com sucesso!\nTotal: R$ {total_final:.2f}\n📄 Uma Nota Fiscal (nota_fiscal.json) foi gerada na sua pasta!")
        
        # Limpa o carrinho para a próxima compra
        carrinho.clear() 
    else:
        bot_fala("❌ Regional inválida. Compra cancelada.")

# --- 4. Interface dos Botões ---
frame_botoes = ctk.CTkFrame(app)
frame_botoes.pack(pady=10)

btn_catalogo = ctk.CTkButton(frame_botoes, text="1. Ver Catálogo", command=ver_catalogo)
btn_catalogo.grid(row=0, column=0, padx=5, pady=5)

btn_add = ctk.CTkButton(frame_botoes, text="2. Add ao Carrinho", command=add_carrinho)
btn_add.grid(row=0, column=1, padx=5, pady=5)

btn_ver_car = ctk.CTkButton(frame_botoes, text="3. Ver Carrinho", command=ver_carrinho)
btn_ver_car.grid(row=0, column=2, padx=5, pady=5)

btn_catalogo = ctk.CTkButton(frame_botoes, text="4. Suporte", command=suporte)
btn_catalogo.grid(row=0, column=3, padx=5, pady=5)

# Botão verde e largo para dar destaque à ação final
btn_finalizar = ctk.CTkButton(frame_botoes, text="5. Finalizar & Gerar Nota Fiscal (JSON)", command=finalizar_compra, fg_color="green", hover_color="darkgreen")
btn_finalizar.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

app.mainloop()