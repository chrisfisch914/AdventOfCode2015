class InputReader:
    @staticmethod
    def fetch_input():
        data = ""
        with open('input.txt', 'r') as file:
            data = file.read()
        return data

    @staticmethod
    def fetch_input_lines():
        return InputReader.fetch_input().split("\n")

    @staticmethod
    def fetch_input_seperated_by_empty_lines():
        return InputReader.fetch_input().split("\n\n")

    @staticmethod
    def fetch_numbers():
        return [int(value) for value in InputReader.fetch_input_lines()]

    @staticmethod
    def fetch_number():
        return InputerReader.fetch_numbers()[0]
