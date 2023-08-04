# X-Ray Classification

X Ray Classsification é um serviço para realizar a classificação de doenças com
base em imagens de raio X toráxicos.

A classificação é feita em uma dos seguintes estados:

- Normal
- COVID-19
- Opacidade pulmonar
- Pneumonia viral

A IA utilizada foi treinada com a seguinte Dataset [COVID-19 Chest X-Ray Database](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database)

## Dependências


## API Endpoints

Get the health status of API

```sh
curl -s http://127.0.0.1:5000/health -X GET | jq .
{
  "cpu": 6.9,
  "mem": 51.6,
  "status": "healthy",
  "uptime": "1:33:01.822082"
}
```

Create an account
```sh
curl -s http://127.0.0.1:5000/user/create -X POST -H 'Content-type: application/json' --data-binary '{"user": "mwb", "pass": "mypass"}'
{
    "token": "2c387b391fc1307b4da5c79925867d42"
}
```


Get token authentication

```sh
curl -s http://127.0.0.1:5000/user/login -X POST -H 'Content-type: application/json' --data-binary '{"user": "mwb", "pass": "mypass"}'
{
    "token": "2c387b391fc1307b4da5c79925867d42"
}
```

Get a image classification
```sh
curl -s http://127.0.0.1:5000/image/classify -X POST -F "image=@<image-path>" -H 'auth: <token>'
{
  "classification": "Covid-19",
  "hash": "57e3966c9967840716274d12cac97b52"
}
```
