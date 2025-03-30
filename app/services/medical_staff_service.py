from app.models.medical_staff import MedicalStaff

def create_medical_staff(staff_id, name, role, status, statusText, phone, ambulance_id=None):
    staff = MedicalStaff(
        staff_id=staff_id,
        name=name,
        role=role,
        status=status,
        statusText=statusText,
        phone=phone,
        ambulance_id=ambulance_id
    )
    staff.save()
    return staff

def get_all_medical_staff():
    return MedicalStaff.get_all()

def get_medical_staff_by_id(staff_id):
    return MedicalStaff.get_by_id(staff_id)

def update_medical_staff(staff_id, **kwargs):
    staff = MedicalStaff.get_by_id(staff_id)
    if staff:
        staff.update(**kwargs)
        return staff
    return None

def delete_medical_staff(staff_id):
    staff = MedicalStaff.get_by_id(staff_id)
    if staff:
        staff.delete()
        return True
    return False