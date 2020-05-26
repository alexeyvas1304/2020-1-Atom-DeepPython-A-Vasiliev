class Cinema:
    def __init__(self, path):
        self.lst_of_seats = self.parse_file(path)

    @staticmethod
    def parse_file(path):
        lst_of_seats = []
        with open(path) as f:
            for line in f:
                lst_of_seats.append(list(map(int, line.split())))
        return lst_of_seats

    def free_seats_count(self):
        count = 0
        for row in self.lst_of_seats:
            count += len(row) - sum(row)
        return count

    def is_free(self, x, y):
        if 1 <= x <= len(self.lst_of_seats[0]) and 1 <= y <= len(self.lst_of_seats[1]):
            return self.lst_of_seats[x - 1][y - 1] == 0
        else:
            return f"УКажите верные данные: ряд должен быть от 1 до {len(self.lst_of_seats[0])}, место - от 1 до {len(self.lst_of_seats[1])}"


if __name__ == "__main__":
    example = Cinema("files/cinema.txt")
    print(example.free_seats_count())  # 27
    print(example.is_free(1, 1))
    print(example.is_free(1, 2))
    print(example.is_free(10, 10))
