import csv
from MarketAction import MarketDatum


class FracsoftReader():
    def __init__(self, filename):
        self.filename = filename
        self.ifile = open(filename, "rb")
        self.csvreader = csv.reader(self.ifile)

        print self.csvreader
        self.name = self.csvreader.next()
        self.csvreader.next()
        self.event = self.csvreader.next()
        self.csvreader.next()
        self.csvreader.next()
        self.datestring = self.csvreader.next()
        self.header = self.csvreader.next()

        self.currentRow = 7

    def GetMarketData(self, count=1):
        data = []

        # Want to get two rows for each data call to get each runner
        for i in range(2 * count):
            # Exit loop with 'None' appended if we've reached the end of the file
            try:
                row = self.csvreader.next()
            except:
                self.ifile.close()
                return None

            data.append(MarketDatum(
                runnerId=int(row[5]),
                runnerName=row[6],
                pricesToBack=[float(s) for s in row[8:13:2]],
                valuesToBack=[float(s) for s in row[9:14:2]],
                pricesToLay=[float(s) for s in row[14:19:2]],
                valuesToLay=[float(s) for s in row[15:20:2]],
                ticks=int(row[0]),
                id=self.currentRow))

            self.currentRow = self.currentRow + 1

        return data
