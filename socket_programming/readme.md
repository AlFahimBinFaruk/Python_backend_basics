### Socket programming
* Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server.
Socket Programming provides the ability to 
  * implement real time analytic
  * instant messaging(socket.io)
  * binary streaming
  * document collaboration.

#### HTTP vs Sockets
* HTTP is an application protocol. It basically means that HTTP itself can't be used to transport information to/from a remote end point. Instead it relies on an underlying protocol which in HTTP's case is TCP.

* You can read more about OSI layers(http://en.wikipedia.org/wiki/OSI_model) if you are interested.

* Sockets on the other hand are an API that most operating systems provide to be able to talk with the network. The socket API supports different protocols from the transport layer and down.

* That means that if you would like to use TCP you use sockets. But you can also use sockets to communicate using HTTP, but then you have to decode/encode messages according to the HTTP specification (RFC2616). Since that can be a huge task for most developers we also got ready clients in our developer frameworks (like .NET), for instance the WebClient or the HttpWebRequest classes.

* Note : both HTTP and sockets do the same thing.both use TCP, it's just that HTTP responds in a predefined format and socket gives data as returned from another end of a socket


### Resources
* [Python socket programming tutorial(core)](https://www.youtube.com/watch?v=3QiPPX-KeSc)
* [A Beginner's Guide to WebSockets](https://www.youtube.com/watch?v=8ARodQ4Wlf4)