from app.models.task import Task

def create_task(id, status, statusText, location, description, time, response_time=None):
    task = Task(
        id=id,
        status=status,
        statusText=statusText,
        location=location,
        description=description,
        time=time,
        response_time=response_time
    )
    task.save()
    return task

def get_all_tasks():
    return Task.get_all()

def get_task_by_id(task_id):
    return Task.get_by_id(task_id)

def update_task(task_id, **kwargs):
    task = Task.get_by_id(task_id)
    if task:
        task.update(**kwargs)
        return task
    return None

def delete_task(task_id):
    task = Task.get_by_id(task_id)
    if task:
        task.delete()
        return True
    return False