import paho.mqtt.client as mqtt
import time


class Thing(mqtt.Client):
    def __init__(self, cname, **kwargs):
        super(Thing, self).__init__(cname, **kwargs)

    def on_connect(self, mqttc, obj, flags, rc):
        print("Connected with result code " + str(rc))

    def on_message(self, mqttc, obj, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

    def on_publish(self, mqttc, obj, mid):
        print("mid: " + str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    def run(self):
        self.connect('broker', 8883, 60)
        rc = 0
        while rc == 0:
            payload = '{"timestamp": "' + str(time.time()) + '", "property": true}'
            self.publish('thing/', payload=payload, qos=2)
            rc = self.loop()
            time.sleep(5)
        return rc


if __name__ == '__main__':
    r = Thing("thing")
    r.run()

