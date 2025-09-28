# controllers/massage_controller.py
from database import SessionLocal
from models.massage_model import Massage


def get_all_massages():
    db = SessionLocal()
    massages = db.query(Massage).all()
    db.close()
    return massages


def create_massage(session: str, therapist: str, schedule: str):
    db = SessionLocal()
    massage = Massage(session=session, therapist=therapist, schedule=schedule)
    db.add(massage)
    db.commit()
    db.refresh(massage)
    db.close()
    return massage


def update_massage(
    massage_id: int, session: str = None, therapist: str = None, schedule: str = None
):
    db = SessionLocal()
    massage = db.query(Massage).filter(Massage.id == massage_id).first()
    if session:
        massage.session = session
    if therapist:
        massage.therapist = therapist
    if schedule:
        massage.schedule = schedule
    db.commit()
    db.refresh(massage)
    db.close()
    return massage


def delete_massage(massage_id: int):
    db = SessionLocal()
    massage = db.query(Massage).filter(Massage.id == massage_id).first()
    if massage:
        db.delete(massage)
        db.commit()
    db.close()
    return massage
