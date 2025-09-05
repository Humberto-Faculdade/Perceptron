#  Perceptron - Implementação da Porta AND

## 1. Conceito
O **Perceptron** é o modelo mais simples de rede neural artificial, criado por Frank Rosenblatt em 1958.
Ele foi o primeiro algoritmo capaz de aprender padrões a partir de exemplos, ajustando seus pesos com base nos erros cometidos durante o treinamento.
Apesar de ser um modelo básico, teve enorme importância histórica porque abriu caminho para o desenvolvimento de técnicas modernas de **Machine Learning** e **Deep Learning**.

---

## 2. Funcionamento
O Perceptron funciona como um **classificador linear**, ou seja, ele consegue traçar uma linha (ou hiperplano, em dimensões maiores) que separa duas classes distintas.
Isso significa que ele é eficiente para resolver problemas **linearmente separáveis**, como a porta lógica **AND** ou **OR**.

**Limitações:**
- Não consegue resolver problemas **não linearmente separáveis**, como o caso clássico da porta lógica **XOR**.
- Sua capacidade de aprendizado é restrita a padrões simples. Para problemas complexos, é necessário usar múltiplas camadas (MLPs – Multi Layer Perceptrons).

---

## 3. Código
No código implementado, as principais etapas do treinamento do Perceptron foram:

1. **Definição dos dados de entrada e saída esperada** (tabela verdade da porta AND).
2. **Inicialização aleatória dos pesos e bias.**
3. **Cálculo da saída prevista** usando a função de ativação degrau.
4. **Cálculo do erro** comparando a saída prevista com a saída esperada.
5. **Atualização dos pesos e do bias** de acordo com a regra de aprendizado do Perceptron.
6. **Repetição por várias épocas** até que o erro total se torne zero (ou mínimo possível).
7. **Teste final** para verificar se o modelo aprendeu corretamente a função AND.

---

## 4. Aplicação prática
Um exemplo real em que um modelo simples como o Perceptron pode ser útil é em **sistemas de detecção binária simples**, como:

- **Classificação de e-mails em spam ou não spam** (considerando regras lineares básicas, como presença/ausência de determinadas palavras).

Justificativa: mesmo que hoje existam algoritmos muito mais sofisticados, um Perceptron ainda pode ser aplicado em situações onde a decisão depende apenas de **regras lineares e simples**, com baixo custo computacional.

---
