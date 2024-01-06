# Clairvoyance

[Used this template as a base.](https://github.com/pmdevita/Django-Svelte-Template)

Backend: Django
Routing: Inertia.js
Frontend: Svelte + Vite
CSS: Tailwind CSS
UI Library: Flowbite Svelte

## Installation and usage

- Clone and cd into the project
- Create a Python virtual environment (tested on Python 3.10.6)

```shell
python3 -m venv env
```

- Activate the virtual environment

```shell
source env/bin/activate
```

- Install the Python requirements

```shell
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

- Create a Django secret key

```shell
echo "SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')" >> .env
```

- Apply the migrations

```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

- Install the NPM dependencies (tested on npm 9.6.3 and node 19.6.0)

```shell
npm i
```

- Run the Python server

```shell
python3 manage.py runserver
```

- Open another terminal window and run the Vite server

```shell
npm run dev
```

Now open your browser and go to: `http://localhost:8000/`
