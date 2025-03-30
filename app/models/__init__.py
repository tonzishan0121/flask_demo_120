from flask_sqlalchemy import SQLAlchemy
from app import app

_db = SQLAlchemy(app)

from .user import User
from .ambulance import Ambulance
from .task import Task
from .task_record import TaskRecord
from .medical_equipment import MedicalEquipment
from .medical_staff import MedicalStaff

__all__ = ['User','Ambulance','Task','TaskRecord','MedicalEquipment','MedicalStaff']