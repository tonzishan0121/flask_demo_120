from app.models import User 
from werkzeug.security import generate_password_hash, check_password_hash

def get_all_users():
    users=User.get_all()
    return [serialize_user(user) for user in users]

def post_test(pwd):
    users=User.get_all()
    return [serialize_user(user,pwd) for user in users]

def test_user(pwd):
    user_pid=User.set_password(User(),pwd)
    return user_pid

#验证用户密码
def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return user
    return None

#更新最后登录时间
def update_last_login(email):
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return {"status": "error", "message": "用户不存在"}
    
    # 调用模型方法判断
    if user.update_last_login():
        return {"status": "success", "message": "登录时间已更新"}
    else:
        print(user.up)
        return {"status": "expired", "message": "登录状态已过期"}

#测试阶段方法
def serialize_user(user,*args):
    user_password =user.password_hash
    is_right=check_password_hash(user_password,args)
    try:
        return {
            'email': user.email,
            'nickname': user.nickname,
            'password_hash': user.password_hash,
            'role': user.role,
            'created_at': user.created_at,
            'last_login': user.last_login,
            'is_right': is_right
        }
    except:
        return None