# Backend Setup

Backend setup of the checkout kata system.

## Prerequisites

- Python 3.10 or higher
- Django 5.1 or higher

## Installation

### Using `venv`

1. **Clone the Repository**

   ```bash
   git clone https://github.com/subhash-goswami/cart-kata.git
   cd cart-kata/backend
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**

   ```bash
   python src/manage.py migrate
   ```

5. **Run the Development Server**

   ```bash
   python src/manage.py runserver
   ```

6. **Run Tests**

   ```bash
   python src/manage.py test modules.api
   ```

### Using Docker

1. **Clone the Repository**

   ```bash
   git clone https://github.com/subhash-goswami/cart-kata.git
   cd cart-kata/backend
   ```

2. **Build and Run the Docker Containers**

   ```bash
   docker compose up -d --build
   ```

3. **Run Tests in Docker**

   ```bash
   docker exec cart-kata_web python src/manage.py test modules.api
   ```

## API Endpoint

- **Endpoint**: `/api/v1/checkout/`
- **Method**: POST
- **Request Body/Payload**: ```{ "items": "AAABBD" }```
- **Response**: JSON object with the total price

   
### You can test it by making a POST request. 
   ```
    curl --location '127.0.0.1:8000/api/v1/checkout/' \
    --header 'Content-Type: application/json' \
    --data '{
        "items": "ABCD"
    }'
   ```

## Example Responses

- For an empty cart:
  ```json
  {
    "total": 0
  }
  ```

- For items `AAABBD`:
  ```json
  {
      "total": 190
  }
  ```

## Project Structure

```
.
├── docker-compose.yml
├── Dockerfile
├── entrypoint.sh
├── LICENSE
├── README.md
├── requirements.txt
└── src
    ├── app
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── db.sqlite3
    ├── manage.py
    └── modules
        ├── api
        │   ├── admin.py
        │   ├── apps.py
        │   ├── exceptions.py
        │   ├── __init__.py
        │   ├── migrations
        │   │   └── __init__.py
        │   ├── models.py
        │   ├── pricing.py
        │   ├── tests.py
        │   ├── urls.py
        │   ├── utils.py
        │   └── views.py
        └── __init__.py
```
## Acknowledgments

- Django REST Framework for providing easy-to-use class-based views.
- Django for the web framework.
