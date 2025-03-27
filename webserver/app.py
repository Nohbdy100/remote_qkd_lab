from flask import Flask, jsonify
import serial

# port = "/dev/ttyACM0"
# ser = serial.Serial(port) # TODO: need to figure out how to kill this??

app = Flask(__name__)

@app.route('/press')
def press_button():
    print('Pressing button...') # WARN: debug
    # ser.flush() # NOTE: necessary?
    # ser.write(b'press')
    print('Button Pressed') # WARN: debug
    return jsonify({'message': 'button pressed'})

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 80
    app.run(host, port, debug=True)
