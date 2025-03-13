from http.server import BaseHTTPRequestHandler, HTTPServer
import serial

"""
Simple/Example/Test web server for remotely pressing buttons
"""

port = "/dev/ttyACM0"
ser = serial.Serial(port) # TODO: need to figure out how to kill this??

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/press':
            self.trigger_button_press()
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'BUTTON PRESSED\n')
        elif self.path == '/test':
            print('remote connection test')
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'REMOTE CONNECTION TEST\n')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Invalid URI\n')

    def trigger_button_press(self):
        print('Pressing button...')
        ser.flush()
        ser.write(b'press')
        print('Button Pressed')

def run_server():
    server_address = ('', 9090)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server running on port 9090...')
    httpd.serve_forever()

run_server()
