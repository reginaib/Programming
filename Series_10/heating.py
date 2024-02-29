# https://dodona.be/nl/courses/2802/series/29676/activities/1745983456
class Heater:
    """
    >>> machine1 = Heater('radiator kitchen', temperature=20)
    >>> machine2 = Heater('radiator living', minimum=15, temperature=18)
    >>> machine3 = Heater('radiator bathroom', temperature=22, minimum=18, maximum=28)
    >>> print(machine1)
    radiator kitchen: current temperature: 20.0; allowed min: 0.0; allowed max: 100.0
    >>> machine2
    Heater('radiator living', 18.0, 15.0, 100.0)
    >>> machine2.change_temperature(8)
    >>> machine2.temperature()
    26.0
    >>> machine3.change_temperature(-5)
    >>> machine3
    Heater('radiator bathroom', 18.0, 18.0, 28.0)
    """

    def __init__(self, name, temperature=10.0, minimum=0.0, maximum=100.0):
        self.name = name
        self._temperature = float(temperature)
        self.minimum = float(minimum)
        self.maximum = float(maximum)

    def __str__(self):
        return (f'{self.name}: current temperature: {self._temperature:0.1f}; allowed min: {self.minimum:0.1f}; '
                f'allowed max:{self.maximum: 0.1f}')

    def __repr__(self):
        return f"Heater('{self.name}', {self._temperature:0.1f}, {self.minimum:0.1f}, {self.maximum:0.1f})"

    def change_temperature(self, increase):
        self._temperature = min(max(self._temperature + increase, self.minimum), self.maximum)

    def temperature(self):
        return self._temperature


if __name__ == '__main__':
    import doctest
    doctest.testmod()
