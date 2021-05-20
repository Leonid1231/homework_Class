class Hotel():
	def __init__(self,name,place,rooms_mid,mid_room_price,rooms_lux,lux_room_price):
		self.name = name 
		self.place = place 
		self.rooms_mid = {}
		self.rooms_mid = rooms_mid
		self.mid_room_price = mid_room_price
		self.rooms_lux = {}
		self.rooms_lux = rooms_lux
		self.lux_room_price = lux_room_price

	def presentation(self):
		print("Hello, we have two types of rooms - middle , which costs 20000 and luxe , which costs 50000")

	def booking(self):
		a = input("if you want to book the mid_room enter the room number (room_1/room_2/room_3/room_4) "\
				  "if you want to book the lux_room enter the room number (room1_lux/room2_lux/room3_lux \n")
		if a == 'room_1' and self.rooms_mid['1_room'] == 'free':
			print("you have successfully booked room_1")
		elif a == 'room_2' and self.rooms_mid['2_room'] == 'free':
			print("you have successfully booked room_2")
		elif a == 'room_3' and self.rooms_mid['3_room'] == 'free':
			print("you have successfully booked room_3")
		elif a == 'room_4' and self.rooms_mid['4_room'] == 'free':
			print("you have successfully booked room_4")
		elif a == 'room1_lux' and self.rooms_lux['room1'] == 'free':
			print("you have successfully booked room1_lux")
		elif a == 'room2_lux' and self.rooms_lux['room2'] == 'free':
			print("you have successfully booked room2_lux")	
		elif a == 'room3_lux' and self.rooms_lux['room3'] == 'free':
			print("you have successfully booked room3_lux")
		else:
			print("this room has already booked")
		
	def aviable_room_check(self):
		pass	

class Taxy():
	def __init__(self,name_,car_types,price_for_tour):
		self.name = name_
		self.car_types = car_types
		self.price_for_tour = price_for_tour

	def presentation_(self):
		print("We have very comfortable cars with good prices ")
	def discount(self):
		print("if you buy 2 tickets, you will get 20%  discount so the price will be ", 40000 - (40000 * 20) // 100)

class Tour(Hotel,Taxy):
	def __init__(self,name,place,rooms_mid,mid_room_price,rooms_lux,lux_room_price,name_,car_types,price_for_tour):
		
		Hotel.__init__(self,name,place,rooms_mid,mid_room_price,rooms_lux,lux_room_price)
		Taxy.__init__(self,name_,car_types,price_for_tour)

	def present_(self):
		amount =  self.lux_room_price + self.price_for_tour
		amount_2 = self.mid_room_price + self.price_for_tour
		print(f"Hello we offer Hiking tour, we have two options, for lux it will cost {amount}",\
              "which includes transport with ride_over company which provides BMW cars and price for middle will cost",\
              f"{amount_2} , we will stay at Hilton")




x = Tour('Hilton','Yerevan',{'1_room' : 'bussy', '2_room': 'free', '3_room': 'bussy', '4_room': "free"},\
		  20000 , {'room1' : 'free', 'room2' : 'free' , 'room3' : 'bussy'}, 40000,'Taxyy','BMW',20000)

print(x.presentation())
print(x.presentation_())
print(x.discount())
print(x.present_())
print(x.booking())