# =====================================================
# ALL PARKING SLOTS
# =====================================================

all_slots = [
    "A1", "A2", "A3",
    "B1", "B2", "B3",
    "C1", "C2"
]

# =====================================================
# AVAILABLE SLOTS
# =====================================================

available_slots = all_slots.copy()

# =====================================================
# HASH MAP
# Vehicle -> Slot
# =====================================================

parked_vehicles = {}


# =====================================================
# GREEDY SLOT ALLOCATION
# =====================================================

def allocate_slot():

    if available_slots:
        return available_slots.pop(0)

    return None


# =====================================================
# PARK VEHICLE
# =====================================================

def park_vehicle(vehicle_number):

    if vehicle_number in parked_vehicles:
        return "ALREADY_PARKED"

    slot = allocate_slot()

    if slot:

        parked_vehicles[vehicle_number] = slot

        return slot

    return None


# =====================================================
# REMOVE VEHICLE
# =====================================================

def remove_vehicle(vehicle_number):

    if vehicle_number in parked_vehicles:

        slot = parked_vehicles.pop(vehicle_number)

        available_slots.append(slot)

        available_slots.sort()

        return slot

    return None


# =====================================================
# SEARCH VEHICLE
# =====================================================

def search_vehicle(vehicle_number):

    return parked_vehicles.get(vehicle_number)