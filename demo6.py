
username = input("Enter the username: ")
if username == "root":
    appname = input("Enter the app name: ")
    if appname == "grafana":
        appportnum = 3000
        conffile = "/etc/grafana/grafana.ini"
    else:
        if appname == "prometheus":
            appportnum = 9090
            conffile = "/etc/prometheus/prometheus.yml"
        else:
            if appname == "webauth":
                appportnum = 8080
                conffile = "/etc/webauth/webauth.conf"
            else:
                appportnum = None
                conffile = None
                print("Invalid app name.")

    if appportnum != None:
        print(f"App name is: {appname} port number is {appportnum} {conffile}.")
else:
    print("Access denied. Only root users are allowed.")
          