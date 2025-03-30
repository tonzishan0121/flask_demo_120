from app.models.ambulance import Ambulance

def create_ambulance(ambulance_id, license_plate, status, statusText, driver_name, driver_phone):
    ambulance = Ambulance(
        ambulance_id=ambulance_id,
        license_plate=license_plate,
        status=status,
        statusText=statusText,
        driver_name=driver_name,
        driver_phone=driver_phone
    )
    ambulance.save()
    return ambulance

def get_all_ambulances():
    return Ambulance.get_all()

def get_ambulance_by_id(ambulance_id):
    return Ambulance.get_by_id(ambulance_id)

def update_ambulance(ambulance_id, **kwargs):
    ambulance = Ambulance.get_by_id(ambulance_id)
    if ambulance:
        ambulance.update(**kwargs)
        return ambulance
    return None

def delete_ambulance(ambulance_id):
    ambulance = Ambulance.get_by_id(ambulance_id)
    if ambulance:
        ambulance.delete()
        return True
    return False