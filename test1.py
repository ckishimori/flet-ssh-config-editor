import flet as ft

def main(page):

    fruits_list = ["apple", "banana", "orange", "grape", "strawberry", "watermelon", "kiwi", "pineapple", "mango", "pear"]

    async def open_anchor(e):
        await anchor.open_view()

    async def close_anchor(e):
        anchor.value = e.control.data
        await anchor.close_view()
        anchor.update()
        page.focus_scope.unfocus()
        page.update()
        

    def handle_change(e):
        list_to_show = [fruit for fruit in fruits_list if e.data.lower() in fruit]
        lv.controls.clear()
        for i in list_to_show:
            lv.controls.append(ft.ListTile(title=ft.Text(f"{i}"), on_click=close_anchor, data=i))
        anchor.update()

    async def handle_submit(e):
        await close_anchor(e)
        
    
    def done_button_click(e):
        pass

    lv = ft.ListView()
    list_to_show = fruits_list
    lv.controls.clear()
    for i in list_to_show:
        lv.controls.append(ft.ListTile(title=ft.Text(f"{i}"), on_click=close_anchor, data=i))    

    anchor = ft.SearchBar(
    view_elevation=4,
    divider_color=ft.Colors.BLUE,
    bar_hint_text="Search for fruits...",
    view_hint_text="Suggestions...",
    on_change=handle_change,
    on_focus=open_anchor,
    on_tap=open_anchor,
    on_submit=handle_submit,
    controls=[
        lv
    ],
    )

    fruit = ft.TextField(label="Fruit", width=300)

    page.add(
        ft.Column(controls=[
            ft.Row([
                anchor
            ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            fruit,
            ft.ElevatedButton(content="Done",on_click=done_button_click)
        ])
    )

ft.app(main)