const http = require('http');
const crypto = require('crypto');
const fs = require('fs');
const path = require('path');

const PORT = 3000;

// Almacenamiento en memoria: { sessionId: [alumnos] }
const store = {};

function generarId() {
  return crypto.randomUUID();
}

function parseCookies(cookieHeader = '') {
  const cookies = {};
  cookieHeader.split(';').forEach(part => {
    const [key, ...vals] = part.trim().split('=');
    if (key) cookies[key.trim()] = decodeURIComponent(vals.join('=').trim());
  });
  return cookies;
}

function parseBody(req) {
  return new Promise((resolve, reject) => {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try { resolve(JSON.parse(body || '{}')); }
      catch { reject(new Error('JSON inválido')); }
    });
    req.on('error', reject);
  });
}

function send(res, status, data, headers = {}) {
  const body = typeof data === 'string' ? data : JSON.stringify(data);
  const contentType = typeof data === 'string' ? 'text/html; charset=utf-8' : 'application/json';
  res.writeHead(status, { 'Content-Type': contentType, ...headers });
  res.end(body);
}

const server = http.createServer(async (req, res) => {
  const cookies = parseCookies(req.headers.cookie);
  let sessionId = cookies['session_id'];
  const isNewSession = !sessionId || !store[sessionId];

  if (isNewSession) {
    sessionId = generarId();
    store[sessionId] = [];
  }

  const setCookieHeader = isNewSession
    ? { 'Set-Cookie': `session_id=${sessionId}; Path=/; HttpOnly; SameSite=Lax` }
    : {};

  const url = req.url.split('?')[0];
  const method = req.method;

  // ── GET / → servir HTML ──────────────────────────────────────────────────
  if (url === '/' && method === 'GET') {
    const htmlPath = path.join(__dirname, 'public', 'index.html');
    fs.readFile(htmlPath, 'utf8', (err, html) => {
      if (err) return send(res, 500, 'Error al leer el archivo HTML.');
      send(res, 200, html, setCookieHeader);
    });
    return;
  }

  // ── GET /api/alumnos → devolver lista del cliente ────────────────────────
  if (url === '/api/alumnos' && method === 'GET') {
    send(res, 200, store[sessionId], setCookieHeader);
    return;
  }

  // ── POST /api/alumnos → agregar alumno ───────────────────────────────────
  if (url === '/api/alumnos' && method === 'POST') {
    let body;
    try { body = await parseBody(req); }
    catch { return send(res, 400, { error: 'Body inválido' }); }

    const { nombre, edad, nota } = body;

    if (
      typeof nombre !== 'string' || !nombre.trim() ||
      typeof edad !== 'number' || edad < 1 ||
      typeof nota !== 'number' || nota < 0 || nota > 10
    ) {
      return send(res, 400, { error: 'Datos inválidos' }, setCookieHeader);
    }

    const alumno = { id: generarId(), nombre: nombre.trim(), edad, nota };
    store[sessionId].push(alumno);
    send(res, 201, alumno, setCookieHeader);
    return;
  }

  // ── DELETE /api/alumnos/:id → eliminar alumno ────────────────────────────
  const deleteMatch = url.match(/^\/api\/alumnos\/([^/]+)$/);
  if (deleteMatch && method === 'DELETE') {
    const id = deleteMatch[1];
    const antes = store[sessionId].length;
    store[sessionId] = store[sessionId].filter(a => a.id !== id);
    const eliminado = store[sessionId].length < antes;
    send(res, eliminado ? 200 : 404, { ok: eliminado }, setCookieHeader);
    return;
  }

  send(res, 404, 'No encontrado.');
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`Servidor corriendo en http://0.0.0.0:${PORT}`);
  console.log('Accesible desde cualquier IP en la red local.');
});
