from http.server import BaseHTTPRequestHandler, HTTPServer
from collections import deque
from urllib.parse import urlparse
from signal import signal, SIGPIPE, SIG_DFL # might only be necessary for curl testing
import serial # pip install pyserial

"""
Simple/Example/Test web server for remotely pressing buttons
"""

class Machine:
    def __init__(self, machine_id) -> None:
        com_num = 'COM1'
        self.machine_id = machine_id
        self.assigned_user = None
        self.port = com_num
        self.baudrate = 9600

    def press_button(self):
        print('Pressing button...')
        with serial.Serial(self.port, self.baudrate) as ser:
            ser.write(b'press')
        print('Button Pressed')

    def repress_button(self):
        print('Repressing button...')
        with serial.Serial(self.port, self.baudrate) as ser:
            ser.write(b'repress')
        print('Button Repressed')

class User:
    def __init__(self, user_id) -> None:
        self.user_id = user_id
        self.assigned_machine = None

class MachineManager:
    def __init__(self) -> None:
        self.available_machines = deque([Machine(f'lab_{i}') for i in range(5)])
        self.inuse_machines = deque()
        self.users = {}

    def assign_user_to_machine(self, user_id):
        if self.available_machines:
            machine = self.available_machines.popleft()
            machine.assigned_user = user_id
            self.inuse_machines.append(machine)
            self.users[user_id] = machine
            return machine
        else:
            return None

    def release_machine(self, user_id):
        machine = self.users.get(user_id)
        if machine:
            self.inuse_machines.remove(machine)
            machine.assigned_user = None
            self.available_machines.append(machine)
            del self.users[user_id]
            return True
        else:
            return False

    def get_machine_for_user(self, user_id):
        return self.users.get(user_id)

class RequestHandler(BaseHTTPRequestHandler):
    machine_manager = MachineManager()

    def do_GET(self):
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.split('/')
        user_id, action = None, None

        # NOTE: this try catch is for curl closing the connection ( i think that's what is happening )
        try:
            if len(path_parts) == 3:
                user_id = path_parts[1]
                action = path_parts[2]

                self.wfile.write(f'{user_id}\n'.encode('utf-8')) # debug
                self.wfile.write(f'{action}\n'.encode('utf-8')) # debug
                if action == 'press':
                    self.trigger_button_press(user_id)
                elif action == 'repress':
                    self.trigger_button_press(user_id)
                else:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(b'Invalid Action - BAD ARGS\n')
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Invalid Action - LEN ARGS\n')
        except:

            # NOTE: this code runs every time, it can probably go unless we want to serve something back?
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'GENERIC OUTPUT MESSAGE\n')

    def trigger_button_press(self, user_id):
        machine = self.machine_manager.get_machine_for_user(user_id)
        if machine is None:
            machine = self.machine_manager.assign_user_to_machine(user_id)
            if machine:
                print(f'assigned user {user_id} to machine {machine.machine_id}')
            else:
                print(f'no machines avaiable for {user_id}')
                return
        print(f'pressing button on machine {machine.machine_id} for user {user_id}')
        machine.press_button()

    def trigger_button_repress(self, user_id):
        machine = self.machine_manager.get_machine_for_user(user_id)
        if machine is None:
            machine = self.machine_manager.assign_user_to_machine(user_id)
            if machine:
                print(f'assigned user {user_id} to machine {machine.machine_id}')
            else:
                print(f'no machines avaiable for {user_id}')
                return
        print(f'repressing button on machine {machine.machine_id} for user {user_id}')
        machine.repress_button()

def run_server():
    signal(SIGPIPE, SIG_DFL) # might only be necessary for curl testing
    server_address = ('', 9090)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server running on port 9090...')
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
