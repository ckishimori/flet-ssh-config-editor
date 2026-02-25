import flet as ft
from sshconf import read_ssh_config
from os.path import expanduser

def main(page: ft.Page):
    page.title = "Hello World App"

    conf = read_ssh_config(expanduser("~/.ssh/config"))

    def add_sshconfig_entry(e):
        conf.add(
            host.value,
            HostName=hostname.value,
            User=user.value,
            Port=port.value,
        )
        conf.save()
        host.value = ""
        hostname.value = ""
        user.value = ""
        port.value = ""
        page.update()

    host = ft.TextField(label="host", width=300)
    hostname = ft.TextField(label="hostname", width=300)
    user = ft.TextField(label="user", width=300)
    port = ft.TextField(label="port", width=300)

    page.add(
        ft.Column(controls=[
            host,
            hostname,
            user,
            port,
            ft.ElevatedButton(content="Add",on_click=add_sshconfig_entry)
        ])
    )


if __name__ == "__main__":
    ft.app(target=main)

