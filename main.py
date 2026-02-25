import flet as ft

class CounterApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.text_number = ft.Text(value=str(self.counter), size=40)

        # Declarative UI structure
        self.controls = [
            ft.Row(
                controls=[
                    ft.IconButton(ft.Icons.REMOVE, on_click=self.decrement),
                    self.text_number,
                    ft.IconButton(ft.Icons.ADD, on_click=self.increment),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ]
        # Center the column contents
        self.alignment = ft.MainAxisAlignment.CENTER

    def increment(self, e):
        self.counter += 1
        self.text_number.value = str(self.counter)
        self.text_number.update()

    def decrement(self, e):
        self.counter -= 1
        self.text_number.value = str(self.counter)
        self.text_number.update()

def main(page: ft.Page):
    page.title = "Declarative Flet Boilerplate"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(CounterApp())

if __name__ == "__main__":
    ft.app(target=main)