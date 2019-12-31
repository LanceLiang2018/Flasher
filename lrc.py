
class Lrc:
    def __init__(self, filename):
        with open(filename, 'rb') as f:
            self.text = f.read().decode()
        self.data = {}
        for i in self.text.split('\n'):
            s = i.split(']')
            s[0] = s[0][1:]
            if s[0].split(':')[0].isdigit() and s[1] != '':
                self.data[str(round(float(s[0].split(':')[0])*60 + float(s[0].split(':')[1]), 2))] = s[1]
        # print(self.data)


class Lrc2:
    def __init__(self):
        self.text = ''
        self.data = {}

    def load(self, content: str):
        self.text = content
        self.data = {}
        for i in self.text.split('\n'):
            s = i.split(']')
            s[0] = s[0][1:]
            if s[0].split(':')[0].isdigit() and s[1] != '':
                self.data[str(round(float(s[0].split(':')[0])*60 + float(s[0].split(':')[1]), 2))] = s[1]
        # print(self.data)

    def __str__(self):
        return str(self.text)


if __name__ == '__main__':
    lrc = Lrc('Cache\\t.lrc')
    

