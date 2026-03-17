# Proyecto: Implementación de Interfaces y Servidores Web

**Alumnos:** Franco Sian, Leandro Francisco

**Descripción:** Este proyecto demuestra la creación de una interfaz interactiva simple y su despliegue a través de tres métodos arquitectónicos distintos.

---

## Implementación 1: Archivo Local (Frontend Puro)

**Archivo principal:** `index.html`

### Instrucciones de ejecución

1. Abrir el navegador web.
2. En la barra de direcciones, utilizar el protocolo de sistema de archivos escribiendo la ruta absoluta.
   
   *Ejemplo:*
   > `file:///C:/Users/IPF-2026/Desktop/Seminario-Actualizacion-II-Ejercicio-1-Franco-Leandro-main/index.html`
   
   *(Alternativa: Arrastrar el archivo `index.html` directamente a la ventana del navegador).*

### Explicación de cómo funciona

En esta implementación, el navegador actúa como un simple visor de documentos. Lee el archivo `index.html` directamente desde el disco duro del sistema operativo sin realizar ninguna petición de red. La lógica de la aplicación se ejecuta de forma aislada en el entorno del cliente.

---

## Implementación 2: Servidor Web con Node.js

**Archivos necesarios:** `index.html` y `servidor.js`

### Instrucciones de ejecución

1. Abrir una terminal de comandos en la carpeta raíz del proyecto.
2. Ejecutar el siguiente comando para iniciar el entorno de Node.js:
   
        node servidor.js

3. La consola indicará que el servidor está en ejecución.
4. Abrir el navegador web e ingresar a: `http://localhost:3000`
5. Para detener el servidor, presionar `Ctrl + C` en la terminal.

### Explicación de cómo funciona

Esta implementación simula un entorno web real. El script `servidor.js` utiliza los módulos nativos de Node.js (`http` y `fs`) para abrir el puerto `3000` en la tarjeta de red virtual (`localhost`). 

Cuando el navegador realiza una petición HTTP GET a la ruta `/`, el servidor de Node intercepta el mensaje, lee el archivo `index.html` del disco duro de forma asíncrona y lo despacha de vuelta a través de la red. Es crucial destacar que el servidor adjunta las cabeceras HTTP (`Content-Type: text/html` y código de estado `200 OK`) para que el navegador interprete correctamente los bytes recibidos y no los trate como texto plano o una descarga binaria.

---

## Implementación 3: Servidor Web con Python

**Archivos necesarios:** `index.html` y `servidor.py`

### Instrucciones de ejecución

1. Asegurarse de tener el intérprete de Python instalado y configurado en las variables de entorno (`PATH`).
2. Abrir una terminal de comandos en la carpeta raíz del proyecto.
3. Ejecutar el siguiente comando:
   
        python servidor.py

4. La consola indicará que el servidor está en ejecución.
5. Abrir el navegador web e ingresar a: `http://localhost:5000`
6. Para detener el servidor, presionar `Ctrl + C` en la terminal.

### Explicación de cómo funciona

A nivel arquitectónico, el navegador (cliente) no distingue en qué lenguaje está escrito el backend, siempre que respete el protocolo HTTP. A diferencia de Node.js donde configuramos el enrutamiento manualmente, este script utiliza el módulo de alto nivel `http.server` de Python. 

La clase `SimpleHTTPRequestHandler` abstrae la complejidad de las cabeceras y el sistema de archivos: automáticamente mapea la petición a la raíz (`/`) buscando un `index.html` en el directorio actual, infiere el Tipo MIME correspondiente de forma dinámica y maneja internamente las respuestas de error (como un `404`), demostrando la eficiencia de las librerías estándar de Python para servir recursos estáticos.

