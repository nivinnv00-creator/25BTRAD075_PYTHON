# Name: Nivin N V\n# USN: 25BTRAD075\n\nimport flet as ft
import flet as ft
from datetime import date

# Student records are stored using a dictionary and lists.
# Example: {"Nivin": [{"date": "2026-11-15", "status": "Present"}]}
students = {}


def main(page: ft.Page):
    page.title = "Attendance Tracker"
    page.window_width = 900
    page.window_height = 700
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    title = ft.Text("CLASS ATTENDANCE TRACKER", size=24, weight=ft.FontWeight.BOLD)

    name_input = ft.TextField(
        label="Student name",
        hint_text="Enter student name",
        expand=True,
    )

    student_dropdown = ft.Dropdown(
        label="Select student",
        options=[],
        expand=True,
    )

    date_input = ft.TextField(
        label="Attendance date (YYYY-MM-DD)",
        value=str(date.today()),
        expand=True,
    )

    status_dropdown = ft.Dropdown(
        label="Attendance status",
        value="Present",
        options=[
            ft.dropdown.Option("Present"),
            ft.dropdown.Option("Absent"),
        ],
        expand=True,
    )

    threshold_input = ft.TextField(
        label="Minimum attendance (%)",
        value="75",
        width=190,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    message = ft.Text()

    attendance_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Student")),
            ft.DataColumn(ft.Text("Present")),
            ft.DataColumn(ft.Text("Sessions")),
            ft.DataColumn(ft.Text("Attendance %")),
            ft.DataColumn(ft.Text("Status")),
        ],
        rows=[],
        column_spacing=25,
    )

    def get_percentage(records):
        if not records:
            return 0
        present = sum(1 for record in records if record["status"] == "Present")
        return present / len(records) * 100

    def refresh():
        student_dropdown.options = [
            ft.dropdown.Option(name) for name in students
        ]

        if student_dropdown.value not in students:
            student_dropdown.value = None

        try:
            threshold = float(threshold_input.value)
        except (ValueError, TypeError):
            threshold = 75

        rows = []
        for name, records in students.items():
            present = sum(1 for r in records if r["status"] == "Present")
            total = len(records)
            percentage = get_percentage(records)

            if total == 0:
                result = "No records"
            elif percentage < threshold:
                result = "Below threshold"
            else:
                result = "Satisfactory"

            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(name)),
                        ft.DataCell(ft.Text(str(present))),
                        ft.DataCell(ft.Text(str(total))),
                        ft.DataCell(ft.Text(f"{percentage:.1f}%")),
                        ft.DataCell(ft.Text(result)),
                    ]
                )
            )

        attendance_table.rows = rows
        page.update()

    def add_student(e):
        name = name_input.value.strip()
        if not name:
            message.value = "Please enter a student name."
        elif name in students:
            message.value = "This student already exists."
        else:
            students[name] = []
            name_input.value = ""
            message.value = f"{name} added successfully."
        refresh()

    def save_attendance(e):
        name = student_dropdown.value
        record_date = date_input.value.strip()
        status = status_dropdown.value

        if not name:
            message.value = "Please select a student."
            page.update()
            return

        try:
            date.fromisoformat(record_date)
        except ValueError:
            message.value = "Enter the date in YYYY-MM-DD format."
            page.update()
            return

        records = students[name]

        # Update the record if this date already exists.
        for record in records:
            if record["date"] == record_date:
                record["status"] = status
                message.value = f"Attendance updated for {name}."
                refresh()
                return

        records.append({"date": record_date, "status": status})
        message.value = f"Attendance saved for {name}."
        refresh()

    def show_details(e):
        name = student_dropdown.value
        if not name:
            message.value = "Please select a student."
        elif not students[name]:
            message.value = f"No attendance records for {name}."
        else:
            details = "\n".join(
                f'{r["date"]}: {r["status"]}' for r in students[name]
            )
            message.value = f"{name}'s attendance:\n{details}"
        page.update()

    def update_threshold(e):
        refresh()
        message.value = "Attendance threshold updated."
        page.update()

    page.add(
        title,
        ft.Text("Add student", size=17, weight=ft.FontWeight.BOLD),
        ft.Row(
            [
                name_input,
                ft.Button("Add Student", on_click=add_student),
            ]
        ),
        ft.Divider(),
        ft.Text("Record attendance", size=17, weight=ft.FontWeight.BOLD),
        ft.Row([student_dropdown, date_input]),
        ft.Row(
            [
                status_dropdown,
                ft.Button("Save / Update Attendance", on_click=save_attendance),
                ft.Button("View Records", on_click=show_details),
            ]
        ),
        ft.Divider(),
        ft.Text("Attendance summary", size=17, weight=ft.FontWeight.BOLD),
        ft.Row(
            [
                threshold_input,
                ft.Button("Apply Threshold", on_click=update_threshold),
            ]
        ),
        attendance_table,
        message,
    )

    refresh()


ft.run(main)
