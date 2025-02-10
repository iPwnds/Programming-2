class Time:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        if not 0 <= hours <= 23:
            raise ValueError("Hours must be between 0 and 23")
        if not 0 <= minutes <= 59:
            raise ValueError("Minutes must be between 0 and 59")
        if not 0 <= seconds <= 59:
            raise ValueError("Seconds must be between 0 and 59")

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        if not 0 <= value <= 23:
            raise ValueError("Hours must be between 0 and 23")
        self.__hours = value

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        if not 0 <= value <= 59:
            raise ValueError("Minutes must be between 0 and 59")
        self.__minutes = value

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value):
        if not 0 <= value <= 59:
            raise ValueError("Seconds must be between 0 and 59")
        self.__seconds = value