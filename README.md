# Wester
A dreamful social networking platform.

## Requirements
+ Python 3.11.1, Old versions may also work!
+ Django 4.1.4

## Installation
1. Rename `wester/settings.example.py` to `settings.py`
2. Generate your own secret key
3. Run the following commands  
    ```bash
    py manage.py makemigrations
    py manage.py migrate
    py manage.py runserver
    ```