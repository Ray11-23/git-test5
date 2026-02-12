#!/usr/bin/env python3
"""
Simple HTTP server for serving static HTML files.
Usage: python3 server.py [port]
Default port: 8000
"""

import http.server
import socketserver
import sys
import os

# Default port
PORT = 8000

# Get port from command line argument if provided
if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1])
    except ValueError:
        print(f"Error: Invalid port number '{sys.argv[1]}'")
        print("Usage: python3 server.py [port]")
        sys.exit(1)

# Change to the directory where the script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server avviato con successo!")
        print(f"Server in esecuzione sulla porta {PORT}")
        print(f"Visita: http://localhost:{PORT}")
        print(f"Premi CTRL+C per fermare il server")
        httpd.serve_forever()
except OSError as e:
    if e.errno == 98:  # Address already in use
        print(f"Errore: La porta {PORT} è già in uso.")
        print(f"Prova con un'altra porta: python3 server.py <numero_porta>")
    else:
        print(f"Errore: {e}")
    sys.exit(1)
except KeyboardInterrupt:
    print("\nServer fermato.")
    sys.exit(0)
