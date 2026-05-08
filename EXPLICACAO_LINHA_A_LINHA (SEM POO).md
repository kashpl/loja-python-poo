# Explicação linha por linha - versão sem POO

Arquivo explicado: `loja_chatbot_melhorada.py`

Esta versão não usa Programação Orientada a Objetos no código do projeto: não existe
`class LojaApp`, não existe `self`, e a organização foi feita com funções normais,
listas, dicionários e variáveis globais para os widgets principais.

Observação: o `customtkinter` internamente usa objetos, então chamadas como
`ctk.CTkFrame(...)` e `.grid(...)` continuam existindo. Isso é uso da biblioteca,
não criação de classes próprias no seu código.

## O que foi melhorado

- Catálogo visual com cards.
- Busca por nome ou categoria.
- Carrinho com quantidade.
- Botões para aumentar, diminuir e remover produto.
- Checkout com nome, telefone, endereço, região e forma de pagamento.
- Cálculo de frete por região.
- Nota fiscal salva com nome único dentro de `notas_fiscais/`.
- Suporte ao cliente salvando mensagens em `suporte_contatos.txt`.
- Visual mais moderno com paleta de cores, cabeçalho, painéis e fontes padronizadas.

## Linhas 1 a 7 - importações

- Linha 1: ignora aviso de importação ausente do analisador `pyrefly`.
- Linha 2: importa `json`, usado para salvar a nota fiscal.
- Linha 3: importa `datetime`, usado para horários, datas e nome de arquivo.
- Linha 4: importa `Path`, usado para montar caminhos de arquivos.
- Linha 5: importa `messagebox`, usado para avisos e confirmações.
- Linha 7: importa `customtkinter` com o apelido `ctk`.

## Linhas 10 a 34 - configuração visual

- Linha 10: separa a área de configuração visual.
- Linha 11: define o modo escuro.
- Linha 12: define o tema azul base do `customtkinter`.
- Linha 14: começa o dicionário `CORES`.
- Linhas 15 a 26: guardam as cores usadas no app, como fundo, painel, botões e textos.
- Linha 27: fecha o dicionário de cores.
- Linhas 29 a 34: criam constantes de fonte para título, subtítulo, seções, texto e botões.

## Linhas 37 a 57 - dados fixos

- Linha 37: separa os dados da loja.
- Linha 38: começa a lista `PRODUTOS`.
- Linhas 39 a 47: cada linha é um produto com `id`, `nome`, `preco` e `categoria`.
- Linha 48: fecha a lista de produtos.
- Linha 50: começa a lista `REGIOES_FORTALEZA`.
- Linhas 51 a 54: cada linha define um bairro e seu frete.
- Linha 55: fecha a lista de regiões.
- Linha 57: cria a lista `FORMAS_PAGAMENTO`.

## Linhas 60 a 74 - variáveis globais

- Linha 60: separa a área de variáveis globais.
- Linha 61: define a pasta onde arquivos serão salvos.
- Linha 62: cria o carrinho como dicionário vazio.
- Linha 64: cria a variável global da janela principal.
- Linhas 65 a 74: criam variáveis globais dos widgets que precisam ser acessados por várias funções.

## Linhas 77 a 99 - funções utilitárias

- Linha 77: separa funções auxiliares.
- Linha 78: cria `formatar_moeda`.
- Linha 79: formata o valor com duas casas decimais.
- Linha 80: troca separadores para o padrão brasileiro, como `R$ 1.234,56`.
- Linha 83: cria `buscar_produto`.
- Linha 84: procura um produto pelo ID e retorna `None` se não encontrar.
- Linha 87: cria `obter_regiao`.
- Linha 88: procura uma região pelo nome do bairro.
- Linha 91: cria `calcular_subtotal`.
- Linhas 92 a 96: somam preço vezes quantidade de todos os itens do carrinho.
- Linha 98: cria `contar_itens`.
- Linha 99: soma todas as quantidades do carrinho.

## Linhas 102 a 126 - layout principal

- Linha 102: separa a montagem da interface.
- Linha 103: cria a função `criar_layout`.
- Linha 104: informa que `conteudo` e `coluna_esquerda` serão variáveis globais.
- Linhas 106 e 107: configuram a expansão da janela principal.
- Linha 109: cria o cabeçalho.
- Linha 111: cria o frame principal do conteúdo.
- Linha 112: posiciona o conteúdo com margem.
- Linhas 113 a 115: configuram as colunas e a linha do conteúdo.
- Linha 117: cria a coluna esquerda.
- Linha 118: posiciona a coluna esquerda.
- Linhas 119 a 122: configuram expansão da coluna esquerda.
- Linhas 124 a 126: chamam as funções que criam catálogo, chat e carrinho.

## Linhas 128 a 178 - cabeçalho

- Linha 128: cria `criar_cabecalho`.
- Linha 129: informa que os labels de status serão globais.
- Linha 131: cria o frame do cabeçalho.
- Linha 132: posiciona o cabeçalho no topo.
- Linha 133: deixa a primeira coluna expansível.
- Linhas 135 e 136: criam e posicionam o bloco do título.
- Linhas 138 a 144: criam o título `Loja C & IA`.
- Linhas 146 a 152: criam o subtítulo.
- Linhas 154 e 155: criam e posicionam o bloco de status à direita.
- Linhas 157 a 166: criam o contador de itens.
- Linha 167: posiciona o contador.
- Linhas 169 a 177: criam o total do carrinho.
- Linha 178: posiciona o total.

## Linhas 180 a 220 - área do catálogo

- Linha 180: cria `criar_area_catalogo`.
- Linha 181: informa que `busca_var` e `catalogo_lista` serão globais.
- Linhas 183 a 186: criam e configuram o painel do catálogo.
- Linhas 188 a 190: criam a barra superior.
- Linhas 192 a 198: criam o título `Catálogo`.
- Linha 200: cria a variável do campo de busca.
- Linhas 202 a 210: criam o campo de busca.
- Linha 211: posiciona o campo.
- Linhas 213 a 218: criam a lista rolável do catálogo.
- Linha 219: permite que os cards ocupem a largura.
- Linha 220: atualiza o catálogo automaticamente quando o texto da busca muda.

## Linhas 222 a 287 - área do chat

- Linha 222: cria `criar_area_chat`.
- Linha 223: informa que `chat_textbox` será global.
- Linhas 225 a 228: criam e configuram o painel do chat.
- Linhas 230 a 232: criam o topo do chat.
- Linhas 234 a 240: criam o título `Conversa`.
- Linhas 242 e 243: criam a área dos botões.
- Linhas 245 a 254: criam o botão `Ver carrinho`.
- Linhas 256 a 265: criam o botão `Suporte`.
- Linhas 267 a 276: criam o botão `Limpar`.
- Linhas 278 a 286: criam a caixa de texto do chat.
- Linha 287: bloqueia edição manual no chat.

## Linhas 289 a 347 - área do carrinho

- Linha 289: cria `criar_area_carrinho`.
- Linha 290: informa que os widgets do carrinho serão globais.
- Linhas 292 a 299: criam o painel lateral do carrinho.
- Linha 300: impede o painel de mudar de largura pelo conteúdo.
- Linhas 301 e 302: configuram expansão interna.
- Linhas 304 a 310: criam o título `Seu carrinho`.
- Linhas 312 a 317: criam a lista rolável do carrinho.
- Linha 318: permite que os cards ocupem a largura.
- Linhas 320 a 322: criam o frame de resumo.
- Linhas 324 a 331: criam o label do subtotal.
- Linhas 333 a 340: criam o label do total.
- Linhas 342 a 347: criam o botão `Finalizar compra`.

## Linhas 349 a 414 - catálogo visual

- Linha 349: separa a área do catálogo.
- Linha 350: cria `mostrar_catalogo`.
- Linhas 351 e 352: apagam cards antigos.
- Linha 354: pega o termo digitado na busca.
- Linhas 356 a 360: filtram produtos por nome ou categoria.
- Linhas 362 a 370: mostram mensagem quando nada é encontrado.
- Linhas 372 e 373: criam um card para cada produto filtrado.
- Linha 375: cria `criar_card_produto`.
- Linhas 376 a 378: criam e posicionam o card.
- Linhas 380 e 381: criam a área de informações do card.
- Linhas 383 a 389: mostram o nome do produto.
- Linhas 391 a 397: mostram categoria e ID.
- Linhas 399 a 405: mostram o preço.
- Linhas 407 a 414: criam o botão `Adicionar`.

## Linhas 416 a 457 - chat

- Linha 416: separa a área do chat.
- Linha 417: cria `escrever_chat`.
- Linha 418: pega o horário atual.
- Linha 419: libera a caixa de texto para escrita.
- Linha 420: insere a mensagem.
- Linha 421: rola para o fim do chat.
- Linha 422: bloqueia a edição novamente.
- Linhas 425 e 426: criam o atalho `bot_fala`.
- Linhas 429 e 430: criam o atalho `usuario_fala`.
- Linhas 433 a 437: limpam o chat e escrevem uma nova mensagem.
- Linha 440: cria `ver_carrinho_no_chat`.
- Linha 441: registra a ação do usuário.
- Linhas 443 a 445: tratam carrinho vazio.
- Linha 447: começa a lista de linhas do resumo.
- Linhas 449 a 453: montam as linhas dos itens.
- Linha 455: adiciona subtotal.
- Linha 456: envia o resumo para o chat.

## Linhas 459 a 588 - carrinho

- Linha 459: separa a área do carrinho.
- Linha 460: cria `adicionar_produto`.
- Linha 461: busca o produto pelo ID.
- Linhas 463 a 465: tratam produto inexistente.
- Linhas 467 e 468: criam o item no carrinho se ele ainda não existe.
- Linha 470: aumenta a quantidade.
- Linhas 471 e 472: registram a ação no chat.
- Linha 473: atualiza o carrinho visual.
- Linha 476: cria `alterar_quantidade`.
- Linhas 477 e 478: ignoram produto que não está no carrinho.
- Linha 480: soma ou subtrai a quantidade.
- Linhas 482 a 485: removem o item quando a quantidade chega a zero.
- Linhas 486 a 489: avisam a nova quantidade.
- Linha 491: atualiza a interface.
- Linha 494: cria `remover_produto`.
- Linhas 495 e 496: ignoram produto ausente.
- Linhas 498 a 501: removem o produto inteiro.
- Linha 504: cria `atualizar_resumo_carrinho`.
- Linhas 505 e 506: apagam cards antigos.
- Linhas 508 a 514: mostram `Carrinho vazio`.
- Linhas 515 a 517: recriam cards do carrinho.
- Linhas 519 a 522: calculam subtotal, quantidade e plural.
- Linhas 524 a 527: atualizam subtotal, total e cabeçalho.
- Linha 529: cria `criar_card_carrinho`.
- Linhas 530 a 533: pegam produto, quantidade e total do item.
- Linhas 535 a 537: criam o card.
- Linhas 539 a 545: mostram nome do produto.
- Linhas 547 a 553: mostram quantidade e valor.
- Linhas 555 e 556: criam a área dos botões.
- Linhas 558 a 568: criam o botão `-`.
- Linhas 570 a 580: criam o botão `+`.
- Linhas 582 a 588: criam o botão `X`.

## Linhas 590 a 655 - suporte

- Linha 590: separa a área de suporte.
- Linha 591: cria `abrir_suporte`.
- Linhas 592 a 597: criam e configuram a janela de suporte.
- Linhas 599 a 605: mostram o título da janela.
- Linhas 607 a 613: mostram o label `Mensagem`.
- Linhas 615 e 616: criam o campo da mensagem.
- Linhas 618 a 624: mostram o label do contato.
- Linhas 626 e 627: criam o campo de contato.
- Linha 629: cria a função interna `enviar_suporte`.
- Linhas 630 e 631: leem mensagem e contato.
- Linhas 633 a 635: impedem envio sem mensagem.
- Linha 637: define o arquivo de suporte.
- Linhas 639 a 644: salvam a mensagem no arquivo.
- Linhas 646 a 648: registram no chat e fecham a janela.
- Linhas 650 a 655: criam o botão de envio.

## Linhas 657 a 853 - checkout e nota fiscal

- Linha 657: separa a área de checkout.
- Linha 658: cria `criar_campo`.
- Linhas 659 a 665: criam o label de um campo.
- Linhas 667 a 669: criam a entrada de texto e retornam essa entrada.
- Linha 671: cria `texto_resumo_checkout`.
- Linhas 672 a 674: calculam subtotal, frete e total.
- Linhas 676 a 680: retornam o texto do resumo.
- Linha 683: cria `criar_nota_fiscal`.
- Linhas 684 a 687: calculam subtotal, frete, total e iniciam lista de itens.
- Linhas 689 a 704: percorrem o carrinho e montam os itens da nota.
- Linhas 706 a 718: retornam o dicionário completo da nota fiscal.
- Linha 720: cria `salvar_nota_fiscal`.
- Linha 721: define a pasta das notas.
- Linha 722: cria a pasta se ela não existir.
- Linha 724: monta data/hora com microssegundos para evitar nomes repetidos.
- Linha 725: cria o caminho do arquivo.
- Linhas 727 e 728: salvam o JSON formatado.
- Linha 730: retorna o caminho salvo.
- Linha 733: cria `abrir_checkout`.
- Linhas 734 a 736: impedem finalizar carrinho vazio.
- Linhas 738 a 744: criam e configuram a janela de checkout.
- Linhas 746 a 752: mostram o título.
- Linhas 754 a 756: criam campos de nome, telefone e endereço.
- Linhas 758 a 764: mostram o label da região.
- Linhas 766 a 776: criam o menu de região.
- Linhas 778 a 784: mostram o label da forma de pagamento.
- Linhas 786 a 796: criam o menu de pagamento.
- Linhas 798 a 810: criam o resumo de valores.
- Linhas 812 e 813: atualizam o resumo quando a região muda.
- Linha 815: cria a função interna `confirmar_compra`.
- Linhas 816 a 818: leem os dados digitados.
- Linhas 820 a 826: validam campos obrigatórios.
- Linhas 828 a 834: criam a nota fiscal.
- Linha 835: salva a nota.
- Linhas 837 a 841: registram sucesso no chat.
- Linhas 843 a 846: limpam carrinho, atualizam tela e fecham a janela.
- Linha 848: conecta mudança de região à atualização do resumo.
- Linhas 844 a 852: criam o botão de confirmação.

## Linhas 855 a 877 - inicialização

- Linha 855: separa a inicialização do programa.
- Linha 856: cria `iniciar_app`.
- Linha 857: informa que `app` será global.
- Linha 859: cria a janela principal.
- Linhas 860 a 864: configuram título, tamanho, mínimo e cor de fundo.
- Linhas 866 a 868: criam interface, catálogo e carrinho vazio.
- Linhas 869 a 872: escrevem a mensagem inicial do bot.
- Linha 874: inicia o loop da janela.
- Linha 876: verifica se o arquivo está sendo executado diretamente.
- Linha 877: chama `iniciar_app`.

## Resumo da lógica

O código está dividido assim:

1. Configuração visual.
2. Dados fixos da loja.
3. Variáveis globais.
4. Funções de cálculo e busca.
5. Funções que montam a interface.
6. Funções do catálogo.
7. Funções do chat.
8. Funções do carrinho.
9. Funções de suporte.
10. Funções do checkout e da nota fiscal.
11. Função final que inicia o programa.

Essa organização continua simples para apresentar em sala, porque usa funções normais
em vez de classe, mas mantém o app com aparência e recursos mais profissionais.
