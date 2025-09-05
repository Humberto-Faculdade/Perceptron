 # Relatório do Projeto: Perceptron para Porta Lógica AND

  Este README serve como um relatório técnico, respondendo às questões propostas sobre a implementação do
  algoritmo Perceptron.

  ---

  ### 1. Conceito

  Pergunta: Explique, com suas palavras, o que é um Perceptron e qual a sua importância histórica para o
  desenvolvimento da Inteligência Artificial.

  O Perceptron, criado por Frank Rosenblatt em 1958, é um dos primeiros e mais fundamentais modelos de rede
  neural artificial. Ele simula um único neurônio que recebe diversas entradas, atribui pesos a elas e, com
  base na soma ponderada desses valores, produz uma saída binária (0 ou 1).

  Sua importância histórica é imensa porque foi o primeiro algoritmo a provar que uma máquina poderia
  aprender com a experiência. Ao ajustar seus pesos para corrigir erros, o Perceptron demonstrou a
  viabilidade do aprendizado supervisionado, estabelecendo os alicerces teóricos e a inspiração para o
  desenvolvimento de redes neurais mais complexas e, eventualmente, para toda a área de Deep Learning.

  ---

  ### 2. Funcionamento

  Pergunta: O Perceptron é considerado um classificador linear. O que isso significa? Quais são as
  limitações desse tipo de modelo?

  Dizer que o Perceptron é um classificador linear significa que ele só consegue resolver problemas cujas
  classes de dados podem ser separadas por uma única linha reta (ou um hiperplano, em múltiplas dimensões).
  Ele literalmente "traça uma linha" no espaço de dados para dividir os pontos em duas categorias. As portas
   lógicas AND e OR são exemplos clássicos de problemas linearmente separáveis.

  As limitações do modelo derivam diretamente dessa característica:
  - Incapacidade de resolver problemas não-lineares: A limitação mais famosa é a falha em resolver a porta
  lógica XOR, pois não existe uma única linha reta que consiga separar corretamente as saídas desse
  problema.
  - Baixa capacidade de generalização: Por ser muito simples, o modelo não captura padrões complexos,
  tornando-o inadequado para a maioria dos problemas do mundo real sem o uso de arquiteturas mais avançadas,
   como redes com múltiplas camadas (MLPs).

  ---

  ### 3. Código

  Pergunta: Ao analisar o código que você executou, quais foram as etapas principais do processo de
  treinamento do Perceptron?

  O processo de treinamento no código implementado seguiu estas etapas essenciais:

  1.  Definição dos Dados: Foram estabelecidos os dados de entrada e as saídas esperadas, correspondentes à
  tabela-verdade da porta lógica AND.
  2.  Inicialização: Os pesos sinápticos e o valor do bias foram iniciados com valores numéricos pequenos e
  aleatórios.
  3.  Cálculo da Saída: Para cada conjunto de entradas, a saída da rede foi calculada. Isso envolveu a soma
  ponderada das entradas e a aplicação de uma função de ativação degrau (step function) para produzir a
  saída binária (0 ou 1).
  4.  Cálculo do Erro: A saída prevista pelo modelo foi comparada com a saída realmente esperada para
  determinar o erro.
  5.  Ajuste dos Pesos e Bias: Com base no erro, os pesos e o bias foram reajustados de acordo com a regra
  de aprendizado do Perceptron, de modo a aproximar o modelo da resposta correta.
  6.  Iteração (Épocas): O processo foi repetido por um número definido de "épocas" (ciclos de treinamento),
   garantindo que o modelo fosse exposto aos dados múltiplas vezes até que o erro fosse minimizado ou
  zerado.
  7.  Validação: Após o treinamento, o modelo foi testado para confirmar sua capacidade de prever
  corretamente a saída para todas as combinações de entrada da porta AND.

  ---

  ### 4. Aplicação Prática

  Pergunta: Dê um exemplo real em que o uso de um modelo simples como o Perceptron poderia ser útil.
  Justifique sua escolha.

  Um exemplo prático seria em um sistema de controle de qualidade industrial muito simples.

  - Cenário: Imagine uma esteira que produz peças de metal que devem ter um peso mínimo (X) e um comprimento
   máximo (Y) para serem aprovadas. Peças fora dessa especificação devem ser descartadas.
  - Aplicação do Perceptron: Um Perceptron poderia ser treinado para tomar a decisão "Aprovar" (1) ou
  "Rejeitar" (0). As duas entradas seriam o peso e o comprimento da peça. O modelo aprenderia a traçar uma
  "linha de decisão" que separa as peças boas das defeituosas.

  - Justificativa: A escolha se justifica porque o problema é linear e binário. A decisão é simples
  (sim/não) e baseada em regras claras que podem ser representadas por uma fronteira linear. Para uma tarefa
   tão específica, usar um modelo complexo como uma rede neural profunda seria computacionalmente
  desnecessário e caro. O Perceptron oferece uma solução eficiente, rápida e de fácil implementação para
  este tipo de problema.
  `
