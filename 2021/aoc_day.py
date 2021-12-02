import requests

class AOCDay:
    def __init__(self, filepath):
        self.set_input(
            filepath
        )

    def set_input(self, filepath=None):
        if filepath is None:
            headers = {
                'cookie': 'session=53616c7465645f5f675aea7adfc467a0be6ab4893603804db460ec1a78c1027ba3b4b1e57038e68251ae350f72853029',
            }
            self.raw_input = requests.get(f"https://adventofcode.com/2021/day/{self.day}/input", headers=headers).content.decode('utf-8').strip()
        else:
            with open(filepath) as f:
                self.raw_input = f.read().strip()
        
        self.input_lines = [l.strip() for l in self.raw_input.split('\n')]