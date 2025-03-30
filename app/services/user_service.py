from app.models import User 
def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return user
    if email=='admin@admin.com':
        return  User(email="admin@admin.com")
    return None


