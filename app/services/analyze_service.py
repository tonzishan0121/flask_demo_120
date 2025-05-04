import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from datetime import datetime, timedelta
import io
import seaborn as sns

matplotlib.use('Agg')
# 模拟数据
tasks = [
    {'id': 'T011', 'status': 'completed', 'time': '2025-04-18 08:45:00', 'location': '浦东新区'},
    {'id': 'T012', 'status': 'completed', 'time': '2025-04-18 09:00:00', 'location': '徐汇区'},
    {'id': 'T013', 'status': 'completed', 'time': '2025-04-18 07:30:00', 'location': '静安区'},
    {'id': 'T014', 'status': 'completed', 'time': '2025-04-18 20:00:00', 'location': '杨浦区'},
    {'id': 'T015', 'status': 'completed', 'time': '2025-04-18 11:15:00', 'location': '闵行区'},
    {'id': 'T016', 'status': 'completed', 'time': '2025-04-18 06:45:00', 'location': '虹口区'},
    {'id': 'T021', 'status': 'completed', 'time': '2025-04-18 20:45:00', 'location': '浦东新区'},
    {'id': 'T022', 'status': 'completed', 'time': '2025-04-18 01:00:00', 'location': '徐汇区'},
    {'id': 'T023', 'status': 'processing', 'time': '2025-04-18 01:30:00', 'location': '静安区'},
    {'id': 'T024', 'status': 'pending', 'time': '2025-04-18 01:45:00', 'location': '杨浦区'},
    {'id': 'T017', 'status': 'completed', 'time': '2025-04-18 22:30:00', 'location': '普陀区'},
    {'id': 'T018', 'status': 'completed', 'time': '2025-04-18 13:00:00', 'location': '长宁区'},
    {'id': 'T018', 'status': 'completed', 'time': '2025-04-18 14:15:00', 'location': '宝山区'},
    {'id': 'T020', 'status': 'completed', 'time': '2025-04-18 15:30:00', 'location': '嘉定区'},
    {'id': 'T025', 'status': 'processing', 'time': '2025-04-18 02:00:00', 'location': '金山区'},
    {'id': 'T026', 'status': 'processing', 'time': '2025-04-18 22:30:00', 'location': '松江区'},
    {'id': 'T027', 'status': 'processing', 'time': '2025-04-18 03:00:00', 'location': '青浦区'},
    {'id': 'T028', 'status': 'processing', 'time': '2025-04-18 23:30:00', 'location': '奉贤区'},
    {'id': 'T029', 'status': 'pending', 'time': '2025-04-18 04:20:00', 'location': '崇明区'},
    {'id': 'T030', 'status': 'pending', 'time': '2025-04-18 04:30:00', 'location': '浦东新区'},
    {'id': 'T031', 'status': 'pending', 'time': '2025-04-18 05:00:00', 'location': '徐汇区'},
    {'id': 'T032', 'status': 'completed', 'time': '2025-04-18 05:30:00', 'location': '静安区'},
    {'id': 'T033', 'status': 'completed', 'time': '2025-04-18 16:00:00', 'location': '杨浦区'},
    {'id': 'T034', 'status': 'completed', 'time': '2025-04-18 16:30:00', 'location': '闵行区'},
    {'id': 'T035', 'status': 'completed', 'time': '2025-04-18 17:00:00', 'location': '虹口区'},
    {'id': 'T036', 'status': 'processing', 'time': '2025-04-18 07:30:00', 'location': '普陀区'},
    {'id': 'T037', 'status': 'processing', 'time': '2025-04-18 08:00:00', 'location': '长宁区'},
    {'id': 'T038', 'status': 'processing', 'time': '2025-04-18 18:30:00', 'location': '宝山区'},
    {'id': 'T039', 'status': 'processing', 'time': '2025-04-18 09:00:00', 'location': '嘉定区'},
    {'id': 'T040', 'status': 'pending', 'time': '2025-04-18 09:30:00', 'location': '金山区'}
]

def get_task_trend():
    plt.figure(figsize=(12, 6))
    sns.set_style(style="whitegrid")
    
    # 时间范围
    start_time = datetime(2025, 4, 18)
    end_time = datetime(2025, 4, 19, 0, 0)  
    start = start_time.timestamp()
    end = end_time.timestamp()
    
    # 提取时间戳并过滤范围外数据
    task_times = [
        datetime.strptime(task['time'], '%Y-%m-%d %H:%M:%S').timestamp()
        for task in tasks
        if start <= datetime.strptime(task['time'], '%Y-%m-%d %H:%M:%S').timestamp() <= end
    ]
    
    # 生成标签
    hours = [start_time + timedelta(hours=i) for i in range(26)]  
    hour_labels = [dt.strftime('%m-%d %H:00') for dt in hours]
    
    bins = int((end - start) / 3600)  # 总秒数转小时数
    task_counts, _ = np.histogram(task_times, bins=bins, range=(start, end))
    
    # 绘制折线图
    plt.plot(hour_labels[:bins], task_counts, color='skyblue')  # 对齐标签与分桶
    plt.xlabel('时间', fontsize=12, fontfamily='Microsoft YaHei')
    plt.ylabel('任务数量', fontsize=12, fontfamily='Microsoft YaHei')
    plt.title('任务时间分布趋势', fontsize=14, fontfamily='Microsoft YaHei')
    plt.xticks(rotation=45)
    
    img = io.BytesIO()
    plt.tight_layout()
    plt.savefig(img, format='png', dpi=100)
    plt.close()
    img.seek(0)
    
    return img

def get_region_distribution():
    plt.figure(figsize=(12, 6))
    sns.set_style(style="whitegrid")
    
    regions = [task['location'] for task in tasks]
    unique_regions, counts = np.unique(regions, return_counts=True)
    plt.bar(unique_regions, counts, color='lightgreen')
    plt.xlabel('区域', fontsize=12, fontfamily='Microsoft YaHei')
    plt.xticks(rotation=45, fontproperties='Microsoft YaHei', fontsize=12)
    plt.ylabel('任务数量', fontsize=12, fontfamily='Microsoft YaHei')
    plt.title('区域任务分布', fontsize=14, fontfamily='Microsoft YaHei')
    plt.xticks(rotation=45)
    
    img = io.BytesIO()
    plt.tight_layout()
    plt.savefig(img, format='png', dpi=100)
    plt.close()
    img.seek(0)
    
    return img
