from facade_formatter import FacadeFormatter


class InterfaceDisplay:

    def __init__(self):
        self.formatter = FacadeFormatter();

    def format_rows(self, rows):
        formatted_rows = []
        for row in rows:
            formatted_rows.append(self.formatter.format_row(row))
        return formatted_rows

    def display_all_items(self, facade):
        return self.format_rows(facade.get_all_items())

    def display_overdue_items(self, facade):
        return self.format_rows(facade.get_overdue_items())

    def display_last_days_items(self, facade):
        return self.format_rows(facade.get_last_days_items())
