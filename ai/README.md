# Preparando o ambiente

Inicialmente baixe o dataset [Ruddit](https://www.kaggle.com/datasets/rajkumarl/ruddit-jigsaw-dataset) e copie o arquivo "ruddit_with_text" para a pasta datasets

Após isso execute os comandos abaixo para criar um ambiente virtual Python na pasta venv

~~~
python -m venv venv
~~~

A ativação varia de acordo com a plataforma

~~~
# CMD (Windows)
venv\Scripts\activate.bat
~~~

~~~
# BASH (Linux)
./venv/bin/activate
~~~

Dentro do ambiente, podemos baixar as dependências do projeto

~~~
pip install -r requirements.txt
~~~

E o conjunto de stopwords fornecido pela NLTK

~~~
python nltk_setup.py
~~~

## Editando e executando o processo de treino

Para lançarmos o Jupyter pasta executar

~~~
jupyter-notebook
~~~

Ou se você utiliza VS Code, você pode usar a extensão [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) que oferece várias utilidades além de integração com as ferramentas Python já existentes para o editor

Todo o processo de treino está organizado no arquivo [train.ipynb](train.ipynb).

## Demonstração de Servidor de Inferência

O pasta [inferenceserver](infenceserver) contém um pequeno servidor de inferência HTTP. Após o treinamento de modelo, para usa-lo basta executar

~~~
python inferenceserver/main.py
~~~

O servidor espera o comentário como o parâmetro de URL "comment", abaixo estão alguns exemplos de resposta

~~~
{
   "offensive_prob": 0.9,
   "not_offensive_prob": 0.1,
   "classification": "OFFENSIVE"
}
~~~

~~~
{
   "offensive_prob": 0.1,
   "not_offensive_prob": 0.9,
   "classification": "NOT_OFFENSIVE"
}
~~~
