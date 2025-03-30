from . import login
from .tasks import task_routes

login_route=login
task_route=task_routes

__all__ = [
    'login_route','task_route'
]