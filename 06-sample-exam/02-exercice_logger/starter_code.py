class Run:
    def __init__(self, date, distance, duration, elevation):
        if not self.is_valid_date(date):
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        self.date = date # date in YYYY-MM-DD format
        self.distance = distance # distance in km
        self.duration = duration # duration in minutes
        self.elevation = elevation # elevation in percentage

    @property
    def calories_factor(self):
        return 10 * (1 + self.elevation / 100)

    @property
    def calories(self):
        return int((self.distance/(self.duration/60))*self.distance * self.calories_factor)

    def is_valid_date(self, date_str):
        if len(date_str) != 10:
            return False
        if date_str[0]<'0' or date_str[0]>'9':
            return False
        if date_str[1]<'0' or date_str[1]>'9':
            return False
        if date_str[2]<'0' or date_str[2]>'9':
            return False
        if date_str[3]<'0' or date_str[3]>'9':
            return False
        if date_str[4] != '-':
            return False
        if date_str[5]<'0' or date_str[5]>'9':
            return False
        if date_str[6]<'0' or date_str[6]>'9':
            return False
        if date_str[7] != '-':
            return False
        if date_str[8]<'0' or date_str[8]>'9':
            return False
        if date_str[9]<'0' or date_str[9]>'9':
            return False
        return True

class Swim:
    def __init__(self, date, distance, duration):
        if distance <= 0:
            raise ValueError("Distance must be greater than 0.")
        if duration <= 0:
            raise ValueError("Duration must be greater than 0.")
        if distance/duration > 0.1278:
            raise ValueError("You just broke the world record for Swim! Either you are a superhuman or the data is incorrect.")

        if not self.is_valid_date(date):
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        self.date = date # date in YYYY-MM-DD format
        self.distance = distance # distance in km
        self.duration = duration # duration in minutes

    @property
    def calories_factor(self):
        return 40

    @property
    def calories(self):
        return int((self.distance/(self.duration/60))*self.distance * self.calories_factor)

    def is_valid_date(self, date_str):
        if len(date_str) != 10:
            return False
        if date_str[0]<'0' or date_str[0]>'9':
            return False
        if date_str[1]<'0' or date_str[1]>'9':
            return False
        if date_str[2]<'0' or date_str[2]>'9':
            return False
        if date_str[3]<'0' or date_str[3]>'9':
            return False
        if date_str[4] != '-':
            return False
        if date_str[5]<'0' or date_str[5]>'9':
            return False
        if date_str[6]<'0' or date_str[6]>'9':
            return False
        if date_str[7] != '-':
            return False
        if date_str[8]<'0' or date_str[8]>'9':
            return False
        if date_str[9]<'0' or date_str[9]>'9':
            return False
        return True

class Ride:
    def __init__(self, date, distance, duration, elevation):
        if not self.is_valid_date(date):
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        self.date = date # date in YYYY-MM-DD format
        self.distance = distance # distance in km
        self.duration = duration # duration in minutes
        self.elevation = elevation # elevation in percentage

    @property
    def calories_factor(self):
        return 2 * (1 + self.elevation / 100)

    @property
    def calories(self):
        return int((self.distance/(self.duration/60))*self.distance * self.calories_factor)

    def is_valid_date(self, date_str):
        if len(date_str) != 10:
            return False
        if date_str[0]<'0' or date_str[0]>'9':
            return False
        if date_str[1]<'0' or date_str[1]>'9':
            return False
        if date_str[2]<'0' or date_str[2]>'9':
            return False
        if date_str[3]<'0' or date_str[3]>'9':
            return False
        if date_str[4] != '-':
            return False
        if date_str[5]<'0' or date_str[5]>'9':
            return False
        if date_str[6]<'0' or date_str[6]>'9':
            return False
        if date_str[7] != '-':
            return False
        if date_str[8]<'0' or date_str[8]>'9':
            return False
        if date_str[9]<'0' or date_str[9]>'9':
            return False
        return True

class ExerciseLog:
    def __init__(self):
        self.__exercises = []

    def add(self, exercise):
        self.__exercises.append(exercise)

    def create_run(self, date, distance, duration, elevation):
        self.add(Run(date, distance, duration, elevation))

    def create_swim(self, date, distance, duration):
        self.add(Swim(date, distance, duration))

    def create_ride(self, date, distance, duration, elevation):
        self.add(Ride(date, distance, duration, elevation))

    def total_calories_burnt(self):
        return sum(exercise.calories for exercise in self.__exercises)
