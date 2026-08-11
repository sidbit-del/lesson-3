name=input("Enter your name:")
gadget=input("Enter you favorite gadget:")
agent_number=12
speed_rating=2.5
mission_count=50
height=169.5
active_status=True


print("name:",name," type:",type(name))
print("favorite gadget:",gadget,"type:",type(gadget))
print("agent number:",agent_number,"type:",type(agent_number))
print("speed rating:",speed_rating,"type:",type(speed_rating))
print("mission count:",mission_count,"type:",type(mission_count))
print("height:",height,"type:",type(height))
print("active status:",active_status,"type:",type(active_status))


agent_number=str(agent_number)
speed_rating=str(speed_rating)
mission_count=str(mission_count)
height=str(height)
active_status=str(active_status)


print("agent number:",agent_number,"type:",type(agent_number))
print("speed rating:",speed_rating,"type:",type(speed_rating))
print("mission count:",mission_count,"type:",type(mission_count))
print("height:",height,"type:",type(height))
print("active status:",active_status,"type:",type(active_status))

name=name[0:3]
print(name)
last=name[-1]
print(last)
code=name+last
print(code)

print(gadget[::-1])