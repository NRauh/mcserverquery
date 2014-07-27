#MCServerQuery
MCServerQuery is a simple web service that can query a Minecraft server and return the info in JSON format.

MCServerQuery is basically a wrapper for the query tool that Dinnerbone built with Python, but takes in the parameters through the request URL.

*Note: You can't query a server running on localhost/127.0.0.1 without hosting a copy of MCServerQuery on your machine. Hosting it yourself is easy to do, but you shouldn't need to unless you're contributing to the code.*

#Querying a server
To query a server, first be sure to set `enable-query` to `true` in the `server.properties` file.  
When querying is enabled, you can send a GET request to `http://mcserverquery.heroku.com/query` with the params...

* `host`
	- Is the server address (ex: example.com, 127.0.0.1)
	- Can be either a domain name or IP address
* `port`
	- The port the server is on (ex: 25565)
* `type`
	- Optional parameter which if set to `simple` will set the query to be a simple query

###Examples
`http://mcserverquery.heroku.com/query?host=example.com?host=example.com&port=25565`  
Would return server info for a server at example.com on port 25565 (example.com:25565)

`http://mcserverquery.heroku.com/query?host=127.0.0.1&port=25565&type=simple`  
Would return the basic server info for a server at 127.0.0.1 on the port 25565

#License
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>