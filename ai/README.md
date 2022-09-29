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
./venv/Scripts/activate
~~~

Dentro do ambiente, podemos baixar as dependencias do projeto

~~~
pip install -r requirements.txt
~~~

E o conjunto de stopwords fornecido pela NLTK

~~~
python nltk_setup.py
~~~

Por fim lançamos o Jupyter

~~~
jupyter-notebook
~~~
