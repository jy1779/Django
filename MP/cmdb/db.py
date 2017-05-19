from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import user,host
# from MP.cmdb.models import user,host
engine = create_engine("mysql+pymysql://root:python@192.168.1.234:33306/MP?charset=utf8")
Session_Class = sessionmaker(bind=engine)
Session = Session_Class()
def select_all():
    user_id = []
    user_owner = []
    user_user = []
    user_password =[]
    user_remarks = []
    data = Session.query(user).filter_by().all()
    for i in range(len(data)):
        user_id.append(data[i].id)
        user_owner.append(data[i].owner)
        user_user.append(data[i].user)
        user_password.append(data[i].password)
        user_remarks.append(data[i].remarks)
    return user_id,user_owner,user_user,user_password,user_remarks

def insert(sumbit_owner,sumbit_user,sumbit_password,sumbit_remarks):
    user_obj = user(owner=sumbit_owner, user=sumbit_user, password=sumbit_password, remarks=sumbit_remarks)
    Session.add(user_obj)
    Session.commit()

def delete(user_id):
    data = Session.query(user).filter_by(id=user_id).first()
    Session.delete(data)
    Session.commit()

def authentication(p_user,p_pwd):
    data = Session.query(user).filter_by(user=p_user).all()
    data_user = data[0].user
    data_pwd = data[0].password
    if p_user == data_user and p_pwd == data_pwd:
        return True
    else:
        return False
def update(upd_id,upd_owner,upd_user,upd_password,upd_remarks):
    data = Session.query(user).filter_by(id=upd_id).all()
    data_owner = data[0].owner
    data_user = data[0].user
    data_password = data[0].password
    data_remarks = data[0].remarks
    if upd_owner != data_owner:
        data[0].owner = upd_owner
    if upd_user != data_user:
        data[0].user = upd_user
    if upd_password != data_password:
        data[0].password = upd_password
    if upd_remarks != data_remarks:
        data[0].remarks = upd_remarks
    Session.commit()