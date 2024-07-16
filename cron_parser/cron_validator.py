import re


class CronValidator:

    def __init__(self, expression: str):
        self._cron_expression = expression
        self._regex_cron_pattern = r'^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(.*)$'
        self.minutes = []
        self.hours = []
        self.days = []
        self.months = []
        self.weeks = []
        self.command = ""

    def validate_cron_expression(self):
        match_values = re.match(self._regex_cron_pattern, self._cron_expression)
        if not match_values:
            raise ValueError("Wrong cron string provided: {}".format(self._cron_expression))
        return match_values

    def validate_hyphen(self, data, component_data, start, end, values, steps=1):
        new_range = list(map(int, data.split('-')))
        if len(new_range) != 2:
            raise ValueError("Wrong cron string provided: {}".format(component_data))
        if new_range[0] < start or new_range[1] > end or new_range[0] > new_range[1]:
            raise ValueError("Wrong cron string provided: {}".format(component_data))
        values.extend(range(new_range[0], new_range[1] + 1, steps))

    def validate_slash(self, data, component_data, start, end, values):
        if len(data) != 2:
            raise ValueError("Wrong component provided: {}".format(component_data))
        steps = int(data[1])
        if steps < start or steps > end:
            raise ValueError("Wrong component provided: {}".format(component_data))
        first_component = data[0]
        if first_component == "*":
            values.extend(range(start, end + 1, steps))
        elif "-" in first_component:
            self.validate_hyphen(first_component, component_data, start, end, values, steps)
        else:
            raise ValueError("Wrong component provided: {}".format(component_data))

    def validate_component(self, component_data, range_start, range_end):
        if component_data == "*":
            return list(range(range_start, range_end + 1))

        value_list = component_data.split(',')
        values = []
        for part in value_list:
            if '/' in part:
                split_data = part.split('/')
                self.validate_slash(split_data, component_data, range_start, range_end, values)
            elif '-' in part:
                self.validate_hyphen(part, component_data, range_start, range_end, values)
            else:
                val = int(part)
                if val < range_start or val > range_end:
                    raise ValueError("Wrong component provided: {}".format(component_data))
                values.append(val)

        return sorted(set(values))

    def validate_minutes(self, minute_value):
        try:
            self.minutes = self.validate_component(minute_value, 0, 59)
            return True
        except ValueError as ve:
            print("Minutes(0:59): {}".format(ve))
            return False

    def validate_hours(self, hour_value):
        try:
            # import pdb;pdb.set_trace()
            self.hours = self.validate_component(hour_value, 0, 23)
            return True
        except ValueError as ve:
            print("Hours(0:23): {}".format(ve))
            return False

    def validate_day_of_month(self, day_value):
        try:
            self.days = self.validate_component(day_value, 1, 31)
            return True
        except ValueError as ve:
            print("Day of month(1:31): {}".format(ve))
            return False

    def validate_month(self, month_value):
        try:
            self.months = self.validate_component(month_value, 1, 12)
            return True
        except ValueError as ve:
            print("Month(1:12): {}".format(ve))
            return False

    def validate_day_of_week(self, day_of_week_value):
        try:
            self.weeks = self.validate_component(day_of_week_value, 1, 7)
            return True
        except ValueError as ve:
            print("Day of Week(1:7): {}".format(ve))
            return False

    def validate_cron_data(self):
        try:
            match = self.validate_cron_expression()
            matching_data = match.groups()
            self.command = matching_data[-1]
            return (self.validate_minutes(matching_data[0]) and self.validate_hours(matching_data[1])
                    and self.validate_day_of_month(matching_data[2]) and self.validate_month(matching_data[3])
                    and self.validate_day_of_week(matching_data[4]))
        except ValueError as e:
            print("{}".format(e))
            return False
