#Delivery Management system-Multiple/hybrid inheritance+method overriding+polymorphism
class Delivery:
    def __init__(self,order_id,destination):
        self.order_id=order_id
        self.destination=destination
    def deliver(self):
        print(f"Order {self.order_id} is being delivered.")
class Trackable:
    def track(self):
        print(f"Tracking order ... ")
class StandardDelivery(Delivery):
    def deliver(self):
        print(f"Order {self.order_id} will arrive in 3-5 days.")
class ExpressDelivery(Delivery,Trackable):
    def deliver(self):
        print(f"Order {self.order_id} will arrive within 24 hours.")
    def track(self):
        print(f"Tracking order {self.order_id}...")
standard=StandardDelivery("D101","Bangkok")
express=ExpressDelivery("D102","ChiangRai")
deliveries=[standard,express]
for delivery in deliveries:
    delivery.deliver()
express.track()