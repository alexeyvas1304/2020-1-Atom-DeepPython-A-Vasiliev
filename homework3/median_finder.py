class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.structure = list()

    def add_num(self, num: int) -> None:
        self.structure.append(num)

    def find_median(self) -> float:
        sorted_structure = sorted(self.structure)
        if len(self.structure) % 2:
            return sorted_structure[len(self.structure) // 2]
        else:
            try:
                return (sorted_structure[len(self.structure) // 2] + sorted_structure[len(self.structure) // 2 - 1]) / 2
            except IndexError:
                return 'structure is empty'
