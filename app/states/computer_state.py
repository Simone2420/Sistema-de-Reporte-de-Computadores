import reflex as rx
import logging
from ..models import ComputerFrontendDict


class ComputerState(rx.State):
    computers: list[ComputerFrontendDict] = []

    async def _handle_api_error(self, response):
        if not response.ok:
            try:
                body = await response.json()
                message = body.get("detail", "An unknown API error occurred.")
            except Exception as e:
                logging.exception(f"Error: {e}")
                message = f"API Error: {response.status_code} {await response.text()}"
            return rx.toast.error(message)

    @rx.event
    async def load_computers(self):
        response = await self.get_api("/api/computers").get()
        if not response.ok:
            return await self._handle_api_error(response)
        self.computers = await response.json()

    @rx.event
    async def add_computer(self, form_data: dict):
        computer_number = form_data.get("computer_number")
        if not computer_number:
            return rx.toast.error("Computer number cannot be empty.")
        has_admin_pass = form_data.get("has_admin_password") == "on"
        admin_password = form_data.get("admin_password")
        computer_data = {
            "computer_number": computer_number,
            "has_admin_password": has_admin_pass,
            "admin_password": admin_password if has_admin_pass else None,
        }
        response = await self.get_api("/api/computers").post(json=computer_data)
        if not response.ok:
            return await self._handle_api_error(response)
        return ComputerState.load_computers

    @rx.event
    async def delete_computer(self, computer_id: int):
        response = await self.get_api(f"/api/computers/{computer_id}").delete()
        if not response.ok:
            return await self._handle_api_error(response)
        return ComputerState.load_computers