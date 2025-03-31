from flask import Flask, jsonify, render_template
import serial
import sys # for parsing args
from unittest.mock import MagicMock # for local development

"""
utilities
"""

def is_dev(args):
    if len(args) > 1 and args[1] == 'local':
        return True
    else:
        return False

################################################################################

"""
serial setup
"""

serial_port = "/dev/ttyACM0"
def create_serial_connection(serial_port):
    # TODO: figure out how to kill
    return serial.Serial(serial_port)

# set up serial connection for dev or prod based on cli args
if is_dev(sys.argv):
    ser = MagicMock()
else:
    ser = create_serial_connection(serial_port)

################################################################################

"""
application
"""

################################################################################

"""
server
"""

app = Flask(__name__)

@app.route('/press_button')
def press_button():
    print('Pressing button...') # WARN: debug
    ser.flush() # NOTE: necessary?
    ser.write(b'press')
    print('Button Pressed') # WARN: debug
    return jsonify({'message': 'button pressed'})

@app.route('/web_cam')
def web_cam():
    return render_template('web_cam.html')


################################################################################

if __name__ == '__main__':
    if is_dev(sys.argv):
        # for localhost
        app.run(debug=True)
    else:
        # for pi
        # TODO: work out host & port
        host = '0.0.0.0'
        port = 80
        app.run(host, port, debug=True)
