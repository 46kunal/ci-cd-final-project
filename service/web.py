"""Minimal HTTP application for OpenShift deployment."""

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    """Respond to readiness and demo requests."""

    def do_GET(self):
        """Send a small JSON response."""
        body = json.dumps({"status": "ok", "project": "cicd-final-project"})
        content = body.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    print("Starting server on port", port, flush=True)
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
