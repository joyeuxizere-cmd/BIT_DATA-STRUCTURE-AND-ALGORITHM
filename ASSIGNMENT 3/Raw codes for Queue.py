# 1. At RRA, 7 citizens queue. After 3 served, who is front?
rra_queue=[]
rra_queue.append("Citizen1")
rra_queue.append("Citizen2")
rra_queue.append("Citizen3")
rra_queue.append("Citizen4")
rra_queue.append("Citizen5")
rra_queue.append("Citizen6")
rra_queue.append("Citizen7")
rra_queue.pop(0)
rra_queue.pop(0)
rra_queue.pop(0)   
print("\n")   
print("Front of RRA queue after 3 served:", rra_queue[0])

# 2. At Airtel, 6 customers queue. Who is last served?
queue_airtel = []
queue_airtel.append("Customer1")
queue_airtel.append("Customer2")
queue_airtel.append("Customer3")
queue_airtel.append("Customer4")
queue_airtel.append("Customer5")
queue_airtel.append("Customer6")
print("Last served in Airtel queue:",queue_airtel[-1] )