Perceptron Simples - Porta AND

Esse projeto é um experimento básico em Python para treinar um perceptron a aprender a porta lógica AND.
A ideia foi implementar tudo do zero, sem usar bibliotecas de machine learning, só para entender melhor como funciona o processo de aprendizado.

O que o código faz

Cria os dados da porta AND (as combinações de 0 e 1 e seus resultados).

Inicializa pesos e bias com valores aleatórios.

Usa uma função de ativação do tipo degrau para decidir entre 0 e 1.

Treina o perceptron ajustando os pesos a cada época.

No final, mostra os pesos aprendidos e testa as previsões com todos os casos possíveis.

Tabela verdade da porta AND usada:

Entrada 1	Entrada 2	Saída
0	0	0
0	1	0
1	0	0
1	1	1
Como rodar

Ter o Python 3 instalado.

Salvar o código em um arquivo, por exemplo perceptron_and.py.

No terminal, executar:

python perceptron_and.py

Exemplo de saída
Época 1 - Erro total: 3
Época 2 - Erro total: 2
...
Época 10 - Erro total: 0

Pesos finais: [0.2, 0.2]
Bias final: -0.3
Entrada: [0, 0] => Saída prevista: 0
Entrada: [0, 1] => Saída prevista: 0
Entrada: [1, 0] => Saída prevista: 0
Entrada: [1, 1] => Saída prevista: 1

Ideias para melhorar

Testar outras portas lógicas (OR, NAND, etc).

Usar funções de ativação diferentes.

Tentar expandir para resolver XOR com múltiplas camadas.
