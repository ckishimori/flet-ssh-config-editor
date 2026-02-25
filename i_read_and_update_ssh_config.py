import flet as ft
from sshconf import read_ssh_config
from os.path import expanduser

def main(page: ft.Page):
    page.title = "Search & Populate Form"
    
    # 1. Read Config and Prepare Data
    conf = read_ssh_config(expanduser("~/.ssh/config"))
    hosts = conf.hosts()
    # print (hosts)
    data = {}
    default_settings = {"hostname" : "", "user" : "", "port" : "" }
    for host in hosts:
        # print(host)
        settings = conf.host(host)
        # print(settings)
        settings_filter = [ 'hostname', 'user', 'port' ]
        filtered_settings = {k: settings[k] for k in settings_filter if k in settings}
        # print(filtered_settings)
        data[host] = default_settings.copy()
        # print (data[host])
        data[host].update(filtered_settings)
    
    # print(data)

    # 2. Form Fields
    detail_host = ft.TextField(label="Host", read_only=True)
    detail_hostname = ft.TextField(label="HostName", read_only=True)
    detail_user = ft.TextField(label="User", read_only=True)
    detail_port = ft.TextField(label="Port", read_only=True)

    # 3. Handle selection: Populates Form
    async def on_item_selected(e):
        search_bar.value = e.control.data
        selected_key = e.control.data
        selected_data = data[selected_key]
        print(selected_key, selected_data)
        detail_host.value = selected_key
        detail_hostname.value = selected_data["hostname"]
        detail_user.value = selected_data["user"]
        detail_port.value = selected_data["port"]
        await close_anchor(selected_key)
        page.update()


    # 4. SearchBar and Filtering
    def on_change(e):
        search_query = e.control.value.lower()
        results = [
            ft.ListTile(
                title=ft.Text(key),
                data=key,
                on_click=on_item_selected
            )
            for key in data.keys()
            if search_query in key.lower()
        ]
        search_bar.controls = results
        search_bar.update()

    async def open_anchor(e):
        await search_bar.open_view()

    async def close_anchor(e):
        await search_bar.close_view()

    search_bar = ft.SearchBar(
        bar_hint_text="Search items...",
        on_change=on_change,
#        on_focus=open_anchor       # do not do this
        on_tap=open_anchor,
        controls=[] # Populated dynamically
    )

    page.add(
        search_bar,
        ft.Column([
            ft.Text("SSH config details:", size=20, weight="bold"),
            detail_host,
            detail_hostname,
            detail_user,
            detail_port
        ])
    )

ft.app(target=main)