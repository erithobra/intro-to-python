temp_dict = {
  "starting_temp":0,
  "temp_unit": "",
  "cel": 0,
  "fah": 0,
  "kel": 0
}

def start_game():
  temp_dict["starting_temp"] = input("What is the Starting temp? Or (q) to quit")

  while temp_dict["starting_temp"] != "q":
    temp_dict["starting_temp"] = int(temp_dict["starting_temp"])
    temp_dict["temp_unit"] = input("What is the unit? (f, C, K)")
    convert_temp(temp_dict["starting_temp"], temp_dict["temp_unit"])
    start_game()

def convert_temp(start, unit):
  if unit == "f":
    temp_dict["cel"] = round((temp_dict["fah"]) - 32 / 1.8)
    temp_dict["kel"] = round((temp_dict["fah"] + 459.67) / 1.8)
    print(f"fahrenheit: {temp_dict['fah']} \nto Celsius: {temp_dict['cel']} \nto Kelvin: {temp_dict['kel']}")
  elif unit == "C":
    temp_dict["fah"] = round(temp_dict["cel"] * 1.8 + 32)
    temp_dict["kel"] = round(temp_dict["cel"]  + 273.15)
    print(f"Celsius: {temp_dict['cel']} \nto fahrenheit: {temp_dict['fah']} \nto Kelvin: {temp_dict['kel']}")
  else:
    temp_dict["fah"] = round(temp_dict["kel"] * 1.8 - 459.67)
    temp_dict["cel"] = round(temp_dict["kel"] - 273.15)
    print(f"Kelvin: {temp_dict['kel']} \nto Celsius: {temp_dict['cel']} \nto fahrenheit: {temp_dict['fah']}")

start_game()
