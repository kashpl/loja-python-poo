# Explicação linha por linha - Loja C & IA

Arquivo explicado: `loja_chatbot_melhorada.py`

Este guia explica o código completo já melhorado. Quando uma chamada de `customtkinter`
ocupa várias linhas, a explicação cobre cada opção importante da chamada.

## O que foi melhorado

- O código virou uma classe chamada `LojaApp`, deixando a aplicação mais organizada.
- O catálogo saiu do chat e virou uma área visual com cards.
- O carrinho agora guarda quantidade por produto.
- O carrinho ganhou botões de aumentar, diminuir e remover produto.
- A busca por produto/categoria foi adicionada ao catálogo.
- O checkout agora pede nome, telefone, endereço, região e forma de pagamento.
- A nota fiscal agora é salva em `notas_fiscais/` com nome único.
- O suporte salva mensagens em `suporte_contatos.txt`.
- O visual ganhou paleta de cores, fontes padronizadas, cabeçalho, painéis e espaçamentos.
- O chat deixou de usar `**Markdown**`, porque `CTkTextbox` não interpreta Markdown.


## Linhas 1 a 7 - importações

- Linha 1: ignora o aviso de importação ausente do `pyrefly`, útil quando o analisador não conhece `customtkinter`.
- Linha 2: importa `json`, usado para salvar a nota fiscal em arquivo `.json`.
- Linha 3: importa `datetime`, usado para horário do chat, data da compra e nomes únicos de arquivos.
- Linha 4: importa `Path`, usado para trabalhar com caminhos de arquivos de forma mais segura.
- Linha 5: importa `messagebox`, usado para avisos e mensagens de confirmação.
- Linha 7: importa `customtkinter` com o apelido `ctk`, que é a biblioteca visual da interface.

## Linhas 10 a 12 - tema do app

- Linha 10: marca o começo da configuração visual.
- Linha 11: coloca a aplicação em modo escuro.
- Linha 12: define o tema base azul do `customtkinter`.

## Linhas 14 a 29 - paleta de cores

- Linha 14: cria o dicionário `CORES`, que centraliza todas as cores do app.
- Linha 15: define a cor de fundo principal.
- Linha 16: define a cor dos painéis maiores.
- Linha 17: define a cor dos cards de produto e carrinho.
- Linha 18: reserva uma cor de hover para cards, caso você queira animar depois.
- Linha 19: define a cor principal dos botões.
- Linha 20: define a cor do botão principal ao passar o mouse.
- Linha 21: define a cor de sucesso, usada no botão de finalizar/enviar.
- Linha 22: define o hover da cor de sucesso.
- Linha 23: define a cor de perigo, usada para remover/limpar.
- Linha 24: define o hover da cor de perigo.
- Linha 25: define uma cor neutra para ações secundárias.
- Linha 26: define o hover da cor neutra.
- Linha 27: define a cor de texto principal.
- Linha 28: define a cor de texto secundário.
- Linha 29: fecha o dicionário.

## Linhas 31 a 35 - fontes

- Linha 31: define a fonte do título principal.
- Linha 32: define a fonte do subtítulo.
- Linha 33: define a fonte dos títulos de seção.
- Linha 34: define a fonte de textos comuns.
- Linha 35: define a fonte de botões.

## Linhas 38 a 58 - dados da loja

- Linha 38: marca o começo da área de dados fixos.
- Linha 39: cria a lista `PRODUTOS`.
- Linhas 40 a 48: cada linha cria um produto com `id`, `nome`, `preco` e `categoria`.
- Linha 49: fecha a lista de produtos.
- Linha 51: cria a lista `REGIOES_FORTALEZA`.
- Linhas 52 a 55: cada linha define um bairro e o valor do frete.
- Linha 56: fecha a lista de regiões.
- Linha 58: define as formas de pagamento exibidas no checkout.

## Linhas 61 a 63 - função de moeda

- Linha 61: cria a função `formatar_moeda`.
- Linha 62: formata o número no padrão financeiro, com duas casas decimais.
- Linha 63: troca separadores para o padrão brasileiro, ficando como `R$ 1.234,56`.

## Linhas 66 a 81 - classe principal e inicialização

- Linha 66: cria a classe `LojaApp`, herdando de `ctk.CTk`, a janela principal.
- Linha 67: inicia o construtor `__init__`, executado quando o app abre.
- Linha 68: chama o construtor da classe mãe, obrigatório para a janela funcionar.
- Linha 69: cria `self.carrinho` como dicionário vazio.
- Linha 70: guarda a pasta onde o arquivo `.py` está, usada para salvar notas e suporte.
- Linha 71: define o título da janela.
- Linha 72: define o tamanho inicial da janela.
- Linha 73: define o tamanho mínimo da janela.
- Linha 74: define a cor de fundo principal.
- Linha 75: chama o método que monta toda a interface.
- Linha 76: desenha os cards do catálogo.
- Linha 77: atualiza o carrinho vazio no painel lateral.
- Linhas 78 a 81: escreve a mensagem inicial do bot no chat.

## Linhas 83 a 104 - estrutura geral da tela

- Linha 83: comentário separando a montagem visual.
- Linha 84: cria o método `criar_layout`.
- Linha 85: faz a coluna principal da janela expandir.
- Linha 86: faz a linha do conteúdo expandir.
- Linha 88: chama o método que cria o cabeçalho.
- Linha 90: cria o frame `conteudo`, que segura catálogo/chat/carrinho.
- Linha 91: posiciona `conteudo` usando grid, com margens.
- Linha 92: faz a coluna esquerda ocupar o espaço flexível.
- Linha 93: reserva largura mínima para o carrinho.
- Linha 94: faz a linha principal expandir.
- Linha 96: cria a coluna esquerda.
- Linha 97: posiciona a coluna esquerda.
- Linha 98: permite que a coluna interna expanda.
- Linha 99: dá mais peso ao catálogo.
- Linha 100: dá menos peso ao chat.
- Linhas 102 a 104: criam catálogo, chat e carrinho.

## Linhas 106 a 153 - cabeçalho

- Linha 106: cria o método `criar_cabecalho`.
- Linha 107: cria o frame superior do app.
- Linha 108: posiciona o cabeçalho no topo.
- Linha 109: permite que o lado esquerdo do cabeçalho expanda.
- Linha 111: cria um frame transparente para título e subtítulo.
- Linha 112: posiciona o bloco do título à esquerda.
- Linhas 114 a 119: criam o texto grande `Loja C & IA`.
- Linhas 121 a 126: criam o subtítulo da loja.
- Linha 128: cria o bloco de status à direita.
- Linha 129: posiciona esse bloco à direita.
- Linhas 131 a 140: criam o contador de itens do carrinho.
- Linha 141: posiciona o contador.
- Linhas 143 a 152: criam o total do carrinho no cabeçalho.
- Linha 153: posiciona o total.

## Linhas 155 a 191 - área do catálogo

- Linha 155: cria o método `criar_area_catalogo`.
- Linha 156: cria o painel visual do catálogo.
- Linha 157: coloca o painel na parte superior esquerda.
- Linhas 158 e 159: configuram expansão horizontal e vertical.
- Linha 161: cria a barra superior do catálogo.
- Linha 162: posiciona a barra superior.
- Linha 163: deixa a busca ocupar o espaço restante.
- Linhas 165 a 170: criam o título `Catálogo`.
- Linha 172: cria a variável que guarda o texto digitado na busca.
- Linha 173: manda redesenhar o catálogo sempre que a busca muda.
- Linhas 175 a 182: criam o campo de busca.
- Linha 183: posiciona o campo de busca.
- Linhas 185 a 189: criam a lista rolável de produtos.
- Linha 190: posiciona a lista.
- Linha 191: permite que os cards ocupem a largura disponível.

## Linhas 193 a 255 - área de chat

- Linha 193: cria o método `criar_area_chat`.
- Linha 194: cria o painel do chat.
- Linha 195: posiciona o painel abaixo do catálogo.
- Linhas 196 e 197: configuram expansão do painel.
- Linha 199: cria a barra superior do chat.
- Linha 200: posiciona essa barra.
- Linha 201: deixa o título ocupar espaço.
- Linhas 203 a 208: criam o título `Conversa`.
- Linha 210: cria o frame dos botões de ação.
- Linha 211: posiciona os botões à direita.
- Linhas 213 a 222: criam o botão `Ver carrinho`.
- Linhas 224 a 233: criam o botão `Suporte`.
- Linhas 235 a 244: criam o botão `Limpar`.
- Linhas 246 a 253: criam a caixa de texto do chat.
- Linha 254: posiciona o chat.
- Linha 255: bloqueia edição manual no chat.

## Linhas 257 a 312 - painel do carrinho

- Linha 257: cria o método `criar_area_carrinho`.
- Linhas 258 a 263: criam o painel lateral do carrinho.
- Linha 264: posiciona o carrinho à direita.
- Linha 265: impede que o painel mude de largura por causa do conteúdo.
- Linhas 266 e 267: configuram expansão interna.
- Linhas 269 a 274: criam o título `Seu carrinho`.
- Linhas 276 a 280: criam a lista rolável do carrinho.
- Linha 281: posiciona a lista.
- Linha 282: permite que os itens ocupem a largura.
- Linha 284: cria o frame de resumo inferior.
- Linha 285: posiciona o resumo.
- Linha 286: deixa o botão final ocupar a largura.
- Linhas 288 a 294: criam o texto de subtotal.
- Linhas 296 a 302: criam o texto de total.
- Linhas 304 a 312: criam o botão `Finalizar compra`.

## Linhas 314 a 337 - exibição do catálogo

- Linha 314: comentário separando a lógica do catálogo.
- Linha 315: cria o método `mostrar_catalogo`.
- Linhas 316 e 317: apagam os cards antigos antes de redesenhar.
- Linha 319: pega o texto buscado, em minúsculas e sem espaços extras.
- Linhas 321 a 325: filtram produtos por nome ou categoria.
- Linhas 327 a 334: mostram mensagem quando não há resultado.
- Linhas 336 e 337: criam um card para cada produto filtrado.

## Linhas 339 a 377 - card de produto

- Linha 339: cria o método `criar_card_produto`.
- Linha 340: cria o card visual.
- Linha 341: posiciona o card na lista.
- Linha 342: deixa a área de informação expandir.
- Linhas 344 e 345: criam e posicionam o frame de informações.
- Linhas 347 a 352: mostram o nome do produto.
- Linhas 354 a 359: mostram categoria e ID.
- Linhas 361 a 366: mostram o preço formatado.
- Linhas 368 a 377: criam o botão `Adicionar`, chamando `adicionar_produto`.

## Linhas 379 a 416 - funções do chat

- Linha 379: comentário separando o chat.
- Linha 380: cria `escrever_chat`.
- Linha 381: pega o horário atual.
- Linha 382: libera a caixa de texto para escrita.
- Linha 383: insere a mensagem no chat.
- Linha 384: rola o chat até o final.
- Linha 385: bloqueia a caixa de texto novamente.
- Linhas 387 e 388: criam atalho para fala do bot.
- Linhas 390 e 391: criam atalho para fala do usuário.
- Linhas 393 a 397: limpam o chat e escrevem uma nova mensagem.
- Linha 399: cria `ver_carrinho_no_chat`.
- Linha 400: registra a ação do usuário.
- Linhas 402 a 404: tratam carrinho vazio.
- Linha 406: começa o resumo textual.
- Linhas 407 a 413: percorrem os itens e adicionam linhas de resumo.
- Linha 415: adiciona o subtotal.
- Linha 416: envia o resumo para o chat.

## Linhas 418 a 470 - regras do carrinho

- Linha 418: comentário separando o carrinho.
- Linhas 419 e 420: buscam um produto pelo ID.
- Linha 422: cria `adicionar_produto`.
- Linha 423: encontra o produto.
- Linhas 425 a 427: tratam produto inexistente.
- Linhas 429 e 430: criam o item no carrinho se ele ainda não existe.
- Linha 432: aumenta a quantidade.
- Linha 433: registra a ação do usuário no chat.
- Linha 434: confirma a ação pelo bot.
- Linha 435: atualiza a interface do carrinho.
- Linha 437: cria `alterar_quantidade`.
- Linhas 438 e 439: ignoram IDs que não estão no carrinho.
- Linha 441: soma ou subtrai a quantidade.
- Linhas 443 a 446: remove o produto se a quantidade chegar a zero.
- Linhas 447 a 450: informa a nova quantidade quando o item continua no carrinho.
- Linha 452: atualiza a interface.
- Linha 454: cria `remover_produto`.
- Linhas 455 e 456: ignoram produto ausente.
- Linhas 458 a 461: removem o item e atualizam a tela.
- Linhas 463 a 467: calculam o subtotal.
- Linhas 469 e 470: contam a quantidade total de itens.

## Linhas 472 a 554 - atualização visual do carrinho

- Linha 472: cria `atualizar_resumo_carrinho`.
- Linhas 473 e 474: apagam os cards antigos.
- Linhas 476 a 482: mostram `Carrinho vazio` quando necessário.
- Linhas 483 a 485: recriam os cards do carrinho.
- Linha 487: calcula subtotal.
- Linha 488: calcula quantidade.
- Linha 489: escolhe singular ou plural para `item`.
- Linhas 491 a 494: atualizam subtotal, total e status do cabeçalho.
- Linha 496: cria `criar_card_carrinho`.
- Linhas 497 a 500: pegam produto, quantidade e total do item.
- Linhas 502 a 504: criam o card do item.
- Linhas 506 a 511: mostram o nome do produto.
- Linhas 513 a 518: mostram quantidade e total do produto.
- Linhas 520 e 521: criam a área dos botões.
- Linhas 523 a 532: botão `-`, que diminui a quantidade.
- Linhas 534 a 543: botão `+`, que aumenta a quantidade.
- Linhas 545 a 554: botão `X`, que remove o produto inteiro.

## Linhas 556 a 619 - suporte ao cliente

- Linha 556: comentário separando suporte.
- Linha 557: cria `abrir_suporte`.
- Linhas 558 a 563: criam e configuram a janela de suporte.
- Linhas 565 a 570: mostram o título.
- Linhas 572 a 577: mostram o rótulo `Mensagem`.
- Linhas 579 e 580: criam e posicionam o campo de mensagem.
- Linhas 582 a 587: mostram o rótulo do contato.
- Linhas 589 e 590: criam e posicionam o campo de contato.
- Linha 592: cria a função interna `enviar_suporte`.
- Linhas 593 e 594: leem mensagem e contato.
- Linhas 596 a 598: impedem envio sem mensagem.
- Linha 600: define o arquivo de suporte.
- Linhas 601 a 605: gravam a mensagem no arquivo.
- Linhas 607 a 609: registram no chat e fecham a janela.
- Linhas 611 a 619: criam o botão `Enviar mensagem`.

## Linhas 621 a 741 - checkout

- Linha 621: comentário separando checkout.
- Linha 622: cria `abrir_checkout`.
- Linhas 623 a 625: impedem finalizar carrinho vazio.
- Linhas 627 a 632: criam e configuram a janela de checkout.
- Linhas 634 a 639: mostram o título.
- Linhas 641 a 643: criam campos de nome, telefone e endereço.
- Linhas 645 a 650: mostram o rótulo da região.
- Linha 652: cria a variável da região escolhida.
- Linhas 653 a 661: criam o menu de regiões.
- Linha 662: posiciona o menu de regiões.
- Linhas 664 a 669: mostram o rótulo da forma de pagamento.
- Linha 671: cria a variável da forma de pagamento.
- Linhas 672 a 680: criam o menu de pagamento.
- Linha 681: posiciona o menu de pagamento.
- Linhas 683 a 694: criam o resumo com subtotal, frete e total.
- Linhas 696 e 697: atualizam o resumo quando a região muda.
- Linha 699: conecta a mudança da região ao resumo.
- Linha 701: cria a função interna `confirmar_compra`.
- Linhas 702 a 704: leem os dados do cliente.
- Linhas 706 a 711: validam se os dados obrigatórios foram preenchidos.
- Linhas 713 a 719: criam a nota fiscal em memória.
- Linha 720: salva a nota em arquivo.
- Linhas 722 a 726: registram a compra no chat.
- Linha 728: limpa o carrinho.
- Linha 729: atualiza a interface.
- Linha 730: fecha o checkout.
- Linha 731: mostra onde a nota foi salva.
- Linhas 733 a 741: criam o botão `Confirmar compra`.

## Linhas 743 a 766 - helpers do checkout

- Linha 743: cria `criar_campo`, helper para campos repetidos.
- Linhas 744 a 749: criam o rótulo do campo.
- Linha 751: cria a entrada de texto.
- Linha 752: posiciona a entrada.
- Linha 753: devolve a entrada para quem chamou.
- Linhas 755 e 756: buscam os dados da região pelo bairro.
- Linha 758: cria `texto_resumo_checkout`.
- Linha 759: calcula subtotal.
- Linha 760: pega o frete da região.
- Linha 761: soma subtotal e frete.
- Linhas 762 a 766: devolvem o texto do resumo.

## Linhas 768 a 814 - nota fiscal

- Linha 768: cria `criar_nota_fiscal`.
- Linha 769: calcula subtotal.
- Linha 770: pega o frete.
- Linha 771: calcula total final.
- Linha 773: cria a lista de itens da nota.
- Linhas 774 a 786: percorrem o carrinho e montam cada item da nota.
- Linhas 788 a 802: devolvem o dicionário completo da nota fiscal.
- Linha 804: cria `salvar_nota_fiscal`.
- Linha 805: define a pasta `notas_fiscais`.
- Linha 806: cria a pasta se ela ainda não existir.
- Linha 808: cria data e hora com microssegundos para nome único.
- Linha 809: monta o caminho completo do arquivo `.json`.
- Linhas 811 e 812: salvam a nota em JSON formatado.
- Linha 814: devolve o caminho do arquivo salvo.

## Linhas 817 a 819 - início do programa

- Linha 817: garante que o app só rode quando o arquivo for executado diretamente.
- Linha 818: cria a janela `LojaApp`.
- Linha 819: inicia o loop da interface, mantendo a janela aberta.

## Ideia central do código

O app funciona em quatro partes:

1. Dados fixos: produtos, regiões e formas de pagamento.
2. Interface: cabeçalho, catálogo, chat e carrinho.
3. Regras: adicionar, remover, contar e calcular totais.
4. Finalização: coletar dados, calcular frete e salvar a nota fiscal.

Essa separação deixa o projeto mais fácil de explicar, modificar e apresentar.
