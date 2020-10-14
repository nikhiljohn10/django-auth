# django-auth

```
# Update system
sudo apt update && sudo apt upgrade -y && sudo apt autoremove

# Install dependencies
sudo apt install -y libpq-dev python3-dev python3-pip python3-venv

# Clone project
git clone https://github.com/nikhiljohn10/django-auth && cd django-auth

# Create Python virtial environment and activate it
python3 -m venv venv && . venv/bin/activate

# Install python dependencies
pip install -r requirements.txt

# Edit your changes in the project

# Create migrations for django models
./manage.py makemigrations
./manage.py migrate

# Create super user
./manage.py createsuperuser --username admin --email admin@localhost

# Run server
./manage.py runserver 0.0.0.0:8000
```