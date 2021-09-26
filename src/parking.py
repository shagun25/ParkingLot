import lot, car

class Parking(object):
    """
    Parking class which has details about parking slots
    as well as operation performed on parking are present here
    """

    def __init__(self):
        self.slots = {}

    def Create_parking_lot(self, no_of_slots):
        """
        This method will create parking lot if not present already with given
        number of slots.
        Input: no_of_slots - Integer Type
        """
        no_of_slots = int(no_of_slots)

        if len(self.slots) > 0:
            print("Parking Lot already created")
            return

        if no_of_slots > 0:
            for i in range(1, no_of_slots+1):
                temp_slot = lot.ParkingSlot(slot_no=i,
                                    available=True)
                self.slots[i] = temp_slot
            print("Created parking of %s slots" % no_of_slots)
        else:
            print("Number of slots is incorrect.")
        return

    def get_nearest_available_slot(self):
        """Method to find nearest available slot in parking
        """
        available_slots = [x for x in list(self.slots.values()) if x.available]
        if not available_slots:
            return None
        return sorted(available_slots, key=lambda x: x.slot_no)[0]

    def Park(self, reg_no, driver_age, age):
        """
        Method to park a coming car in nearest available parking
        slot. If not present it will throw message.
        Input: reg_no - String Type
               age - String Type
        """

        if not self._do_primary_checks():
            return

        available_slot = self.get_nearest_available_slot()
        if available_slot:
            # create car object and save in the available slot
            available_slot.car = car.Car.create(reg_no, age)
            available_slot.available = False
            print("Car with vehicle registration number ",reg_no," has been parked at slot number ",available_slot.slot_no)
        else:
            print("Sorry, parking lot is full.")

    def Leave(self, slot_no):
        """
        Method to empty a parking slot while car is leaving.
        Input: slot_no - Integer Type
        """
        slot_no = int(slot_no)
        if not self._do_primary_checks():
            return

        if slot_no in self.slots:
            pslot = self.slots[slot_no]
            if not pslot.available and pslot.car:
                pslot.car = None
                pslot.available = True
                print("Slot number ",slot_no," is vacated")
                # the car with vehicle registration number",car.reg_no,
                #" left the space, the driver of the car was of age ",car.age)
            else:
                print("No car is present at slot number %s" % slot_no)
        else:
            print("Sorry, slot number does not exist in parking lot.")

    def Status(self):
        """Method to show current status of parking
        """

        if not self._do_primary_checks():
            return

        print("Slot No\tRegistration No\tAge")
        for i in list(self.slots.values()):
            if not i.available and i.car:
                print("%s\t%s\t%s" % (i.slot_no, i.car.reg_no, i.car.age))

    def _do_primary_checks(self):
        if len(self.slots) == 0:
            print("Parking Lot not created")
            return False
        return True

    def Vehicle_registration_number_for_driver_of_age(self, age):
        """
        Method to find registration numbers of car with given age in
        parking
        Input: age - String Type
        """

        if not self._do_primary_checks():
            return

        reg_nos = ''
        for pslot in list(self.slots.values()):
            if not pslot.available and pslot.car and \
                pslot.car.age == age:
                reg_nos += '%s ' % pslot.car.reg_no

        if reg_nos:
            print(reg_nos[:-1])
        else:
            print(" ")

    def Slot_numbers_for_driver_of_age(self, age):
        """
        Method to find slot numbers for cars with given age in
        parking.
        Input: age - String Type
        """

        if not self._do_primary_checks():
            return

        slot_nos = ''
        for pslot in list(self.slots.values()):
            if not pslot.available and pslot.car and \
                pslot.car.age == age:
                slot_nos += '%s ' % pslot.slot_no

        if slot_nos:
            print(slot_nos[:-1])
        else:
            print("Not found")

    def Slot_number_for_car_with_number(self, reg_no):
        """
        Method to find slot numbers in parking with given registration
        number.
        Input: reg_no - String Type
        """

        if not self._do_primary_checks():
            return

        slot_no = ''
        for pslot in list(self.slots.values()):
            if not pslot.available and pslot.car and \
                pslot.car.reg_no == reg_no:
                slot_no = pslot.slot_no
                break

        if slot_no:
            print(slot_no)
        else:
            print("Not found")

