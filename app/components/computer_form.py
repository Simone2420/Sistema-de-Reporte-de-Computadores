import reflex as rx
from ..states.computer_state import ComputerState


def computer_form() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Add New Computer Report", class_name="text-xl font-semibold mb-4"),
        rx.el.form(
            rx.el.div(
                rx.el.label(
                    "Computer Number",
                    class_name="block text-sm font-medium text-gray-700",
                ),
                rx.el.input(
                    name="computer_number",
                    placeholder="e.g., PC-12345",
                    class_name="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.input(
                        type="checkbox",
                        name="has_admin_password",
                        class_name="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600",
                    ),
                    rx.el.label(
                        "Has Admin Password?",
                        class_name="ml-2 block text-sm text-gray-900",
                    ),
                    class_name="flex items-center",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Admin Password",
                    class_name="block text-sm font-medium text-gray-700",
                ),
                rx.el.input(
                    name="admin_password",
                    type="password",
                    placeholder="Enter admin password",
                    class_name="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm",
                ),
                class_name="mb-4",
            ),
            rx.el.button(
                "Add Report",
                type="submit",
                class_name="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2",
            ),
            on_submit=ComputerState.add_computer,
            reset_on_submit=True,
        ),
        class_name="p-6 bg-white rounded-lg shadow-md mb-8",
    )