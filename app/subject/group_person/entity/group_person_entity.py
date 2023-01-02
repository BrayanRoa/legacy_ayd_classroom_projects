from app.db import db
from sqlalchemy.orm import mapper
from app.subject.group_person.model.group_person_dto import GroupPersonDTO
class GroupPersonEntity(db.Model):
    __tablename__='group_person'
    
    id=db.Column(db.Integer, primary_key=True)
    cancelled = db.Column(db.Boolean, default=False)
    
    institutional_mail = db.Column(db.String(100), db.ForeignKey('person.institutional_mail'))
    person = db.relationship('PersonEntity', back_populates="group_person")

    group_id = db.Column(db.Integer, db.ForeignKey('group.code'))
    group = db.relationship('GroupEntity', back_populates="group_person")
    
    
    def start_mapper():
        mapper(GroupPersonDTO, GroupPersonEntity)