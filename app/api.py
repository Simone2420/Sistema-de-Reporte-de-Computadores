from fastapi import APIRouter, HTTPException
import sqlmodel
from pydantic import BaseModel
from app.db import engine
from app.models import Computer as ComputerModel


class ComputerCreate(BaseModel):
    computer_number: str
    has_admin_password: bool
    admin_password: str | None = None


router = APIRouter()


@router.get("/api/computers", response_model=list[ComputerModel])
def _get_computers():
    with sqlmodel.Session(engine) as session:
        computers = session.exec(
            sqlmodel.select(ComputerModel).order_by(ComputerModel.id)
        ).all()
        return computers


@router.post("/api/computers", response_model=ComputerModel)
def _create_computer(computer: ComputerCreate):
    with sqlmodel.Session(engine) as session:
        existing = session.exec(
            sqlmodel.select(ComputerModel).where(
                ComputerModel.computer_number == computer.computer_number
            )
        ).first()
        if existing:
            raise HTTPException(
                status_code=400,
                detail=f"Computer with number {computer.computer_number} already exists.",
            )
        db_computer = ComputerModel.model_validate(computer)
        session.add(db_computer)
        session.commit()
        session.refresh(db_computer)
        return db_computer


@router.delete("/api/computers/{computer_id}")
def _delete_computer(computer_id: int):
    with sqlmodel.Session(engine) as session:
        computer = session.get(ComputerModel, computer_id)
        if not computer:
            raise HTTPException(status_code=404, detail="Computer not found")
        session.delete(computer)
        session.commit()
        return {"ok": True}