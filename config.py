import os

class Config:
    SECRET_KEY = "D58EhG&U@kHJo6!ZhELXe4^*ouJyzvq&shsn8z*kaiU%HrLAPEZu2h5%CD8^CF%bLjYRcC$4aJD#8L9VWPpM5Kt8LQgD#x!VpdVQs2nnATQcVRPxV6aTd6*eEEXcTt$V"
#                os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///synergysphere.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
