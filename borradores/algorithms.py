from math import e 

# RNA - Artificial Neural Network

# ----- RELU ACTIVATION FUNCTION -----
def relu(x):
    return max(0, x)

print(relu(0))  # Output: 0
print(relu(-1))  # Output: 0
print(relu(1))  # Output: 1

# ----- SIGMOID ACTIVATION FUNCTION -----
def sigmoid(x):
    return 1 / (1 + e **(-x))

print (sigmoid(0))  # Output: 0.5
print (sigmoid(1))  # Output: 0.7310585786300049

# ----- TANH ACTIVATION FUNCTION -----
def tanh(x):
    return (e ** x - e ** (-x)) / (e ** x + e ** (-x))

print(tanh(0))  # Output: 0.0
print(tanh(1))  # Output: 0.7615941559557649

# ----- AND LOGIC GATE -----
def and_gate(a, b):
    return 1 if a == 1 and b == 1 else 0

print(and_gate(1, 1))  # Output: 1
print(and_gate(1, 0))  # Output: 0



