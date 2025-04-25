# Capítulo 2: Fundamentos de Redes Neurais 🧠

Este capítulo aborda os conceitos essenciais das redes neurais, explicando desde sua estrutura até o funcionamento de suas funções internas e ativação. Também inclui um exemplo prático de implementação.

---

## 📌 O que é uma Rede Neural?

Uma rede neural é uma estrutura computacional inspirada no cérebro humano, composta por unidades chamadas **neurônios artificiais**. Seu objetivo é processar e transmitir informações por meio de conexões com pesos ajustáveis.

Esse processo é conhecido como **aprendizado por representação**, onde os dados atravessam múltiplas camadas e a rede aprende **padrões complexos**.

---

## 🧱 Estrutura de uma Rede Neural

### 1. Camada de Entrada
Recebe os dados iniciais (imagem, texto, série temporal). Cada nó representa uma **característica (feature)** dos dados.

### 2. Camadas Ocultas
Onde ocorre o **processamento dos dados**. Cada neurônio aplica transformações aos dados com base em pesos e funções de ativação. A quantidade de camadas e neurônios define a profundidade da rede.

### 3. Camada de Saída
Gera o **resultado final da rede**. Em classificação, cada neurônio representa uma **classe possível**.

---

## 🔗 Conexões e Pesos

Cada conexão entre neurônios tem um **peso**, que determina sua importância. Durante o treinamento, esses pesos são ajustados para melhorar o desempenho da rede.

---

## ➡️ Propagação Direta (Forward Propagation)

É o processo de transmissão de dados da entrada até a saída, básicamente aqui é onde a soma ponderada que os neurônios da camada oculta realizam após receberem a os dados da camada anterior, para assim aplicar a função de ativação que é responsável por gerar a saída.

### Fórmula do Neurônio

**z = w1 * x1 + w2 * x2 + ... + wn * xn + b**

Onde:
- `x` = entradas
- `w` = pesos
- `b` = viés
- `z` = valor de ativação antes da função de ativação

---

## ⚙️ Funções de Ativação

As funções de ativação introduzem **não linearidade** na rede. Principais tipos:

- `Sigmoid` → Saída entre 0 e 1 (classificação binária)
- `Tanh`    → Saída entre -1 e 1 (centraliza dados)
- `ReLU`    → Zera valores negativos, eficiente em redes profundas
- `Softmax` → Converte em distribuição de probabilidade (multi-classes)

---

## 💡 Exemplo Prático (`main.py`)

Este capítulo inclui uma rede neural com:
- **Camada oculta com 4 neurônios (ReLU)**
- **Camada de saída com 1 neurônio (Sigmoid)**

Essa rede simula o comportamento de uma **porta lógica XOR**, onde a saída é `1` quando as entradas são diferentes.

---

📁 *Este conteúdo faz parte da minha jornada de estudos em IA, com experimentos práticos implementados em Python e frameworks como TensorFlow.*
