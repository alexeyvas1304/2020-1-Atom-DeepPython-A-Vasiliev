class MaxHeap:
    def __init__(self, array: list) -> None:
        self.array = array

    def heapify(self) -> None:
        for i in range(len(self.array) // 2 - 1, -1, -1):
            self.shift_down(i)

    def shift_down(self, i: int) -> None:
        left = 2 * i + 1
        right = 2 * i + 2
        if right == len(self.array) and self.array[i] < self.array[left]:
            self.array[i], self.array[left] = self.array[left], self.array[i]
            self.shift_down(left)
        elif right < len(self.array) and self.array[i] < max(self.array[left], self.array[right]):
            if self.array[left] >= self.array[right]:
                self.array[i], self.array[left] = self.array[left], self.array[i]
                self.shift_down(left)
            else:
                self.array[i], self.array[right] = self.array[right], self.array[i]
                self.shift_down(right)

    def shift_up(self, i: int) -> None:
        while self.array[i] > self.array[(i - 1) // 2] and i > 0:
            self.array[i], self.array[(i - 1) // 2] = self.array[(i - 1) // 2], self.array[i]
            i = (i - 1) // 2

    def push(self, new_element: int) -> None:
        self.array.append(new_element)
        self.shift_up(len(self.array) - 1)

    def pop(self) -> int:
        if len(self.array) > 0:
            value = self.array[0]
            self.array[0] = self.array[-1]
            self.array.pop()
            self.shift_down(0)
            return value
        else:
            print('Heap is empty')
