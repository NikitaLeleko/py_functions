def validate_pin(pin: str):
    if pin[0] == "-":
        pin = pin[1::]
    if pin.isdigit() and pin !="-" and  len(pin) == 4 or len(pin) == 6:
        return True
    else:
        return False
