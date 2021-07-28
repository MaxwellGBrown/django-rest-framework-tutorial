# django-rest-tutorial

https://www.django-rest-framework.org/tutorial/quickstart/


## quickstart

```
docker build -t django-rest-tutorial .
docker run -it -v $(pwd):/usr/src/app --name django-migration --rm django-rest-tutorial migrate
docker run -d -p 8000:80 -v $(pwd):/usr/src/app --name django-rest-tutorial --rm django-rest-tutorial
```
