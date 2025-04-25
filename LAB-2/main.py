#Importando as bibliotecas necessárias
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2

#Dados de exemplo (entrada):
x = np.array([[0,0],[0,1],[1,0],[1,1]])

#Rótulos (saída espereda)
y = np.array([[0],[1],[1],[0]])

#Definindo a estrutura do modelo
model = Sequential()

model.add(Dense(8,input_dim=2,activation='relu',kernel_regularizer=l2(0.01)))   # Camada oculta com 8 neuronios, ReLU e regularização L2
model.add(Dropout(0.5))                                                         # Drpout para regularização
model.add(Dense(1,activation='sigmoid'))                                        # Camada de saida com ativação sigmoid

#Compilando o modelo
model.compile(loss="binary_crossentropy",optimizer=Adam(learning_rate=0.01),metrics=["accuracy"])
#Treinando o modelo
model.fit(x,y,epochs=200,verbose=0,validation_split=0.25)

#Avaliação do modelo
_,accuracy = model.evaluate(x,y)
print(f"Acurácia do modelo: {accuracy*100:.2f}%")

#Fazendo previsões
predictions = model.predict(x)
print("Previsões")
print(predictions)
print("\n")

# Convertendo probabilidades para rótulos binários (0 ou 1)
class_labels = np.round(predictions)
print("Rótulos previstos:")
print(class_labels)