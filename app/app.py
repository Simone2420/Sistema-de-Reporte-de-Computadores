import reflex as rx
from app.states.computer_state import ComputerState
from app.components.computer_form import computer_form
from app.db import create_db_and_tables
from app.api import router as api_router


def computer_table() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Computer Reports", class_name="text-xl font-semibold mb-4"),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "ID",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Computer Number",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Has Admin Pass",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Admin Password",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Actions",
                            class_name="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                    ),
                    class_name="bg-gray-50",
                ),
                rx.el.tbody(
                    rx.foreach(
                        ComputerState.computers,
                        lambda computer: rx.el.tr(
                            rx.el.td(
                                computer["id"],
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
                            ),
                            rx.el.td(
                                computer["computer_number"],
                                class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900",
                            ),
                            rx.el.td(
                                rx.icon(
                                    tag=rx.cond(
                                        computer["has_admin_password"],
                                        "check_circle",
                                        "x_circle",
                                    ),
                                    class_name=rx.cond(
                                        computer["has_admin_password"],
                                        "text-green-500",
                                        "text-red-500",
                                    ),
                                ),
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
                            ),
                            rx.el.td(
                                rx.cond(
                                    computer["admin_password"] == None,
                                    "N/A",
                                    "********",
                                ),
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
                            ),
                            rx.el.td(
                                rx.el.button(
                                    rx.icon(tag="trash_2", class_name="h-4 w-4"),
                                    on_click=lambda: ComputerState.delete_computer(
                                        computer["id"]
                                    ),
                                    class_name="text-red-600 hover:text-red-900",
                                ),
                                class_name="px-6 py-4 whitespace-nowrap text-right text-sm font-medium",
                            ),
                        ),
                    ),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg",
        ),
        class_name="w-full",
    )


def index() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.h1("Computer Reporting System", class_name="text-3xl font-bold mb-8"),
            computer_form(),
            computer_table(),
            class_name="max-w-4xl mx-auto p-8",
        ),
        class_name="font-['Inter'] bg-gray-100 min-h-screen",
        on_mount=ComputerState.load_computers,
    )


create_db_and_tables()
app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)
app.api = api_router