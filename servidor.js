const http = require('http');
const fs = require('fs');
const path = require('path');

const PUERTO = 3000;

const servidor = http.createServer((peticion, respuesta) => {
    
    if (peticion.url === '/') {
        
        const rutaArchivo = path.join(__dirname, 'index.html');

        fs.readFile(rutaArchivo, (error, contenido) => {
            if (error) {
                respuesta.writeHead(500, { 'Content-Type': 'text/plain' });
                respuesta.end('Error interno del servidor: No se pudo leer el archivo HTML.');
                return;
            }

            respuesta.writeHead(200, { 'Content-Type': 'text/html' });
            respuesta.end(contenido);
        });

    } else {
        respuesta.writeHead(404, { 'Content-Type': 'text/plain' });
        respuesta.end('Error 404: Recurso no encontrado.');
    }
});

servidor.listen(PUERTO, () => {
    console.log(`Servidor HTTP nativo iniciado correctamente.`);
    console.log(`Servidor iniciado en: http://localhost:${PUERTO}`);
});