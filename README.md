# Segundo Examen Parcial - Big Data

En este repositorio se encuentra un proyecto, el cual corresponde a el parcial del segundo corte de la materia fundamentos de ML (Machine learning) en computacion avanzada, en este repositorio se encuentra, el dataset implemetado, el codigo en python en un cuaderno notebook (.ipynb), codigo fuentes del Programa LR en C++, y el documento (Readme.md) que presenta el contenido 

## Desarrollo ⚙️

Desarrollar los ETL y un Workflow en AWS Glue para la descarga de información de periódicos (eltiempo y el espectador):

a) Crear un Job en AWS Glue(con un trigger) que descargue cada dia la página principal de el Tiempo y El Espectador(o publímetro).
La información debe quedar en S3 con la estructura:

* s3://bucket/headlines/raw/contenido-yyyy-mm-dd.html

b) Una vez llega el archivo a la carpeta raw, se debe activar un segundo job que procese los
datos que llegaron utilizando Beautifulsoup. Este proceso debe extraer la categoría, el
titular y el enlace para cada noticia. Estos datos se deben guardar en un csv en la
siguiente ruta:

* s3://bucket/headlines/final/periodico=xxx/year=xxx/month=xxx/day=xxx

Para usar paquetes externos revisar:

https://aws.amazon.com/es/premiumsupport/knowledge-center/glue-version2-external-python-libraries/

c) Una vez terminados estos jobs, se debe activar un crawler que actualice el catálogo de
AWS Glue y permita visualizar los datos en AWS Athena.

d) Crear un Job que inserte la información en una base de datos MYSQL(usando aws glue connectors y aws job). Para esto se debe crear la BD de MYSQL en RDS con la respectiva tabla. Luego se debe mapear con un crawler al catálogo del glue. Finalmente crear el job con la interfaz que copie de tabla a tabla(la que representa s3 y la que representa RDS en el catálogo).

- Activar la opción “job bookmarks” cuando se cree el job por interfaz. Esto permite que glue lleve una trazabilidad de los datos insertados y evita que se vuelvan a insertar datos ya insertados.


## Conclusiones 📋

* Los coeficientes de C++ y los realizados con SKLearn en python son parecidos
* Se aprendio a como hacer la implemetacion desde cero de una regresion lineal, desde cargar un archivo, hasta mostrar los datos

## Construido con 🛠️

Herramientas que utilizamos para el proyecto

* [Colab](https://colab.research.google.com/drive/122yDvWKHggehFmqg5oM2CqJUsyJcTAjH#scrollTo=M2Z55G32TwQL) - Notebook
* [Qt](https://qr.io/) - Framework

## Fuentes de informacion 📖

* https://medium.com/@lachlanmiller_52885/understanding-and-calculating-the-cost-function-for-linear-regression-39b8a3519fcb

![Terminal](https://github.com/shelsyrod/Parcial2-BD/blob/master/TerminalMySql.png)

![Workflow](https://github.com/shelsyrod/Parcial2-BD/blob/master/workflow.jpeg)

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Juan Carlos Castro Guevara**  - [Correo](juan.castro03correo.usa.edu.com)
* **Shelsy Natalia Rodriguez Barajas**  - [Correo](shelsy.rodriguez01@correo.usa.edu.co)
