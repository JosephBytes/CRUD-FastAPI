from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, order_detail):
    # Create a new instance of the order_details model with the provided data
    db_order_details = models.OrderDetail(
        order_id=order_detail.order_id,
        sandwich_id=order_detail.sandwich_id,
        amount=order_detail.amount
    )
    # Add the newly created order_details object to the database session
    db.add(db_order_details)
    # Commit the changes to the database
    db.commit()
    # Refresh the order_details object to ensure it reflects the current state in the database
    db.refresh(db_order_details)
    # Return the newly created Order object
    return db_order_details

