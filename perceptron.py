import random

# Dados (porta lógica AND)
X = [[0,0], [0,1], [1,0], [1,1]]
y = [0, 0, 0, 1]

# Hiperparâmetros
learning_rate = 0.1
epochs = 20

# Inicializando pesos e bias aleatórios
weights = [random.uniform(-1, 1) for _ in range(2)]
bias = random.uniform(-1, 1)

def step_function(value):
    return 1 if value >= 0 else 0

def predict(inputs, weights, bias):
    total = sum(w*x for w, x in zip(weights, inputs)) + bias
    return step_function(total)

# Treinamento
for epoch in range(epochs):
    total_error = 0
    for inputs, expected in zip(X, y):
        prediction = predict(inputs, weights, bias)
        error = expected - prediction
        # Atualiza pesos e bias
        weights = [w + learning_rate * error * x for w, x in zip(weights, inputs)]
        bias += learning_rate * error
        total_error += abs(error)
    print(f"Época {epoch+1} - Erro total: {total_error}")

print("\nPesos finais:", weights)
print("Bias final:", bias)

# Testando
for inputs in X:
    print(f"Entrada: {inputs} => Saída prevista: {predict(inputs, weights, bias)}")
