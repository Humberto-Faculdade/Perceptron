# Perceptron Simples - Porta AND  

Este projeto implementa um perceptron do zero em Python para aprender a porta lógica **AND**.  
A ideia foi treinar o modelo usando apenas operações matemáticas básicas, sem bibliotecas externas de machine learning.  

---

##  Como funciona  

- Dados usados: tabela verdade da porta AND  
- Inicialização aleatória dos pesos e bias  
- Função de ativação: degrau (step function)  
- Ajuste dos pesos feito a cada época com base no erro  
- No final, o perceptron consegue prever corretamente todas as entradas  

Tabela verdade usada:  

| Entrada 1 | Entrada 2 | Saída |
|-----------|-----------|-------|
| 0         | 0         | 0     |
| 0         | 1         | 0     |
| 1         | 0         | 0     |
| 1         | 1         | 1     |

---

##  Como executar  

1. Instale o **Python 3**.  
2. Salve o código em um arquivo `perceptron_and.py`.  
3. No terminal, rode:  

```bash
python perceptron_and.py

