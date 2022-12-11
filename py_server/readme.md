### Core python server.
* we are going to use http.server module to do this.
* there are two ways to create a server in python using http.server.

1. using command line
```
python -m http.server
```
   - this will serve the data of that dir that we are currently in.


* we can use this to locally connect two computers
```
- to know your adapter ip/host address
ipconfig 

- python -m http.serve PORT -b HOST
python -m http.server 8000 -b 192.168.0.109
```    

2. using python
- see server.py


### Resources
* [Simple HTTP server in python - Video](https://www.youtube.com/watch?v=DeFST8tvtuI)