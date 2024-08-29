#### Commands
##### Part 1:
git clone https://github.com/andyjud/django-starter.git . && rm -rf .git <br/>
python3 -m venv venv <br/>
source venv/bin/activate <br/>
pip install --upgrade pip <br/>
pip install -r requirements.txt <br/>
docker compose up -d <br/>
pip install psycopg2-binary <br/>
python manage.py migrate <br/>
python manage.py createsuperuser <br/>
python manage.py runserver <br/>
ctrl + c <br/>
python manage.py makemigrations
