from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import models, schemas


def create(db: Session, sandwich: schemas.SandwichCreate) -> models.Sandwich:
    # Create a new instance of the Sandwich model with the provided data
    db_sandwich = models.Sandwich(
        item=sandwich.sandwich_name,
        price=sandwich.price
    )
    # Add the newly created Sandwich object to the database session
    db.add(db_sandwich)
    # Commit the changes to the database
    db.commit()
    # Refresh the Sandwich object to ensure it reflects the current state in the database
    db.refresh(db_sandwich)
    # Return the newly created Sandwich object
    return db_sandwich


def update(db: Session, id: int, sandwich: schemas.SandwichUpdate) -> models.Sandwich:
    # Query the database for the specific sandwich to update
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == id).first()
    if db_sandwich is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")

    # Extract the update data from the provided 'sandwich' object
    update_data = sandwich.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    for key, value in update_data.items():
        setattr(db_sandwich, key, value)

    # Commit the changes to the database
    db.commit()
    # Return the updated sandwich record
    return db_sandwich