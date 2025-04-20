from .login_routes import login_routes
from .task_routes import task_routes
from .user_routes import user_routes
from .ambulance_routes import ambulance_routes
from .task_record_routes import task_record_routes
from .medical_staff_routes import medical_staff_routes
from .medical_equipment_routes import medical_equipment_routes

__all__ = [
    'login_routes','task_routes','user_routes','ambulance_routes','task_record_routes','medical_staff_routes','medical_equipment_routes'
]