class convertation(object):

    def __init__(self):
        fahrenheit = 0
        celsius = 0
        kelvin = 0

    def convertFromFahrenheitToCelsius(self, fahrenheit):
        self.celsius = float((self.fahrenheit - 32) * (5 / 9))
        return self.celsius

    def convertFromFahrenheitToKelvin(self, fahrenheit):
        self.kelvin = float((self.fahrenheit - 32) * 5 / 9 + 273.15)
        return self.kelvin

    def convertFromCelsiusToFahrenheit(self, celsius):
        self.fahrenheit = float((self.celsius * (9 / 5)) + 32)
        return self.fahrenheit

    def convertFromCelsiusToKelvin(self, celsius):
        self.kelvin = float((self.celsius + 273.15))
        return self.kelvin

    def convertFromKelvinToFahrenheit(self, kelvin):
        self.fahrenheit = float((self.kelvin - 273.15) * 9 / 5 + 32)
        return self.fahrenheit

    def convertFromKelvinToCelsius(self, kelvin):
        self.celsius = float((self.kelvin - 273.15))
        return self.celsius


class Element(object):
    freezing_point = 0
    melting_point = 0
    evaporation_point = 0

    def agg_state(self, t):

        if t <= self.freezing_point:
            return 'Температура замерзания {} °С или {} °K или {} °F '.format(self.celsius, self.kelvin, self.fahrenheit)
        elif t > self.evaporation_point:
            return 'Температура испарения {} °С или {} °K или {} °F '.format(self.celsius, self.kelvin, self.fahrenheit)
        else:
            return 'Температура твердого состояния {} °С или {} °K или {} °F '.format(self.celsius, self.kelvin, self.fahrenheit)


class Oxygen(Element):
    freezing_point = -218
    melting_point = -218
    evaporation_point = -182


oxygen = Oxygen()

print(oxygen.agg_state(int(input('Введите температуру - '))))
