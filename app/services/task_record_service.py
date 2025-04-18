from app.models import TaskRecord

def create_task_record(task_id, ambulance_id, equipment_id, doctor_id, start_time, end_time, duration, task_status, task_statusText):
    record = TaskRecord(
        task_id=task_id,
        ambulance_id=ambulance_id,
        equipment_id=equipment_id,
        doctor_id=doctor_id,
        start_time=start_time,
        end_time=end_time,
        duration=duration,
        task_status=task_status,
        task_statusText=task_statusText
    )
    record.save()
    return record

def get_all_task_records():
    return TaskRecord.get_all()

def get_task_record_by_id(record_id):
    return TaskRecord.get_by_id(record_id)

def update_task_record(record_id, **kwargs):
    record = TaskRecord.get_by_id(record_id)
    if record:
        record.update(**kwargs)
        return record
    return None

def get_today_avg_response_time():
    return TaskRecord.get_today_avg_response_time()

def get_yesterday_avg_response_time():
    return TaskRecord.get_yesterday_avg_response_time()

def get_response_time_change_percentage():
    today_avg = get_today_avg_response_time()
    yesterday_avg = get_yesterday_avg_response_time()
    if yesterday_avg == 0:
        return 0 if today_avg == 0 else float('inf')
    change = ((today_avg - yesterday_avg) / yesterday_avg) * 100
    return round(change, 2)