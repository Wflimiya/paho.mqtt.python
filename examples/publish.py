import context
import paho.mqtt.publish as publish

topic = u"v3/19aj146@ttn/devices/eui-70b3d559e01d2493/down/push"
payload = u'{"downlinks":[{"f_port": 10,"frm_payload":"hello world","priority": "NORMAL"}]}'


publish.single(topic, 
               payload, 
               hostname="eu1.cloud.thethings.network",
               port=1883,
               auth={'username':"19aj146@ttn",'password':"NNSXS.733YNHPYC4QMWMX6QZNGPETXW7ANSGVFKSLVZGY.Y6ZVI52YCZJF4RDHKRWYX5NR3TV3KU5BSGFTBEWFPKSTYJ4BNMLQ"})