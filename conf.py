from sshconf import read_ssh_config
from os.path import expanduser

def main():
    conf = read_ssh_config(expanduser("~/.ssh/config"))
    hosts = conf.hosts()
    # print (hosts)
    hosts_dict = {}
    for host in hosts:
        # print(host)
        settings = conf.host(host)
        # print(settings)
        settings_filter = [ 'hostname', 'user', 'port' ]
        filtered_settings = {k: settings[k] for k in settings_filter if k in settings}
        # print(filtered_settings)
        hosts_dict[host] = filtered_settings
    
    print(hosts_dict)


if __name__ == "__main__":
    main()