# Fleet Management API

## Índice

* [1. Resumen del proyecto](#1-resumen-del-proyecto)
* [2. Características](#2-características)
* [3. Tecnologías](#3-tecnologías)
* [4. Endpoints Principales](#4-endpoints-principales)

***

## 1. Resumen del proyecto

Este proyecto consiste en la construcción de una API REST para la gestión de flotas, específicamente para la consulta de ubicaciones de taxis. La API está diseñada para cargar y consultar la información de casi 10,000 taxis, almacenada en una base de datos PostgreSQL. A través de varios endpoints, permite la consulta de taxis y sus trayectorias, además de ofrecer funcionalidades de autenticación y gestión de usuarios.


## 2. Características

* Carga masiva de información desde archivos SQL a una base de datos PostgreSQL.
* Listado de taxis con soporte de paginación y filtrado por número de placa.
* Consulta de trayectorias por taxi y fecha, con datos de latitud, longitud y timestamp.
* Endpoint para consultar la última ubicación de cada taxi.
* CRUD de usuarios para la plataforma, con autenticación mediante JWT.
* Protección de endpoints con JWT.
* Pruebas unitarias y de integración con Postman.


## 3. Tecnologías

* Lenguajes: Python (Flask)
* Bases de datos: PostgreSQL
* Autenticación: JWT (JSON Web Token)
* ORM: SQLAlchemy
* Testing: Postman


## 4. Endpoints Principales

* GET /taxis: Listado de todos los taxis con paginación y filtrado por placa.
* GET /trajectories: Consulta de todas las trayectorias de un taxi en una fecha específica.
* GET /trajectories/latest: Consulta de la última ubicación reportada por cada taxi.
* CRUD /users: Este conjunto de endpoints permite crear, leer, actualizar y eliminar usuarios en la plataforma.
* POST /auth/login: Autenticación de usuarios y obtención de JWT.
