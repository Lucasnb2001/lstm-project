### **Rodando a API localmento**  
Para que isso funcione, é necessário estar em um ambiente Linux.

### Opção padrão:
Terminal (no diretório do projeto)

🔹 1. Criar o ambiente Conda
$ conda create -n name-api python=3.9 -y

🔹 2. Ativar o ambiente
$ conda activate name-api

🔹 3. Instalar os pacotes necessários no ambiente (demora...)
$ pip install fastapi uvicorn tensorflow scikit-learn numpy pandas

🔹 5. Rodar a API
$ uvicorn app:app --reload

🔹 6. Go to: http://127.0.0.1:8000/docs

### Outra alternativa:
Terminal (no diretório do projeto)

🔹 1. Criar o ambiente Conda
$ conda env create -f environment.yml

🔹 2. Ativar o ambiente
$ conda activate text-api

🔹 3. Rodar a API
$ uvicorn main:app --reload

🔹 6. Go to: http://127.0.0.1:8000/docs