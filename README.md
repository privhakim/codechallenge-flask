# codechallenge-flask

## Pizza Restaurants API

This project implements a Flask API for managing pizza restaurants. It includes functionalities like handling restaurants, pizzas, and their associations.

## Table of Contents
- [Models](#models)
- [Validations](#validations)
- [Routes](#routes)
- [Running the Server](#running-the-server)
- [Testing Endpoints with Postman](#testing-endpoints-with-postman)

## Models

The application involves three main models:
- **Restaurant**: Represents a pizza restaurant.
- **Pizza**: Represents a type of pizza available at restaurants.
- **RestaurantPizza**: Represents the association between a restaurant and a pizza.

## Validations

The models have specific validations to ensure data integrity:
- **RestaurantPizza**:
  - Price must be between 1 and 30.

- **Restaurant**:
  - Name must be less than 50 characters in length.
  - Name must be unique.

## Routes

The API provides the following routes for interaction:

- **GET /restaurants**: Retrieve a list of all restaurants.
  - Response format:
    ```json
    [
      {
        "id": 1,
        "name": "Dominion Pizza",
        "address": "Good Italian, Ngong Road, 5th Avenue"
      },
      {
        "id": 2,
        "name": "Pizza Hut",
        "address": "Westgate Mall, Mwanzi Road, Nrb 100"
      }
    ]
    ```

- **GET /restaurants/:id**: Retrieve details of a restaurant by ID.
  - Response format for valid restaurant:
    ```json
    {
      "id": 1,
      "name": "Dominion Pizza",
      "address": "Good Italian, Ngong Road, 5th Avenue",
      "pizzas": [
        {
          "id": 1,
          "name": "Cheese",
          "ingredients": "Dough, Tomato Sauce, Cheese"
        },
        {
          "id": 2,
          "name": "Pepperoni",
          "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
        }
      ]
    }
    ```
  - Response format for invalid restaurant:
    ```json
    {
      "error": "Restaurant not found"
    }
    ```

- **DELETE /restaurants/:id**: Delete a restaurant by ID.

- **GET /pizzas**: Retrieve a list of all pizzas.
  - Response format:
    ```json
    [
      {
        "id": 1,
        "name": "Cheese",
        "ingredients": "Dough, Tomato Sauce, Cheese"
      },
      {
        "id": 2,
        "name": "Pepperoni",
        "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
      }
    ]
    ```

- **POST /restaurant_pizzas**: Create a new RestaurantPizza associated with an existing Pizza and Restaurant.

## Running the Server

1. Install the necessary dependencies using `pip install -r requirements.txt`.
2. Set the `FLASK_APP` environment variable:
    ```bash
    export FLASK_APP=app.py
    ```
3. Run the Flask application:
    ```bash
    flask run
    ```

## Testing Endpoints with Postman

Import the provided Postman collection and use it to test the API endpoints.

