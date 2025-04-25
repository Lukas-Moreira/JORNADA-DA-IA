# Capítulo 3: Treinamento de Redes Neurais 🧠

## 🧮 Função de Custo e Aprendizado

Para que uma rede neural aprenda, é necessário medir a precisão de suas previsões. Isso é feito através de uma **função de custo** (ou **função de perda**), que avalia o quanto a saída da rede difere do valor real esperado.

Quanto menor o valor da função de custo, melhor o desempenho da rede.

Essas funções orientam o aprendizado da rede, indicando **como os pesos devem ser ajustados** para minimizar o erro.

---

### 📊 Principais Funções de Custo

- **Erro Quadrático Médio (Mean Squared Error - MSE)**  
  Usado em tarefas de regressão.  
  Calcula a média dos quadrados das diferenças entre as previsões e os valores reais.

- **Entropia Cruzada (Cross-Entropy)**  
  Usada em tarefas de classificação.  
  Mede a diferença entre duas distribuições probabilísticas: a previsão e o rótulo real.  
  - Para classificação binária, é amplamente utilizada por sua eficácia.

- **Erro Absoluto Médio (Mean Absolute Error - MAE)**  
  Calcula a média das diferenças absolutas entre as previsões e os valores reais.  
  É menos sensível a outliers do que o MSE.

---

## 🔁 Retropropagação (Backpropagation)

A **retropropagação** é o algoritmo responsável por **ajustar os pesos da rede** para minimizar a função de custo. Esse processo ocorre em duas etapas:

1. **Propagação Direta (Forward Propagation)**  
   A entrada percorre a rede até a saída, onde é feita a previsão.

2. **Retropropagação**  
   A partir do erro calculado, os **pesos são ajustados** no sentido de reduzir esse erro, utilizando o gradiente da função de custo.

---

## ⚙️ Otimização

O processo de ajuste dos pesos é realizado por **algoritmos de otimização**. O mais básico é o **Gradiente Descendente**, mas existem versões mais avançadas:

- **SGD (Stochastic Gradient Descent)**  
  Atualiza os pesos com base em um único exemplo ou mini-batch.  
  É mais rápido em grandes conjuntos de dados, mas pode apresentar oscilações.

- **Adam (Adaptive Moment Estimation)**  
  Combina métodos de momento e adaptação de taxa de aprendizado.  
  É amplamente utilizado por sua **eficiência e estabilidade**, principalmente em redes profundas.

- **RMSprop (Root Mean Square Propagation)**  
  Ajusta a taxa de aprendizado com base nos gradientes recentes.  
  É útil em cenários com funções de custo ruidosas.

---

## 🛡️ Regularização e Overfitting

**Overfitting** ocorre quando a rede aprende muito bem os dados de treino, mas não consegue generalizar para novos dados. Algumas técnicas ajudam a evitar esse problema:

- **Dropout**  
  Durante o treinamento, desativa aleatoriamente alguns neurônios em cada iteração, forçando a rede a aprender representações mais robustas.

- **Regularização L2**  
  Penaliza pesos muito grandes adicionando um termo à função de custo, ajudando a reduzir a complexidade da rede.

- **Early Stopping**  
  Monitora a função de custo em um conjunto de validação e **interrompe o treinamento** quando o desempenho começa a piorar, prevenindo overfitting.

---
📁 *Este conteúdo faz parte da minha jornada de estudos em IA, com experimentos práticos implementados em Python e frameworks como TensorFlow.*