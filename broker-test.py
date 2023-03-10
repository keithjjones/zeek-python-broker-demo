import sys
import broker

# Setup endpoint and connect to Zeek.
with broker.Endpoint() as ep, \
     ep.make_subscriber("/topic/test") as sub:

    ep.listen("127.0.0.1", 60000)

    while True:
        (t, d) = sub.get()
        pong = broker.zeek.Event(d)
        print("received {}  --   {}".format(pong.name(), pong.args()))

        python_results = broker.zeek.Event("python_results", pong.args()[0]);
        ep.publish("/topic/test", python_results);