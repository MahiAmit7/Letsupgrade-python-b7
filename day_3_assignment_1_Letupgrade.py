altitude = input("You want to land the plane so please tell me the altitude in ehich you are in ft : ")
altitude = int(altitude)
if altitude <= 1000:
      print("Yes , you can land the plane please land it carefully")
elif altitude > 1000 and altitude <= 5000:
      print("No , you cannot land the plane . At first came down tpo 1000ft then land the plane")
elif altitude > 5000 :
     print("Go around and try later")

