import SimpleHTTPServer
import SocketServer
import sys
sys.path.insert(0, "../")
import sys_constant as sc

PORT = sc.TOPO_SERVER_PORT

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "--> Topo server is serving at port", PORT
httpd.serve_forever()