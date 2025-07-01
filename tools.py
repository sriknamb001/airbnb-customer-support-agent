def get_wifi_password(data): return f"The Wi-Fi password is {data['wifi_pass']}."
def get_check_in_time(data): return f"Check-in time is {data['check_in_time']}."
def get_local_recs(data): return "Local recommendations: " + ", ".join(data['local_recs'])
