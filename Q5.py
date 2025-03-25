from http.server import SimpleHTTPRequestHandler, HTTPServer

host = ('0.0.0.0', 8080)

class ServidorHTTP(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Servidor Web em Python</h1></body></html>")

if __name__ == "__main__":
    with HTTPServer(host, ServidorHTTP) as servidor:
        print(f"Servidor rodando em http://{host[0]}:{host[1]}")
        servidor.serve_forever()
