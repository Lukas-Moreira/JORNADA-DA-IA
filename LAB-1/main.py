#Importando as bibliotecas necessárias
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

#Dados de exemplo (entrada):
x = np.array([[0,0],[0,1],[1,0],[1,1]])

#Rótulos (saída espereda)
y = np.array([[0],[1],[1],[0]])

# O exemplo trata-se de um classificador binário, logo na camada de saída é utilizado uma 
# ativação sigmoid, pois ela é capaz de produzir uma saída entre 0 e 1.

#Definindo a estrutura do modelo
model = Sequential()

model.add(Dense(4,input_dim=2,activation='relu'))   ### Camada oculta com 4 neuronios e ReLU
model.add(Dense(1,activation='sigmoid'))            ### Camada de saida com ativação sigmoid

#Compilando o modelo
model.compile(loss='binary_crossentropy',optimizer=SGD(learning_rate=0.1),metrics=['accuracy'])
model.fit(x,y,epochs=1000, verbose=0)

#Avaliação do modelo
_,accuracy = model.evaluate(x,y)
print(f"Acurácia do modelo: {accuracy*100:.2f}%")

#Fazendo previsões
predictions = model.predict(x)
print("Previsões")
print(predictions)

# Convertendo probabilidades para rótulos binários (0 ou 1)
class_labels = np.round(predictions)
print("Rótulos previstos:")
print(class_labels)