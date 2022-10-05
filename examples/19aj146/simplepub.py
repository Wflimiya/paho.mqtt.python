import paho.mqtt.publish as publish

publish.single("トピック名", "メッセージ内容", hostname="ホスト名")