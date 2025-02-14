class LengthConverter:
    def __init__(self):
        self.__meter = 0

    @property
    def meter(self):
        return self.__meter

    @meter.setter
    def meter(self, value):
        self.__meter = value

    @property
    def feet(self):
        return self.__meter * 3.28084

    @feet.setter
    def feet(self, value):
        self.__meter = value / 3.28084

    @property
    def inch(self):
        return self.__meter * 39.37008

    @inch.setter
    def inch(self, value):
        self.__meter = value / 39.37008