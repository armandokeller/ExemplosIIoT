from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

led_status = False

@app.route('/led', methods=['GET'])
def led_get():
    if request.method == 'GET':
        return f'LED status: {"Ligado" if led_status else "Desligado"}'
    else:
        return 'Método invalido'

@app.route('/led', methods=['PUT'])
def led_put():
    global led_status
    
    status = request.args.get('status')
    if status.strip().lower() == 'on':
        led_status = True
    elif status.strip().lower() == 'off':
        led_status = False
    else:
        return 'Status invalido'
    return "OK"
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

# curl -X PUT -d status=on http://localhost:80/led
