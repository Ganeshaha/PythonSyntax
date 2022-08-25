def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # YOUR CODE HERE
    if unit_in == 'f' and unit_out == 'c':
      return (temp-32)/ 1.8
    elif unit_in == 'c' and unit_out == 'f':
      return (temp*1.8) +32
    else:
      return f"{unit_in} or {unit_out} is invalid"

print("c", "f", 0, convert_temp("c", "f", 0), "\nshould be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "\nshould be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "\nshould be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "\nshould be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "\nshould be 75.5")

