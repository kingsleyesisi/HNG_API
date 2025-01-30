# HNG TECH STAGE 0 BACKENDD

## Description
This project is designed Displayed basic Information about the registration email, 
Current date time and a url to this github repository in a JSON API.


## Setup Instructions

### Prerequisites
-  Python3 and above 


### Installation
1. Clone the repository:
    ```bash
    <!-- git clone https://github.com/kingsleyesisi/yourproject.git -->
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
    for Linux and Mac 
    ```bash
    python3 manage.py runserver
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/info`. 
2.1 Or use the public URL `https://`

## API Documentation

### Endpoints

#### GET http://127.0.0.1:8000/info
- Description: This is the Main Endpoint to get the informatin 
- Response:
    ```json
    {
    "email": "my-email@example.",
    "current_datetime": "2025-01-30T15:40:35.028602",
    "github_url": "https://github.com/kingsleyesisi/HNG"
    }
