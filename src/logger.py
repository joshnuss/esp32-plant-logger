class Logger:
    def __init__(self, path = '/sd/temp.csv'):
        self.path = path

    def log(self, values):
        line = ','.join(values)
        print(line)

        file = open(self.path, 'a')
        file.write(line + '\n')
        file.close()
