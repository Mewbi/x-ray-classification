# 🫁 X-Ray Classification

X Ray Classsification é um serviço para realizar a classificação de doenças com
base em imagens de raio X toráxicos.

A classificação é feita em uma dos seguintes estados:

| Normal | COVID-19 | Opacidade Pulmonar | Pneumonia Viral |
|----------|----------|----------|----------|
| ![normal](/ia/train/1/Normal-10.png) | ![covid-19](/ia/train/0/COVID-10.png) | ![lung-opacity](/ia/train/2/Lung_Opacity-10.png) | ![viral-pneumonia](/ia/train/3/Viral%20Pneumonia-10.png) |

A IA utilizada foi treinada com a seguinte Dataset [COVID-19 Chest X-Ray Database](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database)

## 🛠️ Dependências

O serviço de API utiliza `python3` e as seguintes dependências que podem ser instaladas via gerenciador de pacotes do sistema ou utilizando `pip`:

- flask
- opencv-python
- numpy
- sqlite3

## 🔬 Inicializando

O repositório possui um modelo já treinado. Porém caso queira treinar o modelo novamente é possível fazer conforme descrito em [Treinamento IA](/ia/README.md)

Com todas as dependências instaladas e modelo presente, basta executar o programa `app.py`

```sh
python3 app.py
```

## ⚙️ API Endpoints

Por padrão a API é executada na porta `5000` localmente.

A API usa o formato JSON no conteúdo do `body`

### GET /health

Retorna o status de saúde da API e seu uso de recursos.

**Resposta**

```json
{
    "cpu": 6.9,
    "mem": 51.6,
    "status": "healthy",
    "uptime": "1:33:01.822082"
}
```
---

### POST /user

Cria uma conta na API

**Parâmetros**

| Nome | Local | Tipo | Descrição
|-------------:|:--------:|:-------:| --- |
| `nome` | body | string  | Nome do usuário. |
| `email`| body | string  | E-mail do usuário. |
| `senha`| body | string  | Senha do usuário. |      

**Resposta**

```json
{
    "message": "Usuário criado com sucesso"
}
```

---

### POST /user/login

Realiza o login na aplicação

**Parâmetros**

| Nome | Local | Tipo | Descrição
|-------------:|:--------:|:-------:| --- |
| `email`| body | string  | E-mail do usuário. |
| `senha`| body | string  | Senha do usuário. |      

**Resposta**

```json
{
    "message": "Informações de login corretas",
    "user": {
        "email": "pass",
        "nome": "mwb",
        "user_id": 1
    }
}
```

---

### POST /image/classify

Realiza a classificação de uma imagem de Raio-X

**Parâmetros**

| Nome | Local | Tipo | Descrição
|-------------:|:--------:|:-------:| --- |
| `user_id` | body | string  | ID da conta do usuário. |
| `username`| body | string  | Nome do paciente. |
| `age`| body | string  | Idade do paciente. |
| `name` | body | string  | Nome da imagem de Raio-X. |
| `date`| body | string  | Data de envio da imagem. |
| `image`| body | string  | Base64 da imagem de Raio-X que será classificada pela IA. |    

**Resposta**

```json
{
    "age": 21,
    "date": "02/08/2023",
    "hash": "fb262f0de1b69e0cabf1fb407a5846d0",
    "name": "Torax do paciente alterado",
    "result": "Lung opacity",
    "user_id": 1,
    "username": "Paciente da Silva"
}
```

---

### GET /image/classifications/<user_id>

Busca todas as imagens que foram classificadas por um usuário.

**Parâmetros**

| Nome | Local | Tipo | Descrição
|-------------:|:--------:|:-------:| --- |
| `user_id`| URL | string  | ID da conta do usuário. |

**Resposta**

```json
[
    {
        "age": 255,
        "date": "23/03/2901",
        "hash": "7099fcfdb795fc5975aa31a5700e2047",
        "id": 1,
        "name": "Torax do paciente Clodoaldo",
        "result": "Covid-19",
        "user_id": 1,
        "username": "Clodoaldo"
    },
    {
        "age": 21,
        "date": "02/08/2023",
        "hash": "fb262f0de1b69e0cabf1fb407a5846d0",
        "id": 3,
        "name": "Torax do paciente alterado",
        "result": "Lung opacity",
        "user_id": 1,
        "username": "Paciente da Silva"
    }
]
```

---

### GET /image/\<hash>

Retorna a imagem que foi classificada no formato Base64

**Parâmetros**

| Nome | Local | Tipo | Descrição
|-------------:|:--------:|:-------:| --- |
| `hash`| URL | string  | Hash da imagem que foi classificada. |

**Resposta**

```json
{
    "image": "iVBORw0KGgoAAAANSUhEUgAAASsAAAErCAAAAACjz/poAAAAB3RJTU
    ...
    dzdzVzUVu5u1RjYjVNPQRU0feUQ7X29HoMUXgMl8vblq9u8AAAAASUVORK5CYII="
}
```

---

### DELETE /image/\<hash>/<user_id>

Deleta uma classificação feita previamente em uma conta

**Parâmetros**

| Nome | Local | Tipo | Descrição
|-------------:|:--------:|:-------:| --- |
| `user_id`| URL | string  | ID da conta do usuário. |
| `hash`| URL | string  | Hash da imagem que foi classificada. |

**Resposta**

```json
{
    "hash": "fb262f0de1b69e0cabf1fb407a5846d0",
    "user_id": 1
}
```