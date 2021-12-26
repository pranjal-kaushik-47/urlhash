<h1>
Initial Setup
</h1>

<h2>
Clone the git repository
</h2>

```
git clone https://github.com/pranjal-kaushik-47/urlhash.git
```

<h2>
Navigate to the project folder
</h2>

```
cd urlhash
```

<h2>
Crete a vertual environment
</h2>

* linux

    ```
    python3 -m venv env
    ```

* Windows
    ```
    python -m venv env
    ```

<h2>
Activate the vertual environment
</h2>

* linux

    ```
    source env/bin/activate
    ```

* Windows
    ```
    .\env\Scripts\activate
    ```

<h2>
Installing Requirements
</h2>

```
pip install -r requirements.txt
```

<h2>
Redis
</h2>

* Linus : <a src=https://redis.io/topics/quickstart>Redis</a>

* Windows : <a src=https://redis.io/download>Redis</a>

After installing Redis run the redis server on port 6379

<br>
<br>

<h1>
Django Setup
</h1>

Navigate to the project folder ( where the manage.py is present ) and place the provided .env file.

<h2>
Migrations
</h2>

```
python3 manage.py makemigrations short
python3 manage.py migrate
```

<h2>
Start the server
</h2>

```
python3 manage.py runserver
```

<h2>
Start celery
</h2>
Open a second terminal in the project folder

<br>

<h3>
Activate the vertual environment
</h3>

* linux

    ```
    source env/bin/activate
    ```

* Windows
    ```
    .\env\Scripts\activate
    ```

<h3>
start celery
</h3>

```
celery -A urlhash worker -B
```

** Note : Make sure redis server is running on prot 6379 before staarting celery