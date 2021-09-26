from src import parking
import unittest
class TestParkingLot(unittest.TestCase):

	def test_Create_parking_lot(self):
		parkingLot  = parking.Parking()
		res = object.Create_parking_lot(6)
		self.assertEqual(6,res)

	def test_Park(self):
		parkingLot  = parking.Parking()
		res = parkingLot.Create_parking_lot(6)
		res = parkingLot.Park("KA-01-HH-1234",21)
		self.assertNotEqual(-1,res)

	def test_Leave(self):
		parkingLot  = parking.Parking()
		res = parkingLot.Create_parking_lot(6)
		res = parkingLot.Park("KA-01-HH-1234",21)
		res = parkingLot.Leave(1)
		self.assertEqual(True,res)

	def test_Vehicle_registration_number_for_driver_of_age(self):
		parkingLot  = parking.Parking()
		res = parkingLot.Create_parking_lot(6)
		res = parkingLot.Park("KA-01-HH-1234",21)
		res = parkingLot.Park("PB-01-HH-1234",21)
		regnos = parkingLot.Vehicle_registration_number_for_driver_of_age(21)
		self.assertIn("KA-01-HH-1234",regnos)
		self.assertIn("PB-01-HH-1234",regnos)

	def test_Slot_number_for_car_with_number(self):
		parkingLot  = parking.Parking()
		res = parkingLot.Create_parking_lot(6)
		res = parkingLot.Park("KA-01-HH-1234",21)
		res = parkingLot.Park("PB-01-HH-1234",21)
		slotno = parkingLot.Slot_number_for_car_with_number("PB-01-HH-1234")
		self.assertEqual(2,slotno)

	def test_Slot_numbers_for_driver_of_age(self):
		parkingLot  = parking.Parking()
		res = parkingLot.Create_parking_lot(6)
		res = parkingLot.Park("KA-01-HH-1234",21)
		res = parkingLot.Park("PB-01-HH-1234",21)
		slotnos = parkingLot.Slot_numbers_for_driver_of_age(21)
		self.assertIn("1",slotnos)
		self.assertIn("2",slotnos)

if __name__ == '__main__':
	unittest.main()
