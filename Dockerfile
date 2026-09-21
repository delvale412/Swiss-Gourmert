# Usar imagem oficial leve do Python
FROM python:3.9-slim

# Definir diretório de trabalho
WORKDIR /code

# Copiar dependências e instalar
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copiar o resto do código
COPY ./app /code/app

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]