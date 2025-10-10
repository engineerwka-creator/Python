#Get Numbers of pins

def get_number_of_pin (connector_name):
    if connector_name == "Phoenix":
        return 12
    elif connector_name == "d_sub":
        return 9
    else:
        return 0

