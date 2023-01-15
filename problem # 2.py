while True:
    service_crew_name = input("Service Crew Name: ")
    hours_worked = float(input("No. of Hours Worked: "))
    ot_hours = float(input("Extra Service Hours (OT): "))
    ut_hours = float(input("No. of Hours Late (UT): "))
    rate_per_hour = float(input("Rate per Hour: "))
    food_deduction = float(input("Food Deduction: "))
    extra_income = float(input("Extra Income (Tip): "))

    ot_rate = rate_per_hour * 0.03
    under_time_pay = ut_hours * rate_per_hour
    over_time_pay = ot_hours * ot_rate
    gross_pay = (hours_worked * rate_per_hour) + over_time_pay
    insurance = gross_pay * 0.03
    sss = gross_pay * 0.05
    tax = gross_pay * 0.1
    deduction = under_time_pay + insurance + tax + sss + food_deduction
    net_pay = gross_pay - deduction + extra_income

    print("Service Crew Name: ", service_crew_name)
    print("Under Time Pay: ", under_time_pay)
    print("Over Time Pay: ", over_time_pay)
    print("Extra Income (Tip): ", extra_income)
    print("Net Pay: ", net_pay)
    repeat = input("Do you want to repeat the transaction? (yes/no)")
    if repeat.lower() == "no":
        break
    elif repeat.lower() == "yes":
        continue
