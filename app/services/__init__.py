from .user_service import authenticate_user,update_last_login,get_all_users,post_test,test_user
from .task_service import create_task, delete_task, get_all_tasks, get_task_by_id, update_task
from .task_record_service import create_task_record, delete_task_record, get_all_task_records, get_task_record_by_id, update_task_record
from .medical_staff_service import create_medical_staff, delete_medical_staff, get_all_medical_staff, get_medical_staff_by_id, update_medical_staff
from .medical_equipment_service import create_medical_equipment, delete_medical_equipment, get_all_medical_equipment, get_medical_equipment_by_id, update_medical_equipment
from .ambulance_service import create_ambulance, delete_ambulance, get_all_ambulances, get_ambulance_by_id, update_ambulance

__all__ = ["authenticate_user","update_last_login","get_all_users","post_test","test_user",
           "create_task","delete_task","get_all_tasks","get_task_by_id","update_task",
           "create_task_record","delete_task_record","get_all_task_records","get_task_record_by_id","update_task_record",
           "create_medical_staff","delete_medical_staff","get_all_medical_staff","get_medical_staff_by_id","update_medical_staff",
           "create_medical_equipment","delete_medical_equipment","get_all_medical_equipment","get_medical_equipment_by_id","update_medical_equipment",
           "create_ambulance","delete_ambulance","get_all_ambulances","get_ambulance_by_id","update_ambulance"]