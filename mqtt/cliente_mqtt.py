import paho.mqtt.client as mqtt

status_led = False

def on_connect(client, userdata, flags, rc):
    print("Conectado com código "+str(rc))
    
    # Realizar as inscrições nos tópicos aqui
    client.subscribe("/unisinos/iiot/led/status")


def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload}")
    if msg.topic == "/unisinos/iiot/led/status":
        global status_led
        if str(msg.payload.decode()) == "on":
            status_led = True
        elif str(msg.payload.decode()) == "off":
            status_led = False
    
    print(f"Status do LED: {'ligado' if status_led else 'desligado'}")


if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("mqtt.eclipseprojects.io", 1883, 60)
    client.loop_forever()
