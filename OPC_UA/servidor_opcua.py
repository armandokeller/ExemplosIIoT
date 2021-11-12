# Código adaptado de https://github.com/FreeOpcUa
from opcua import ua, Server
import sys
import time
import datetime
sys.path.insert(0, "..")

if __name__ == "__main__":

    server = Server()
    server.set_endpoint("opc.tcp://127.0.0.1:4840")
    
    uri = "Unisinos_IIOT"
    idx = server.register_namespace(uri)
    
    objects = server.get_objects_node()
    

    myobj = objects.add_object(idx, "LED")
    status = myobj.add_variable(idx, "status", 0)
    myDataDatetime = myobj.add_variable(idx, "timestamp", 0)
    status.set_writable()   
    myDataDatetime.set_writable()
 
    server.start()
    try:
        count = 0
        while True:
            time.sleep(2)
            status_led = status.get_value()
            myDataDatetime.set_value(datetime.datetime.now())
            if(status_led == 0):
                print('Led apagado')
            else:
                print('Led acionado')
            #status.set_value(count)
    finally:
        server.stop()