import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # 确保这个密钥是安全的，并且在应用重启后不会改变
    