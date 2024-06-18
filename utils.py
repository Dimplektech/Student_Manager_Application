from datetime import datetime


def draw_line(symbol="-", length=80):
    print(symbol*length)


def parse_date(date_str):
    """Parse a string into a date object, raise valueError is format is
      incorrect."""
    try:
        return datetime.strptime(date_str, "%d-%m-%Y").date()
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}.Expected format: DD-MM-YYYY.")
