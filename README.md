# Segundo Examen Parcial - Big Data

En este repositorio se encuentra el proyecto correspondiente al segundo corte de la materia Big data, se encuentra el proceidmiento, las fuentes de informacion, erra mientas usadas y finalmente una muestra de los resultados

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

* De esta manera se pueden automatizar procesos como la recoleccion, transformacion y carga de datos para hacerlo de manera mas precisa y en menor tiempo sin la necesidad de interaccion humana

## Construido con 🛠️

Herramientas que utilizamos para el proyecto

* [AWS](https://www.awsacademy.com/vforcesite/LMS_Login) - servicios en la nube
* [Terminal]
* [Scripts en python]

## Fuentes de informacion 📖

* https://aws.amazon.com/es/glue/
* https://aws.amazon.com/es/premiumsupport/knowledge-center/glue-version2-external-python-libraries/
* https://docs.aws.amazon.com/es_es/glue/latest/dg/console-crawlers.html

## Resultados ✅

![Terminal](https://github.com/shelsyrod/Parcial2-BD/blob/master/TerminalMySql.png)

![Workflow](https://github.com/shelsyrod/Parcial2-BD/blob/master/workflow.jpeg)

## Autores ✒️

* **Juan Carlos Castro Guevara**  - [Correo](juan.castro03correo.usa.edu.com)
* **Shelsy Natalia Rodriguez Barajas**  - [Correo](shelsy.rodriguez01@correo.usa.edu.co)
