# IA

Esse módulo é destinado para o treinamento do modelo de IA para classificação de Raio X

## Dependências

É necessário que sejam instaladas as seguintes dependências

```
opencv
numpy
tensorflow
matplotlib
```

## Treinamento da IA

O treinamento da IA para geração do modelo pode ser feita de duas maneiras:

- Localmente
- Google Colab

Por questões de praticidade (e até performance) é recomendado que seja usado o Google Colab para fazer o treinamento

### Google Colab


### Localmente


## Teste da IA

Com o modelo treinado é possível fazer o teste da IA utilizando o programa `test.py`

Nele são selecionadas imagens alteatórias do diretório de testes e é comparado o resultado esperado com o classificado pela IA

O programa que realiza o teste não requer muita capacidade computacional, assim não é necessário que seja executado no Google Colab.

Para executar os testes basta rodar o comando

```sh
python3 test.py
```

**Resultados**

É retornado algumas métricas referentes a assertividade das classificações feitas pela IA.

```
aaa
```

Além disso, é retornado visualmente as imagens que foram classificadas, tendo o resultado esperado e o resultado classificado pela IA.

<img>
