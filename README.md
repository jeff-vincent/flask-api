# flask-api

A simple api boilerplate with email/password auth. 

To use:

1. Clone the repo

2. Create a virtual env in the root directory that runs Python3.6. 

3. Install dependencies. From within the env, if you are using one, run:

```pip install -r requirements.txt```

4. Setup MySQL. The current connection string assumes the following:
>a. You have a db in MySQL called `flaskapidb`
>b. You have a db admin user called `root` with a password of `password`

Adjust accordingly. 

5. Run the app. From within the root directory, run:

```python main.py```

6. The app should be up at: 

```http://0.0.0.0:5000```
