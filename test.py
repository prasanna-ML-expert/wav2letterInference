import cherrypy

class HelloWorld:
    def index(self):
        return "Hello World!"
    index.exposed = True
if __name__ == '__main__':
   config = {'server.socket_host': '35.190.159.163','server.socket_port' : 8000}
   cherrypy.config.update(config)
   cherrypy.quickstart(HelloWorld())
