
global test_topic = "/topic/test";

global some_test_event: event(c_id: conn_id);

event python_results(c_id: conn_id)
{
	print(cat("Got Python Results: ", c_id));
}

event connection_state_remove(c: connection)
{
    Broker::publish(test_topic, some_test_event, c$id);
}

event zeek_init()
{
	Broker::peer(addr_to_uri(127.0.0.1), 60000/tcp);
	Broker::subscribe(test_topic);
}
