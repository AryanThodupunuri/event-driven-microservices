# Event Driven Microservices

## Tech:  

- Python
- Django
- Flask
- SQLAlchemy
- MySQL
- RabbitMQ
- Docker

## System Architecture  

![diagram](https://user-images.githubusercontent.com/73492002/182219050-71557077-350e-4d31-b52d-a53c5e88948c.PNG)


## Overview
The app is divided into 2 main microservices:  

- Admin
  - Allows CRUD operations on products using Django REST
  - Produces Products' data via RabbitMQ to the main service
  - Consumes RabbiMQ messages from the main service to pefrom updates on products
<br>
- Main  
  - Allows to Edit/Delete/Like products where it's updated in the main serivce  
  - Consumes products' data and save it into Flask's db using SQLAlchemy
  - Produces events to update data in the admin service
  
## How to run the app
- Main
  - cd into the main directory and spin up the server using docker:  
  `docker-compose up --build`
  - ssh into the backend container:  
  `docker-compose exec backend ssh`  
  - Create migration files:  
  `python manager.py db init`  
  - Apply the db migrations :  
  `python manager.py db migrate`  
  `python manager.py db upgrade`
- Admin
  - cd into the admin directory and spin up the server using docker:  
  `docker-compose up --build`
  - ssh into the backend container to:  
  `docker-compose exec backend ssh`
  - Migrate Django's models into the db:  
  `python manage.py makemigrations`  
  `python manage.py migrate`

## Endpoints
- Main
  - GET `/api/products` Fetch all products from admin db
  - POST `/api/products/<int:id>/like` Like a product
- Admin
  - GET `/api/products` Get all products
  - POST `/api/products` Create a new product
  - GET `/api/products/<str:pk>` Get one product
  - PUT `/api/products/<str:pk>` Update product
  - DELETE `/api/products/<str:pk>` Delete product
