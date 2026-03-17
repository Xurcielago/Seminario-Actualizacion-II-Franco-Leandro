import http.server
import socketserver


PUERTO = 5000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PUERTO), Handler) as servidor:
    
    print(f"Servidor Python iniciado correctamente.")
    print(f"Servidor iniciado en: http://localhost:{PUERTO}")
    
    servidor.serve_forever()