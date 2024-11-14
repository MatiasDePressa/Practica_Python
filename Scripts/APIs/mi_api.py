from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MiApi(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        data = {
            "mensaje": "hola mundo",
            "estado": "funcionando"
        }

        self.wfile.write(json.dumps(data).encode("utf-8"))

def run():
    servidor = HTTPServer(("localhost", 8080), MiApi)
    print("Servidor corriendo en http://localhost:8080")
    servidor.serve_forever()

if __name__ == "__main__":
    run()
