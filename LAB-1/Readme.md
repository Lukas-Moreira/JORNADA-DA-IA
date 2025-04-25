# Descrição do capítulo 2: `Fundamentos de Redes Neurais`

## O que é uma Rede Neural?

O ponto de partida para se começar a trabalhar com IA é definir o que é uma rede neural, bom ela é uma estrutura computacional inspirada no funcionamento do cérebro humano. Seu objetivo é, através dos nós, processarem e transmitir informações assim com os neurônios biológicos, esse processo fica conhecido como aprendizado por representação, onde a informação é processada por várias camadas, permitindo que a rede aprenda padrões complexos. 

## Estrutura de uma Rede
1. **Camada de Entrada**:
    - Camada de entrada de dados, podendo ser imagem, texto ou série temporal. Cada nó da camada de entrada representa uma característica (ou variável) de dados.
    
2. **Camadas Ocultas**:
    - Aqui é onde a mágica acontece, essa é a parte oculta entre a camada de entrada e saída. Cada camada oculta é composta de neurônios que aplicam transformações nos dados. O número de camdas ocultas e neurônios em cada camada define a "profundidade" da rede neural.

3. **Camada de Saída**:
    - Fornece o resultado final da rede. No caso de uma tarefa de classificação, cada neurônio na camada de saída representa uma classe possível.

### Conexões e Pesos
    - Cada neurônio de entrada está conectado a outro neurônio da camada seguinte, e essa conexão possui pesos que vão definir a importância dessa conexão no processo de aprendizado, esses pesos podem ser ajustados durante o treinamento para melhorar o desempenho da rede.

## Propagação direta
  - A propagação direta é o processo pelo qual a informação flui através da rede, da camada de entrada até a camada de saída:

```
Formula básica do Neurônio: Seja um neurônio que recebe entradas x1, x2, ..., xn com pesos w1, w2, ..., wn e um viés b. O valor de ativação z é calculado como:

    z = w1 * x1 + w2 * x2 + ... + wn * xn + b
```

  - O que essa função quer dizer: Cada neurônio da camada oculta realiza uma soma ponderadados sinais recebidos da camada anterior, adicionando um valor de viés antes de aplicar uma função de ativação, que é responsável por gerar a saída.

## Função de ativação
- **Sigmoid**:
  - Produz uma saída entre 0 e 1, muito boa para classificação binária.

- **Tanh**:
  - Produz uma saída entre -1 e 1 sua vantagem é de centralizar os dados em torno de zero.

- **ReLU**:
  - A Relu é usada por ser computacionalmente eficiente e ajuda a mitigar o problema do gradiente desaparecendo em redes profundas.

- **Softmax**:
  - Normaliza a saída em uma distribuição de probabilidade, sendo ideal para problemas de classificação com múltiplas classes.

---

## Exemplo prático:

No código `main.py`, foi criada uma rede neural com uma camada de 4 neurônios com a função de ativação ReLU e uma camada de saída com função sigmoid, esse exemplo se assemelha a porta digital XOR que para que a saída seja 1, pelo menos uma das entradas deve ser diferente da outra entrada.