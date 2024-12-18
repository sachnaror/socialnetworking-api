# SOCIALNETWORKING API


## How to run locally

* Download this repo or run: 
```bash
    $ git clone https://github.com/sachnaror/socialnetworking-api.git
```

#### In the root directory:
- Install all dependencies
```bash
    $ pip install -r requirements.txt
```
- Create an `.env` file and copy the contents from the `.env.example` to the file and set the respective values. A postgres database can be created with PG ADMIN or psql

- Run Locally
```bash
    $ python manage.py migrate 
```
```bash
    $ uvicorn socialnetworking.asgi:application --reload
```

- Run With Docker
```bash
    $ docker-compose up --build -d --remove-orphans
```
OR
```bash
    $ make build
```

- Test Coverage
```bash
    $ pytest --disable-warnings -vv
```
OR
```bash
    $ make test
```

## Docs
<!-- #### API Url: [Socialnetworking Docs](http://127.0.0.1:8000/)  -->
#### Swagger: [Documentation](https://swagger.io/docs/)

![alt text](https://github.com/sachnaror/socialnetworking-api/blob/main/display/display1.png?raw=true)

![alt text](https://github.com/sachnaror/socialnetworking-api/blob/main/display/display2.png?raw=true)

![alt text](https://github.com/sachnaror/socialnetworking-api/blob/main/display/display3.png?raw=true)

![alt text](https://github.com/sachnaror/socialnetworking-api/blob/main/display/display4.png?raw=true)

![alt text](https://github.com/sachnaror/socialnetworking-api/blob/main/display/display5.png?raw=true)

![alt text](https://github.com/sachnaror/socialnetworking-api/blob/main/display/display6.png?raw=true)

![alt text](https://github.com/sachnaror/socialnetworking-api/blob/main/display/display7.png?raw=true)

![alt text](https://github.com/sachnaror/socialnetworking-api/blob/main/display/display8.png?raw=true)

![alt text](https://github.com/sachnaror/socialnetworking-api/blob/main/display/display9.png?raw=true)

![alt text](https://github.com/sachnaror/socialnetworking-api/blob/main/display/display10.png?raw=true)

<!-- ## ADMIN PAGE
![alt text](https://github.com/sachnaror/socialnetworking-api/blob/main/display/admin.png?raw=true) -->
