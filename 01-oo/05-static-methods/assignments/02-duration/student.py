class Duration:
    def __init__(self, seconds):
        self.__seconds = seconds

    @staticmethod
    def from_seconds(amount):
        return Duration(amount)

    @staticmethod
    def from_minutes(amount):
        return Duration(amount * 60)

    @staticmethod
    def from_hours(amount):
        return Duration(amount * 3600)

    @property
    def seconds(self):
        return self.__seconds

    @property
    def minutes(self):
        return self.__seconds // 60

    @property
    def hours(self):
        return self.__seconds // 3600