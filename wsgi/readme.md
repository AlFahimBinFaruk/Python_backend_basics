### What is WSGI.
* Purpose. WSGI stands for "Web Server Gateway Interface". It is used to forward requests from a web server (such as Apache or NGINX) to a backend Python web application or framework. From there, responses are then passed back to the webserver to reply to the requestor.

* WSGI is an application server.
* in python Gunicorn is a pure WSGI server.

### why WSGI are used
* WSGI servers are designed to handle many requests concurrently. Frameworks are not made to process thousands of requests and determine how to best route them from the server. WSGI speeds up Python web application development because you only need to know basic things about WSGI
* web servers like apache,nginx cannot communicate with python backend directly that where the application-server or web server gateway interface(WSGI) come.
  * web server(Apache) -> WSGI(gunicorn) -> Flask/Django.