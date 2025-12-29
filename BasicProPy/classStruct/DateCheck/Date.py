class Date:
    # index 0 -> dummy
    DAYS_IN_MONTH = [0 ,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, month: int, day: int):
        self._month = 0
        self._day = 0

        self.month = month
        self.day = day

    @property
    def month(self) -> int:
        return self._month
    
    @month.setter
    def month(self, value: int):
        if 1<=value <= 12:
            self._month = value

    @property
    def day(self):
        return self._day
    
    @day.setter
    def day(self, value: int):
        max_days = self.days_in_month()
        if 1<=value<=max_days:
            self._day = value
    

    def days_in_month(self) -> int:
        if 1<=self._month<=12:
            return Date.DAYS_IN_MONTH[self._month]
        
    
    def advance(self):
        self._day +=1

        if self._day > self.days_in_month:
            self._day = 1
            self._month +=1

            if self._month > 12:
                self._month = 1
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Date):
            return self.month == other.month and self.day == other.day
        return NotImplemented
    
    def __str__(self) -> str:
        return f"{self.month}/{self.day}"
