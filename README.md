
  # Perceptron para Porta Lógica AND

  Este projeto demonstra a implementação de um algoritmo Perceptron, um dos modelos fundamentais de redes
  neurais, para resolver o problema da porta lógica AND. O relatório a seguir detalha os conceitos, o
  funcionamento e a aplicação do modelo.

  ---

  ### 1. O que é um Perceptron?

  O Perceptron é um algoritmo de aprendizado de máquina criado por Frank Rosenblatt em 1958, inspirado no
  funcionamento de um único neurônio. Ele recebe múltiplas entradas, associa um peso a cada uma delas e, a
  partir da soma ponderada, gera uma saída binária (0 ou 1).

  Sua relevância histórica está em ser o primeiro modelo a demonstrar que uma máquina poderia aprender com a
   experiência de forma supervisionada. Ao ajustar seus pesos para minimizar erros, o Perceptron estabeleceu
   a base teórica que abriu caminho para as redes neurais complexas e para o campo de Deep Learning.

  ---

  ### 2. Como o Perceptron Funciona?

  O Perceptron é um classificador linear. Isso significa que sua função é encontrar uma única linha (ou um
  hiperplano, em mais de duas dimensões) que consiga separar os dados em duas classes distintas. Problemas
  como as portas lógicas AND e OR são exemplos clássicos de cenários linearmente separáveis.

  As limitações do modelo são uma consequência direta dessa característica:

  - Problemas Não-Lineares: Sua limitação mais conhecida é a incapacidade de resolver a porta lógica XOR,
  pois não há uma única linha reta capaz de dividir corretamente as saídas do problema.
  - Generalização Limitada: Por ser um modelo simples, ele não consegue capturar padrões complexos, o que o
  torna inadequado para a maioria dos problemas do mundo real, que exigem arquiteturas mais robustas como as
   Redes Neurais de Múltiplas Camadas (MLPs).

  ---

  ### 3. Etapas do Treinamento no Código

  O processo de treinamento implementado neste projeto seguiu 6 etapas principais:

  1.  Estruturação dos Dados: Definição das entradas e saídas esperadas, seguindo a tabela-verdade da porta
  AND.
  2.  Inicialização de Pesos e Bias: Atribuição de valores numéricos, pequenos e aleatórios, para os pesos
  sinápticos e o bias.
  3.  Cálculo da Previsão: Para cada entrada, a saída da rede foi calculada usando a soma ponderada e uma
  função de ativação degrau (step function).
  4.  Avaliação do Erro: A saída prevista pelo modelo foi comparada com a saída esperada para quantificar o
  erro.
  5.  Ajuste dos Parâmetros: Com base no erro, os pesos e o bias foram reajustados para aproximar o modelo
  da resposta correta.
  6.  Repetição (Épocas): O ciclo foi repetido por um número definido de épocas, garantindo que o modelo
  aprendesse com os dados até minimizar ou zerar o erro.

  Ao final, o modelo treinado foi validado para confirmar sua capacidade de prever corretamente todas as
  saídas da porta AND.

  ---

  ### 4. Exemplo de Aplicação: Filtro de Spam Simplificado

  Um caso de uso ideal para o Perceptron é a criação de um filtro de spam de e-mail de baixa complexidade.

  - Cenário: Classificar e-mails como "Spam" ou "Não Spam".
  - Features (Entradas):
      - Presença de palavras-chave ("grátis", "promoção").
      - O remetente é desconhecido.
      - Uso excessivo de texto em maiúsculas.
  - Justificativa:
    É uma tarefa de classificação binária (Spam/Não Spam) que pode ser resolvida de forma linear para uma
  primeira camada de defesa. O Perceptron é rápido, leve e fácil de treinar, tornando-o perfeito para
  sistemas com recursos limitados ou como um classificador base em um sistema mais complexo, onde a
  velocidade é mais importante que a precisão absoluta.
  `
