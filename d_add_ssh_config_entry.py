import flet as ft
from sshconf import read_ssh_config
from os.path import expanduser

class SshConfigEditor(ft.Column):
    def __init__(self):
        super().__init__()
        # Initialize state
        self.conf = read_ssh_config(expanduser("~/.ssh/config"))

        # Create controls
        self.host = ft.TextField(label="Host", width=300)
        self.hostname = ft.TextField(label="HostName", width=300)
        self.user = ft.TextField(label="User", width=300)
        self.port = ft.TextField(label="Port", width=300)

        # Define declarative layout
        self.controls = [
            self.host,
            self.hostname,
            self.user,
            self.port,
            ft.ElevatedButton(content="Add", on_click=self.add_sshconfig_entry)
        ]

    def add_sshconfig_entry(self, e):
        self.conf.add(
            self.host.value,
            HostName=self.hostname.value,
            User=self.user.value,
            Port=self.port.value,
        )
        self.conf.save()
        
        # Reset fields and update UI
        for control in [self.host, self.hostname, self.user, self.port]:
            control.value = ""
        self.update()

def main(page: ft.Page):
    page.title = "SSH Config Editor (Declarative)"
    page.add(SshConfigEditor())

if __name__ == "__main__":
    ft.app(target=main)