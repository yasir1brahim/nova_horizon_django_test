# Nova Project Setup

This README provides instructions for setting up a Nova project that connects to the Apollo API.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Step 1: Install Python and Create a Virtual Environment](#step-1-install-python-and-create-a-virtual-environment)
- [Step 2: Install Required Packages](#step-2-install-required-packages)
- [Step 3: Run the Development Server](#step-3-run-the-development-server)
- [Step 4: Connect with Apollo](#step-4-connect-with-apollo)

## Prerequisites

- Ensure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

## Step 1: Install Python and Create a Virtual Environment

1. **Install Python**: Download and install Python from the official website.
2. **Create a virtual environment**:
```bash
   python -m venv venv
```
3. **Activate the virtual environment**:
- **On Windows**:
```bash
    venv\Scripts\activate
```
- **On macOS/Linux**:
```bash
    source venv/bin/activate
```

## Step 2: Install Required Packages
- Install packages from the requirements file: Make sure you have a requirements.txt file in your project directory. Then run:
```bash
    pip install -r requirements.txt
```

## Step 3: Run the Development Server
1. **Apply database migrations**:
```bash
    python manage.py migrate
```
2. **Run the server:**
```bash
    python manage.py runserver
```
- Your server should now be running at http://127.0.0.1:8000/.


## Step 4: Connect with Apollo
1. **Set up your Apollo API Key**:
- Make sure to set your Apollo API Key as an environment variable or directly in your code as required by your application.

## Step 5: API Endpoints
1. **Login Endpoint**
- Endpoint: /app/login/
- Method: POST
- Request Body
```json
{
    "username": "your_username",
    "password": "your_password"
}
```
- Response Body
```json
{
    "token": "your_token_here"
}
```
2. **Fetch Account Stages**
- Endpoint: /app/fetch_account_stages/
- Method: GET
- Authentication: Bearer Token
- Headers:
```
    Authorization: Token your_token_here
```
- Response Body
```json
{
    "success": true,
    "stages": [
        {
            "id": "stage_id",
            "team_id": "team_id",
            "display_name": "Cold",
            "name": "Cold",
            "display_order": 0,
            "default_exclude_for_leadgen": false,
            "category": "in_progress",
            "is_meeting_set": null
        }
        // Additional stages...
    ]
}
```
**3. Create Account Stage**
- Endpoint: /app/create_account_stage/
- Method: POST
- Authentication: Bearer Token
- Request Body:
```json
{
    "team_id": "your_team_id",
    "display_name": "New Stage",
    "name": "New Stage",
    "display_order": 5,
    "default_exclude_for_leadgen": false,
    "category": "in_progress",
    "is_meeting_set": null
}
```
- Response Body
```json
{
    "account": {
        "id": "67092cbe8a153201af08d62a",
        "domain": null,
        "name": "New Stage",
        "team_id": "your_team_id",
        "organization_id": null,
        "account_stage_id": "6708f07c267aa201afc6af95",
        "source": "api",
        "original_source": "api",
        "creator_id": null,
        "owner_id": "6708f07f267aa201afc6b14b",
        "created_at": "2024-10-11T13:48:46.345Z",
        // Additional fields...
    }
}
```