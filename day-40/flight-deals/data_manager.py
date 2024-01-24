import polars as pl

class DataManager():
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        super().__init__()
        self.file_name = "Flight Deals.csv"
        self.df = pl.read_csv(self.file_name)

    def save(self, rows):
        self.df = pl.DataFrame(rows)
        self.df.write_csv(self.file_name)