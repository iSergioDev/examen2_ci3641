import heapq

class NewIterator:
    def __init__(self, nums):
        self.nums = nums
        self.index = 0
        # Convertir la lista en un montículo mínimo (heap)
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, num)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.heap:
            # No hay más elementos
            raise StopIteration
        # Extraer el elemento más pequeño
        return heapq.heappop(self.heap)

# Ejemplo de uso
if __name__ == "__main__":
    nums = [1, 3, 3, 2, 1]

    for value in NewIterator(nums):
        print(value, end=' ')
