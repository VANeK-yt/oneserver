
# OneServer by m133

### A python web server whith python scripting


## Example

```python
import server
#this a oscript initer
def oscript(arg, filename): 
    if filename == 'helloworld.oscript': #this is oscript helloworld.oscript
        return f"Hello {arg}!" # it returns string Hello {arg}!
    else:
        return server.notfoundpage() # if not found script return 404 error page
    #now try to go to localhost:8080/helloworld.oscript?t=World and you see Hello World!

server.run(oscript) # this line runs server
```


