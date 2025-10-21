# Jogo da forca
Projeto - Programação 1

Plano de Mudanças para o Jogo da Forca - Programação 1

Olá, pessoal!

Este documento detalha as mudanças e melhorias propostas para o nosso projeto do jogo da forca, trazendo a modernização do frotend e a integração da lógica do jogo.

### 1. Análise do Código Existente

**1.1. `forcaGame.py` (Lógica do Jogo no Console)**

*   **Pontos Fortes:**
    *   Implementa a lógica básica do jogo da forca: contagem de tentativas, exibição da palavra oculta, registro de letras tentadas.
    *   Define o limite de 5 erros para a derrota, conforme especificado.

*   **Pontos a Melhorar:**
    *   **Palavra Fixa:** A palavra secreta é definida estaticamente (`'TECLADO'`). Precisamos que seja carregada de um arquivo e escolhida aleatoriamente.
    *   **Interface:** É um jogo de console, e o objetivo é criar uma interface gráfica moderna.
    *   **Condição de Vitória:** O jogo não verifica explicitamente a vitória antes das tentativas acabarem, o que pode ser melhorado para uma experiência mais fluida.

**1.2. `forcaTKINTER.py` (Esboço de Interface Gráfica com Tkinter)**

*   **Pontos Fortes:**
    *   Inicia uma janela gráfica usando Tkinter.
    *   Define elementos básicos como título, tamanho da janela e um botão de saída.
    *   Possui um campo de entrada para a letra do usuário.

*   **Pontos a Melhorar:**
    *   **Lógica Não Integrada:** A interface não está conectada à lógica do jogo. Não há processamento de palpites, atualização da palavra ou contagem de tentativas.
    *   **Design Básico:** O Tkinter padrão oferece um visual mais antigo. A solicitação é por uma interface *moderna* e *fluida*.

### 2. Proposta de Nova Interface Frontend e Integração

Para atender aos requisitos de uma interface moderna e funcional, a proposta é utilizar a biblioteca **CustomTkinter**.

**2.1. Por que CustomTkinter?**

*   **Visual Moderno:** Oferece widgets com um design mais contemporâneo e personalizável, com suporte a temas claros e escuros.
*   **Base no Tkinter:** Como já iniciamos com Tkinter, o CustomTkinter é uma extensão natural e mais fácil de adaptar, pois mantém a sintaxe e a estrutura familiar.
*   **Funcionalidades Aprimoradas:** Permite criar interfaces mais agradáveis e interativas com menos esforço do que o Tkinter puro.

**2.2. Implementação da Nova Interface (`forca_gui.py`)**

O novo arquivo `forca_front.py` foi criado para integrar a lógica do jogo com a nova interface gráfica. As principais características são:

*   **Carregamento de Palavras de Arquivo:**
    *   Uma função `carregar_palavras('palavras.txt')` foi implementada para ler palavras de um arquivo de texto, uma por linha. Isso atende ao requisito de palavras pré-definidas e aleatórias.
    *   As palavras são convertidas para maiúsculas e espaços em branco são removidos para padronização.

*   **Lógica do Jogo Integrada:**
    *   Todo o controle do jogo (seleção aleatória da palavra, registro de letras corretas/erradas, contagem de tentativas) agora está dentro da classe da interface.
    *   A palavra secreta é escolhida aleatoriamente no início de cada novo jogo.
    *   As tentativas são limitadas a 5, e o jogo termina ao atingir esse limite ou ao adivinhar a palavra.

*   **Interface Gráfica Interativa:**
    *   **Elementos Visuais:** Título do jogo, exibição da palavra oculta (com `_` para letras não adivinhadas), contador de tentativas restantes, lista de letras erradas.
    *   **Entrada de Usuário:** Campo de texto para o palpite de uma letra, com um botão "Adivinhar" e suporte para o uso da tecla Enter.
    *   **Feedback:** Mensagens claras para o usuário (letra correta, letra errada, já tentou, vitória, derrota).
    *   **Controle de Jogo:** Botão "Novo Jogo" para reiniciar a partida a qualquer momento.

*   **Atualização Dinâmica:** A interface é atualizada automaticamente após cada palpite, mostrando o estado atual da palavra, tentativas e letras erradas.

### 3. Como Executar o Jogo (Passo a Passo)

Para que todos possam testar e ver a nova interface, sigam estes passos em seus computadores:

1.  **Verificar Python:** Certifiquem-se de que têm o Python 3 (versão 3.6 ou superior) instalado.

2.  **Instalar CustomTkinter:** Abram o terminal ou prompt de comando e executem:
    ```bash
    pip install CustomTkinter
    ```
    *Se tiverem várias versões do Python, usem `pip3 install CustomTkinter`.*

3.  **Criar o arquivo `palavras.txt`:**
    *   Na mesma pasta onde vocês vão salvar o código Python do jogo, criem um arquivo chamado `palavras.txt`.
    *   Adicionem as palavras que desejam usar, uma por linha. Exemplo:
        ```
        PYTHON
        PROGRAMACAO
        COMPUTADOR
        ALGORITMO
        DESENVOLVIMENTO
        SEGURANCA
        SOFTWARE
        MUSICA
        ```

4.  **Salvar o código `forca_front.py`:**
    *   Salvem o código completo da nova interface (que foi compartilhado anteriormente) em um arquivo chamado `front.py` na mesma pasta do `palavras.txt`.

5.  **Executar o Jogo:**
    *   No terminal ou prompt de comando, naveguem até a pasta onde salvaram os arquivos (usando o comando `cd` para mudar de diretório).
    *   Executem o jogo com o comando:
        ```bash
        python forca_front.py
        ```

Isso abrirá a janela do jogo da forca com a nova interface gráfica.

