Các thư viện cần cài đặt:
asgiref==3.8.1
attrs==24.3.0
tzdata==2024.2
dj-database-url==2.3.0
Django==4.2.17
django-heroku==0.3.1
djangorestframework==3.15.2
djangorestframework-simplejwt==5.3.1
drf-spectacular==0.28.0
gunicorn==23.0.0
importlib-resources==6.4.5
inflection==0.5.1
jsonschema==4.23.0
jsonschema-specifications==2023.12.1
packaging==24.2
pkgutil-resolve-name==1.3.10
psycopg2==2.9.10
PyJWT==2.9.0
python-decouple==3.8
PyYAML==6.0.2
referencing==0.35.1
rpds-py==0.20.1
sqlparse==0.5.3
typing-extensions==4.12.2
tzdata==2024.2
uritemplate==4.1.1
whitenoise==6.7.0
zipp==3.20.2





để chạy dự án cần làm như sau:
python manage runserver

để test các api có thể dùng postman hoặc try cập đường dẫn sau(swagger): https://test-mci.onrender.com/api/docs/

truy cập api https://test-mci.onrender.com/api/docs/#/account/account_token_create
dùng tài khoản 'user1', password:123 để lấy token access sau đó có thể truy cập các api quản lý


