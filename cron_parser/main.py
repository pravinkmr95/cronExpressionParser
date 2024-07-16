import sys
from cron_detail_provider import CronProvider


if __name__ == '__main__':
    # cron_expression = "*/15 0 1,15 * 1-5 /usr/bin/find"
    # cron_expression = "*/10 0 1,15 * 1-5 /usr/bin/find"

    # cron_expression = "* * * * * /usr/bin/find"
    if len(sys.argv) != 2:
        print("Please enter the input in correct format from the terminal, ie: 'python3 main.py <cron_expression>'")
    else:
        cron_expression = sys.argv[1]
        print("Details for cron expression {}".format(cron_expression))
        print("----------------------------------------------")
        cron_details_obj = CronProvider(cron_expression)
        if cron_details_obj.validate_expression():
            print(cron_details_obj.format_cron_data())
    print()
