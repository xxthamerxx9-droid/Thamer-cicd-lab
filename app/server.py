import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
APP_VERSION = os.getenv("APP_VERSION", "1.0")
def get_version():
return APP_VERSION
def get_status():
return 200
class PulseHandler(BaseHTTPRequestHandler):
def do_GET(self):
if self.path == "/health":
status, body, mime = get_status(), "healthy", "text/plain"
elif self.path == "/version":
status, body, mime = 200, get_version(), "text/plain"
elif self.path == "/":
status, mime = 200, "text/html"
body = ("<html><head><meta name='viewport' content='width=device-width,initial-scale=1'>"
"<style>body{background:#172f51;color:white;font-family:Arial;text-align:center;padding:8vh}"
"article{background:#245078;border-radius:22px;padding:4rem;max-width:650px;margin:auto}"
"strong{color:#42e4cb;font-size:44px}</style></head><body><article>"
"<h1>PULSE DASHBOARD</h1><p>Automated CI/CD & GitOps lab</p>"
f"<strong>Version {get_version()}</strong><p>Healthy</p></article></body></html>")
else:
status, body, mime = 404, "not found", "text/plain"
payload = body.encode("utf-8")
self.send_response(status)
self.send_header("Content-Type", mime + "; charset=utf-8")
self.send_header("Content-Length", str(len(payload)))
self.end_headers()
self.wfile.write(payload)
if __name__ == "__main__":
ThreadingHTTPServer(("0.0.0.0", 8000), PulseHandler).serve_forever()
