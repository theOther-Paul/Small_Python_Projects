from dataclasses import dataclass
import tkinter as tk

"""
Future development map: 
- GUI to be added using Tkinter
- refactor the code base when i'll find an optimal solution
"""


@dataclass
class Scale:
    name: str
    k_zero: float
    k_degree: float


class ScaleConverter:
    def __init__(self):
        self.scales = {'K': Scale('Kelvin', 0.0, 1.0), 'C': Scale('Celsius', 273.15, 1.0),
                       'F': Scale('Fahrenheit', 459.67, 1.8), 'R': Scale('Reaumur', 273.15, 0.8)}

    def convert(self, temp, from_scale, to_scale):
        if from_scale == to_scale:
            return temp
        if from_scale == 'K' or to_scale == 'K':
            delta = self.scales[from_scale].k_zero - self.scales[to_scale].k_zero
            temp_coefficient = self.scales[to_scale].k_degree / self.scales[from_scale].k_degree
            # print(temp, temp_coefficient, delta)
            if temp_coefficient > 1:
                result = round(temp * temp_coefficient + delta, 2)
            elif temp_coefficient < 1:
                result = round((temp + delta) * temp_coefficient, 2)
            else:
                result = round(temp + delta, 2)
            return result
        else:
            return self.convert(self.convert(temp, from_scale, 'K'), 'K', to_scale)


def testing_ground():
    pass
    # this will be the testing environment, before implementing the code into the main function. 
    # I think a test class might be more suitable for this task


def main():
    var = tk.ACTIVE
    to_be_converted = ScaleConverter()
    test_temp = float(input("Enter a temperature to be converted:"))
    print(to_be_converted.convert(test_temp, 'C', 'K'))


if __name__ == "__main__":
    main()
