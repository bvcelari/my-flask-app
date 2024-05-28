from flask import Flask

import socket
 
# Function to display hostname and
# IP address
 
 
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return f'Hostname :  {host_name} \n IP : {host_ip}'
    except:
        return "Unable to get Hostname and IP"
 
 
app = Flask(__name__)

@app.route('/')
def hello():
    info = get_Host_name_IP()
    return f"Hello World! from latest {info}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
