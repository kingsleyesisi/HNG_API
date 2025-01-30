# HNG TECH STAGE 0 BACKEND

## Description
This project displays basic information about the registration email, current date and time, and a URL to this GitHub repository in a JSON API. The information is stored in a local SQLite3 database.

## Setup Instructions

### Prerequisites
- Python 3

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/kingsleyesisi/HNG_API.git
    ```
2. Navigate to the project directory:
    ```bash
    cd HNG12
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Project Locally
1. Start the development server:
    ```bash
    python manage.py runserver
    ```
    For Linux and Mac:
    ```bash
    python3 manage.py runserver
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/info`. 
2.1 Or use the public URL `https://hng-api-de1o.onrender.com/info`.

## API Documentation

### Endpoints

#### GET `https://hng-api-de1o.onrender.com/info`
- Description: This is the main endpoint to get the information.
- Response:
    ```json
    {
        "email": "my-email@example.com",
        "current_datetime": "2025-01-30T15:40:35.028602",
        "github_url": "https://github.com/kingsleyesisi/HNG_API"
    }
    ```

## LICENSE
This project is under the MIT license.
