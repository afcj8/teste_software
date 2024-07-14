import unittest

class BuscaBinaria:
    def busca_binaria(self, arr, x):
        n = 0
        y = len(arr) - 1

        while n <= y:
            aux = (n + y) // 2
            if arr[aux] == x:
                return True
            elif arr[aux] < x:
                n = aux + 1
            else:
                y = aux - 1
        return False