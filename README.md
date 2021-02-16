# With virtual environment

***Create the virtual environment(Windows)***

````
python -m venv graph-api-env
````

***Activate the virtual environment(Windows)***

````
source \graph-api-env\Scripts\activate
````

***Install all packages***

Make sure to activate the virtual environment

````
pip install -r requirements.txt
````

***Migrate DataBase***

Make sure to activate the virtual environment

````
python manage.py migrate
````


***load data fixtures***

````
python manage.py loaddata graphql_api/fixtures/users.json
````

***Run server (http://localhost:8000/graphql)***

Make sure to activate the virtual environment

````
python manage.py runserver
````

# With Docker
***Docker Build***

````
docker build -t local/graphql_api:beta .
````

***Docker Run***

````
docker run -p 8000:8000 local/graphql_api:beta
````

# With docker-compose
***Run docker-compose***

````
docker-compose up
````

# Tests

***Run the tests***

Make sure to activate the virtual environment

````
python manage.py test
````

***Users Schema***


````
{
  users {
    id
    name
    followers {
      name
    }
    postSet {
      content
    }
  }
}

````

***User Schema***


````
{
  user (id:1) {
    id
    name
    followers {
      name
    }
    postSet {
      content
    }
  }
}

````

