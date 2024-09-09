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
python manage.py makemigrations<br/>
<br/>
##### Part 2:
pip install django-tenants <br/>
python manage.py startapp a_tenant_manager <br/>
python manage.py create_tenant <br/>
python manage.py create_tenant_superuser <br/>
<br/>
##### Part 3:
pip install django-colorfield <br/>
{% if color %}style="background-color: {{ color }};"{% endif %} <br/>
{% if logo %}{{ logo.url }}{% else %}{% static 'images/logo.svg' %}{% endif %} <br/>
