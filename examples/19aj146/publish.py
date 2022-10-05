#Publishing Downlink Messages
import context
import paho.mqtt.publish as publish

publish.single("v3/19aj146/端末A/eui-70b3d559e01d2493/down/push", 
               '{"downlinks":[{"f_port": 10,"frm_payload":"vu8=","priority": "NORMAL"}]}',
               hostname="eu1.cloud.thethings.network",
               port=1883, 
               auth={'username':"19aj146@ttn",
                     'password':"NNSXS.733YNHPYC4QMWMX6QZNGPETXW7ANSGVFKSLVZGY.Y6ZVI52YCZJF4RDHKRWYX5NR3TV3KU5BSGFTBEWFPKSTYJ4BNMLQ"})

#For scheduling downlink messages, the values from to are allowed. f_port1233
#ダウンリンク メッセージをスケジュールする場合、from から to の値が許可されます。f_port1233
#mosquitto_pub -h <server_hostname> -p <port> -t 'base-topic/push-subtopic' -m '{"end_device_ids":{"device_id":"dev1","application_ids":{"application_id":"app1"}},"downlinks":[{"f_port":1,"frm_payload":"AA==","priority":"NORMAL"}]}'