from .user_service import *
from .task_service import *
from .task_record_service import *
from .medical_staff_service import *
from .medical_equipment_service import *
from .ambulance_service import *
            #user部分方法&login方法
__all__ = ['authenticate_user','update_last_login','get_all_users','post_test','test_user',
           #/task部分方法
           'create_task','delete_task','get_all_tasks','get_task_by_id','update_task','get_task_count_change_percentage','get_today_task_count',
           #/task_record部分方法
           'create_task_record','delete_task_record','get_all_task_records','get_task_record_by_id','update_task_record','get_today_task_count','get_today_avg_response_time',
           #/medical_staff部分方法
           'create_medical_staff','delete_medical_staff','get_all_medical_staff','get_medical_staff_by_id','update_medical_staff',
           #/medical_equipment部分方法
           'create_medical_equipment','delete_medical_equipment','get_all_medical_equipment','get_medical_equipment_by_id','update_medical_equipment',
           #/ambulance部分方法
           'create_ambulance','delete_ambulance','get_all_ambulances','get_ambulance_by_id','update_ambulance','get_idle_ambulance_percentag','get_idle_ambulance_count']