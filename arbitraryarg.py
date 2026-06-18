# 1. Positional Arbitrary Arguments (*args)
# When you place an asterisk * before a parameter name, Python creates an empty Tuple with that name and packs any extra positional arguments it receives into that tuple.
# 2. Keyword Arbitrary Arguments (kwargs)
# When you place two asterisks  before a parameter name, Python creates an empty Dictionary with that name and packs any extra key-value arguments it receives into that dictionary.
# def log_session_summary(day_name,*completed_exercises):
#     print(f"Summary for {day_name}")
#     for exercise in completed_exercises:
#         print(f"-{exercise}")
# log_session_summary("Monday","Squats","Leg Press", "Calf Raises")
# log_session_summary("Wednesday","Bench Press","Incline Flyes")
def log_session_summary(day_name,**completed_exercises):
    day={'Day':day_name}
    print(f"Summary for {day['Day']}")
    for key, value in completed_exercises.items():
        day[key]=value
        print(f"-Exercise : {key} Sets : {value}")
log_session_summary("Monday",Squats=3,Leg_Press=4, Calf_Raises=3)
log_session_summary("Wednesday",Bench_Press=4,Incline_Flyes=4)