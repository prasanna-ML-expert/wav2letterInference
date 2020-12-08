import cherrypy
import sys

class HelloWorld:
    def index(self):
        return "Hello World!"
    index.exposed = True
if __name__ == '__main__':
   config = {'server.socket_host': '0.0.0.0','server.socket_port' : int(sys.argv[1])}
   cherrypy.config.update(config)
   cherrypy.quickstart(HelloWorld())
