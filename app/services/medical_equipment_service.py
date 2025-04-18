from app.models import MedicalEquipment

def create_medical_equipment(equipment_id, name, status, statusText, ambulance_id):
    equipment = MedicalEquipment(
        equipment_id=equipment_id,
        name=name,
        status=status,
        statusText=statusText,
        ambulance_id=ambulance_id
    )
    equipment.save()
    return equipment

def get_all_medical_equipment():
    return MedicalEquipment.get_all()

def get_medical_equipment_by_id(equipment_id):
    return MedicalEquipment.get_by_id(equipment_id)

def update_medical_equipment(equipment_id, **kwargs):
    equipment = MedicalEquipment.get_by_id(equipment_id)
    if equipment:
        equipment.update(**kwargs)
        return equipment
    return None

def delete_medical_equipment(equipment_id):
    equipment = MedicalEquipment.get_by_id(equipment_id)
    if equipment:
        equipment.delete()
        return True
    return False

