# 120急救大数据平台（后端）  :hospital:

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


## 技术栈
- **后端框架**: Flask 2.0+
- **数据库**: MySQL 8.0+
- **ORM**: SQLAlchemy
- **认证**: JWT
- **API文档**: Swagger UI
- **测试框架**: pytest

## 功能模块
### 核心功能
- 🚑 救护车状态实时监控
- 🏥 医疗设备资源管理
- 👨⚕️ 医护人员调度管理
- 🚨 急救任务全流程跟踪
- 📊 大数据可视化看板

### 管理功能
1. **救护车管理**
   - 实时状态更新（在线/任务中/离线）
   - 车牌号绑定管理
   - 司机信息维护

2. **医疗设备管理** 
   - 设备状态监控（可用/使用中/需维护）
   - 设备-救护车绑定管理
   - 设备使用记录追踪

3. **医护人员管理**
   - 人员状态管理（当班/待命/休息）
   - 技能标签管理
   - 急救任务分配

## 项目结构
```bash
flask_demo_120/
├── app/                      # 应用核心
│   ├── models/               # 数据模型
│   │   ├── ambulance.py      # 救护车模型
│   │   ├── medical_staff.py  # 医护人员模型
│   │   └── medical_equipment.py # 医疗设备模型
│   ├── routes/               # API路由
│   │   ├── ambulance_routes.py 
│   │   └── medical_*_routes.py
│   ├── services/             # 业务逻辑
│   └── __init__.py           # 应用初始化
├── requirements.txt          # 依赖列表
├── run.py                    # 启动脚本
└── admin.html                # 管理端界面
```

## API文档
访问 `/swagger` 查看完整API文档，包含：
- 救护车状态查询接口
- 医疗设备管理接口
- 急救任务创建/更新接口
- 实时数据统计接口

## 快速部署
```bash
# 创建虚拟环境
python -m venv .venv
.\.venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
set FLASK_APP=run.py
set FLASK_ENV=development

# 初始化数据库
flask db init
flask db migrate
flask db upgrade

# 启动服务
flask run --port 5000
```

## 贡献指南
欢迎通过 Issue 提交改进建议或通过 Pull Request 贡献代码

## 许可证
本项目采用 [MIT License](LICENSE)