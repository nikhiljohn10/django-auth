# django-auth

```
# Update system
sudo apt update && sudo apt upgrade -y && sudo apt autoremove

# Install dependencies
sudo apt install -y libpq-dev python3-dev python3-pip python3-venv

# Install 
pip install -r requirements.txt

./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser --username admin --email admin@localhost
./manage.py runserver 0.0.0.0:8000
```