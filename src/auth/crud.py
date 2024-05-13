from sqlalchemy.orm import Session

from . import model


def get_permission(db: Session):
    return db.query(model.Permission).all()
