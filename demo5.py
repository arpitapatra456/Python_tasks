appname = input("Enter the app name: ")
if(appname == "grafana"):
    appportnum = 3000
    print(f"App name is: {appname}")
else:
    print(f"App name is: {appname}")
    print(f"App running port number is {appportnum}.")

print(f'''App name is: {appname}
App running port number is: {appportnum}''')