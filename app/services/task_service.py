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
    tasks=Task.get_all()
    return [serialize_task(task) for task in tasks]
    


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

def serialize_task(task):
    return {
        'id': task.id,
        'status': task.status,
        'statusText': task.statusText,
        'location': task.location,
        'description': task.description,
        'time': task.time.isoformat() if task.time else None,
        'response_time': task.response_time
    }