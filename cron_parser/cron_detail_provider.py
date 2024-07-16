from cron_validator import CronValidator


class CronProvider:
    def __init__(self, expression: str):
        self.validator = None
        self.expression = expression

    def validate_expression(self):
        self.validator = CronValidator(self.expression)
        return self.validator.validate_cron_data()

    def format_cron_data(self):
        formatted_output = list()
        formatted_output.append("minute {}".format(' '.join(map(str, self.validator.minutes))))
        formatted_output.append("hour {}".format(' '.join(map(str, self.validator.hours))))
        formatted_output.append("day of month {}".format(" ".join(map(str, self.validator.days))))
        formatted_output.append("month {}".format(' '.join(map(str, self.validator.months))))
        formatted_output.append("day of week {}".format(' '.join(map(str, self.validator.weeks))))
        formatted_output.append("command {}".format(''.join(map(str, self.validator.command))))

        return "\n".join(formatted_output)
