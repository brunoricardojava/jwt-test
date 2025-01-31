# Test JWT - Projeto Django com JWT

Este é um projeto Django configurado para autenticação via JWT, utilizando o `djangorestframework-simplejwt` para tokens JWT, com ferramentas para testes, cobertura de código e documentação.

## Requisitos para rodar o projeto via Docker

- Docker ([para execução com contêineres](https://docs.docker.com/engine/install/))

## Instalação e Configuração

### 1. Clone o Repositório

Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/jwt-test.git
cd jwt-test
```
A aplicação vai ficar disponivel no endereço [http://0.0.0.0:5001/api/v1/docs/#/](http://0.0.0.0:5001/api/v1/docs/#/)

### 2. Rodar aplicação no container

```bash
docker compose up
```

ENDPOINTS:

- [GET] /admin - Django admin padrão

- [GET] /api/v1/user

- [GET] /api/v1/admin

- [POST] /api/v1/token

- [POST] /api/v1/toekn/refresh

### 3. To run the tests, use:

```bash
docker compose exec web make test
```

## Imagens

![image](https://github.com/user-attachments/assets/3f3983e7-c4c8-413e-9493-9f261bfea361)

![image](https://github.com/user-attachments/assets/1dd460cf-2031-4adc-a40c-8a2d5e83a87d)

![image](https://github.com/user-attachments/assets/ce01cd35-1b4c-48aa-b5ae-eaa331f157ee)


![image](https://github.com/user-attachments/assets/cc1e2607-5f99-4dcf-831a-37141aab9a82)

![image](https://github.com/user-attachments/assets/a12b5351-7d10-48f3-925e-b8d17018c006)


