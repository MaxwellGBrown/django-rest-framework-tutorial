# django-rest-tutorial

https://www.django-rest-framework.org/tutorial/quickstart/


## quickstart

```
docker build -t django-rest-tutorial .
docker run -it -v $(pwd):/usr/src/app --name django-rest-tutorial-migration --rm django-rest-tutorial migrate
docker run -d -p 8081:80 -v $(pwd):/usr/src/app --name django-rest-tutorial-wsgi --rm django-rest-tutorial
```
