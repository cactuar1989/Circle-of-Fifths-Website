import http.server
import socketserver
import os

PORT = 8000  
DIRECTORY_TO_SERVE = '.' 

# Set up a custom handler to serve the files
Handler = http.server.SimpleHTTPRequestHandler

# Change to the desired directory
os.chdir(DIRECTORY_TO_SERVE)

# Create a server instance
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving directory at port", PORT)
    # Start the server
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
