# Python Backend REST API with Database application

This is a bare-bones application providing a REST
API to a database model for CRUD.

## Local Install

### Install

    pip install requirements.txt

### Run the app (Which will run on port 5000)

    flask run

## Docker Install (Which will run on port 8080)

### Install

    docker-compose up

# REST API

The REST API to the idea app is described below.

## Get list of ideas

### Request

`GET /Ideas/`

    curl --location --request GET http://localhost:8080/Ideas

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    [{"id":1,"idea":"Foo"},{"id":2,"idea":"Bar"}]

## Create a new Idea

### Request

`POST /Ideas/`

    curl --location --request POST http://localhost:8080/Ideas?idea=Foo

### Response

    HTTP/1.1 201 Created
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Location: /idea/1
    Content-Length: 36

    {"id":1,"idea":"Foo"}

## Get a specific Idea

### Request

`GET /Ideas/<idea_id>`

    curl --location --request GET http://localhost:8080/Ideas/1

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 36

    {"id":1,"idea":"Foo"}

## Update an Idea

### Request

`UPDATE /Ideas/<idea_id>`

    curl --location --request PUT DELETE http://localhost:8080/Ideas/2?idea=Bar

### Response

    HTTP/1.1 204 No Content
    Date: Thu, 24 Feb 2011 12:36:33 GMT
    Status: 204 No Content
    Connection: close

## Delete an Idea

### Request

`DELETE /Ideas/<idea_id>`

    curl --location --request DELETE http://localhost:8080/Ideas/2/

### Response

    HTTP/1.1 204 No Content
    Date: Thu, 24 Feb 2011 12:36:33 GMT
    Status: 204 No Content
    Connection: close

### Questions for Patrick

How do I see the db? Can't find the info "Adam Test" "Id 1"
When setting up a separate db, How do I add to that from flask via Terminal?
Challenge getting curl or postman working

<!-- <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p> -->

###Adam's Notes:

## make sure docker is opened before composing up docker-compose.yaml file

###todos

1finish python p
2podcast make a list of dope python podcasts
3cry
4figure out DB design
5plan for projects
6google db design
7find python / flask learning options
8work on fetch
