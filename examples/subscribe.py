#Subscribing to Upstream Traffic
import context
import paho.mqtt.subscribe as subscribe

m = subscribe.simple(topics=['#'],
                     hostname="eu1.cloud.thethings.network",
                     port=1883,
                     auth={'username':"19aj146@ttn",'password':"NNSXS.733YNHPYC4QMWMX6QZNGPETXW7ANSGVFKSLVZGY.Y6ZVI52YCZJF4RDHKRWYX5NR3TV3KU5BSGFTBEWFPKSTYJ4BNMLQ"},
                     msg_count=2)

for a in m:
    print(a.topic)
    print(a.payload)