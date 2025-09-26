import reflex as rx
import sqlmodel
from ..models import Computer
from ..db import engine


class ComputerState(rx.State):
    computers: list[Computer] = []
    computer_number: str = ""
    has_admin_password: bool = False
    admin_password: str = ""

    @rx.event
    def load_computers(self):
        with sqlmodel.Session(engine) as session:
            self.computers = session.exec(
                sqlmodel.select(Computer).order_by(Computer.id)
            ).all()

    @rx.event
    def add_computer(self):
        if not self.computer_number:
            return rx.toast.error("Computer number cannot be empty.")
        with sqlmodel.Session(engine) as session:
            existing = session.exec(
                sqlmodel.select(Computer).where(
                    Computer.computer_number == self.computer_number
                )
            ).first()
            if existing:
                return rx.toast.error(
                    f"Computer with number {self.computer_number} already exists."
                )
            new_computer = Computer(
                computer_number=self.computer_number,
                has_admin_password=self.has_admin_password,
                admin_password=self.admin_password if self.has_admin_password else None,
            )
            session.add(new_computer)
            session.commit()
        self.computer_number = ""
        self.has_admin_password = False
        self.admin_password = ""
        return ComputerState.load_computers