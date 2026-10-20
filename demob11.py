app_details = []
app_details.append(['flask' , 'version is 2.34' , 5000])
app_details.append(['fastAPI' , 'version is 4.2' , 8000])
app_details.append(['streamlit' , 'version is 4.1' , 9000])
app_details.append(['django' , 'version is 3.2' , 7000])
print(app_details)
app_details[2][2] = 5002
print(app_details)  
app_details.append(['pyramid' , 'version is 2.0' , 6000])
print(app_details)

app_details[1].append('fastAPI.conf');
print(app_details)