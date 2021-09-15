def result(days_for_conversion, unit_for_conversion):
    if unit_for_conversion == "hours":
        return f"{days_for_conversion} days in hours are {days_for_conversion * 24}."
    elif unit_for_conversion == "minutes":
        return f"{days_for_conversion} days in minutes are {days_for_conversion * 24 * 60}."
    else:
        return "What kinda unit is that?"


def input_validation(days_and_unit_dict):
    try:
        user_input_number = int(days_and_unit_dict["days"])
        if user_input_number > 0:
            result_with_input = result(user_input_number, days_and_unit_dict["unit"])
            print(result_with_input)
        elif user_input_number == 0:
            print("Why would you need conversion for 0 days anyways?")
        else:
            print("Negative days? Am I blind or are you dumb?")
    except ValueError:
        print("Not a valid input! Stop fooling around!")


user_input_message = "Hey, put down the days and the unit (hours or minutes) you wanna convert to, separate them with " \
                     "colon.\n"
