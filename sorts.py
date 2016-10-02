import random
import time
from random import randint
import heapq


class WorldData:
    def __init__(self, country_name, life_expectancy):
        self.country_name = country_name
        self.life_expectancy = life_expectancy

    def generate_life_expectancy(self):
        life_expectancy = random.randint(65, 85)
        return life_expectancy

    def generate_country_name(self):
        country_name = " "
        n_country_name = random.randint(1, 10)
        if n_country_name == 1:
            country_name = "Brazil"
        elif n_country_name == 2:
            country_name = "Argentina"
        elif n_country_name == 3:
            country_name = "Uruguay"
        elif n_country_name == 4:
            country_name = "Paraguay"
        elif n_country_name == 5:
            country_name = "Chile"
        elif n_country_name == 6:
            country_name = "Bolivia"
        elif n_country_name == 7:
            country_name = "Peru"
        elif n_country_name == 8:
            country_name = "Ecuador"
        elif n_country_name == 9:
            country_name = "Colombia"
        elif n_country_name == 10:
            country_name = "Venezuela"
        return country_name

    # ALGORITMOS NUMERICOS
    def insertionSort(self, alist, list_number):
        file = open("resultados_Zimbabwe.txt", "a")
        start_time = time.time()
        for index in range(1, len(alist)):
            currentvalue = alist[index].life_expectancy
            position = index

            while position > 0 and alist[position - 1].life_expectancy > currentvalue:
                alist[position].life_expectancy = alist[position - 1].life_expectancy
                position = position - 1

            alist[position].life_expectancy = currentvalue
        elapsed_time = (time.time() - start_time) * 1000
        file.write("ISBL, numerico, ")
        file.write(list_number)
        file.write(", ")
        file.write(str(int(elapsed_time)))
        file.write("ms\n")
        file.close()

    def shellSort(self, alist, list_number):
        file = open("resultados_Zimbabwe.txt", "a")
        start_time = time.time()
        sublistcount = len(alist) // 2
        while sublistcount > 0:
            for startposition in range(sublistcount):
                self.gapInsertionSort(alist, startposition, sublistcount)

            sublistcount = sublistcount // 2
        elapsed_time = (time.time() - start_time) * 1000
        file.write("SHST, numerico, ")
        file.write(list_number)
        file.write(", ")
        file.write(str(int(elapsed_time)))
        file.write("ms\n")
        file.close()

    # Shell Sort auxiliar
    def gapInsertionSort(self, alist, start, gap):
        for i in range(start + gap, len(alist), gap):

            currentvalue = alist[i].life_expectancy
            position = i

            while position >= gap and alist[position - gap].life_expectancy > currentvalue:
                alist[position].life_expectancy = alist[position - gap].life_expectancy
                position = position - gap

            alist[position].life_expectancy = currentvalue

    def bubbleSort(self, alist, list_number):
        file = open("resultados_Zimbabwe.txt", "a")
        start_time = time.time()
        for passnum in range(len(alist) - 1, 0, -1):
            for i in range(passnum):
                if alist[i].life_expectancy > alist[i + 1].life_expectancy:
                    temp = alist[i].life_expectancy
                    alist[i].life_expectancy = alist[i + 1].life_expectancy
                    alist[i + 1].life_expectancy = temp
        elapsed_time = (time.time() - start_time) * 1000
        file.write("BBST, numerico, ")
        file.write(list_number)
        file.write(", ")
        file.write(str(int(elapsed_time)))
        file.write("ms\n")
        file.close()


    def quickSort(self, alist, start, end, list_number):
        file = open("resultados_Zimbabwe.txt", "a")
        start_time = time.time()
        self.inPlaceQuickSort(alist, start, end)
        elapsed_time = (time.time() - start_time) * 1000
        file.write("QSRM, numerico, ")
        file.write(list_number)
        file.write(", ")
        file.write(str(int(elapsed_time)))
        file.write("ms\n")
        file.close()


    def inPlaceQuickSort(self, alist, start, end):
        if start < end:
            pivot = randint(start, end)
            temp = alist[end].life_expectancy
            alist[end].life_expectancy = alist[pivot].life_expectancy
            alist[pivot].life_expectancy = temp

            p = self.inPlacePartition(alist, start, end)
            self.inPlaceQuickSort(alist, start, p - 1)
            self.inPlaceQuickSort(alist, p + 1, end)

    def inPlacePartition(self, alist, start, end):
        pivot = randint(start, end)
        temp = alist[end].life_expectancy
        alist[end].life_expectancy = alist[pivot].life_expectancy
        alist[pivot].life_expectancy = temp
        newPivotIndex = start - 1
        for index in range(start, end):
            if alist[index].life_expectancy < alist[end].life_expectancy:
                newPivotIndex = newPivotIndex + 1
                temp = alist[newPivotIndex].life_expectancy
                alist[newPivotIndex].life_expectancy = alist[index].life_expectancy
                alist[index].life_expectancy = temp
        temp = alist[newPivotIndex + 1].life_expectancy
        alist[newPivotIndex + 1].life_expectancy = alist[end].life_expectancy
        alist[end].life_expectancy = temp
        return newPivotIndex + 1



    def heap_swap(self, l, i, j):
        tmp = l[i]
        l[i] = l[j]
        l[j] = tmp

    def heap_heapify(self, l, idx, end):
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < end and l[left].life_expectancy > l[idx].life_expectancy:
            largest = left
        else:
            largest = idx
        if right < end and l[right].life_expectancy > l[largest].life_expectancy:
            largest = right

        if largest != idx:
            self.heap_swap(l, idx, largest)
            self.heap_heapify(l, largest, end)

    def heap_build_heap(self, l):
         for i in range(len(l) // 2 - 1, -1, -1):
             self.heap_heapify(l, i, len(l))

    def heapSort(self, l, list_number):
        file = open("resultados_Zimbabwe.txt", "a")
        start_time = time.time()
        self.heap_build_heap(l)
        for i in range(len(l) - 1, -1, -1):
            self.heap_swap(l, 0, i)
            self.heap_heapify(l, 0, i)
        elapsed_time = (time.time() - start_time) * 1000
        file.write("HPST, numerico, ")
        file.write(list_number)
        file.write(", ")
        file.write(str(int(elapsed_time)))
        file.write("ms\n")
        file.close()


            # ALGORITMOS CATEGORICOS
    def insertionSort_name(self, alist, list_number):
        file = open("resultados_Zimbabwe.txt", "a")
        start_time = time.time()
        for index in range(1, len(alist)):
            currentvalue = alist[index].country_name
            position = index

            while position > 0 and alist[position - 1].country_name > currentvalue:
                alist[position].country_name = alist[position - 1].country_name
                position = position - 1

            alist[position].country_name = currentvalue
        elapsed_time = (time.time() - start_time) * 1000
        file.write("ISBL, categorico, ")
        file.write(list_number)
        file.write(", ")
        file.write(str(int(elapsed_time)))
        file.write("ms\n")
        file.close()

    def shellSort_name(self, alist, list_number):
        file = open("resultados_Zimbabwe.txt", "a")
        start_time = time.time()
        gap = len(alist) // 2
        # loop over the gaps
        while gap > 0:
            # do the insertion sort
            for i in range(gap, len(alist)):
                val = alist[i].country_name
                j = i
                while j >= gap and alist[j - gap].country_name > val:
                    alist[j].country_name = alist[j - gap].country_name
                    j -= gap
                alist[j].country_name = val
            gap //= 2
        elapsed_time = (time.time() - start_time) * 1000
        file.write("SHST, categorico, ")
        file.write(list_number)
        file.write(", ")
        file.write(str(int(elapsed_time)))
        file.write("ms\n")
        file.close()

    def bubbleSort_name(self, alist, list_number):
        file = open("resultados_Zimbabwe.txt", "a")
        start_time = time.time()
        for passnum in range(len(alist) - 1, 0, -1):
            for i in range(passnum):
                if alist[i].country_name > alist[i + 1].country_name:
                    temp = alist[i].country_name
                    alist[i].country_name = alist[i + 1].country_name
                    alist[i + 1].country_name = temp
        elapsed_time = (time.time() - start_time) * 1000
        file.write("BBST, categorico, ")
        file.write(list_number)
        file.write(", ")
        file.write(str(int(elapsed_time)))
        file.write("ms\n")
        file.close()

    def quickSort_name(self, alist, start, end, list_number):
        file = open("resultados_Zimbabwe.txt", "a")
        start_time = time.time()
        self.inPlaceQuickSort_name(alist, start, end)
        elapsed_time = (time.time() - start_time) * 1000
        file.write("QSRM, categorico, ")
        file.write(list_number)
        file.write(", ")
        file.write(str(int(elapsed_time)))
        file.write("ms\n")
        file.close()


    def inPlaceQuickSort_name(self, alist, start, end):
        if start < end:
            pivot = randint(start, end)
            temp = alist[end].country_name
            alist[end].country_name = alist[pivot].country_name
            alist[pivot].country_name = temp

            p = self.inPlacePartition_name(alist, start, end)
            self.inPlaceQuickSort_name(alist, start, p - 1)
            self.inPlaceQuickSort_name(alist, p + 1, end)

    def inPlacePartition_name(self, alist, start, end):
        pivot = randint(start, end)
        temp = alist[end].country_name
        alist[end].country_name = alist[pivot].country_name
        alist[pivot].country_name = temp
        newPivotIndex = start - 1
        for index in range(start, end):
            if alist[index].country_name < alist[end].country_name:  # check if current val is less than pivot value
                newPivotIndex = newPivotIndex + 1
                temp = alist[newPivotIndex].country_name
                alist[newPivotIndex].country_name = alist[index].country_name
                alist[index].country_name = temp
        temp = alist[newPivotIndex + 1].country_name
        alist[newPivotIndex + 1].country_name = alist[end].country_name
        alist[end].country_name = temp
        return newPivotIndex + 1


    def heap_swap_name(self, l, i, j):
        tmp = l[i]
        l[i] = l[j]
        l[j] = tmp

    def heap_heapify_name(self, l, idx, end):
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < end and l[left].country_name > l[idx].country_name:
            largest = left
        else:
            largest = idx
        if right < end and l[right].country_name > l[largest].country_name:
            largest = right

        if largest != idx:
            self.heap_swap_name(l, idx, largest)
            self.heap_heapify_name(l, largest, end)

    def heap_build_heap_name(self, l):
         for i in range(len(l) // 2 - 1, -1, -1):
             self.heap_heapify_name(l, i, len(l))

    def heapSort_name(self, l, list_number):
        file = open("resultados_Zimbabwe.txt", "a")
        start_time = time.time()
        self.heap_build_heap_name(l)
        for i in range(len(l) - 1, -1, -1):
            self.heap_swap_name(l, 0, i)
            self.heap_heapify_name(l, 0, i)
        elapsed_time = (time.time() - start_time) * 1000
        file.write("HPST, categorico, ")
        file.write(list_number)
        file.write(", ")
        file.write(str(int(elapsed_time)))
        file.write("ms\n")
        file.close()




obj = WorldData(None, None)
# cria listas de objetos

obj_list100 = [WorldData(obj.generate_country_name(), obj.generate_life_expectancy()) for i in range(100)]
obj_list1000 = [WorldData(obj.generate_country_name(), obj.generate_life_expectancy()) for i in range(1000)]
obj_list2000 = [WorldData(obj.generate_country_name(), obj.generate_life_expectancy()) for i in range(2000)]
obj_list10000 = [WorldData(obj.generate_country_name(), obj.generate_life_expectancy()) for i in range(10000)]
obj_list100000 = [WorldData(obj.generate_country_name(), obj.generate_life_expectancy()) for i in range(100000)]
# Para listas com 100 objetos
random.shuffle(obj_list100)#SHUFFLE LIST
obj.insertionSort(obj_list100, "100")
obj.insertionSort_name(obj_list100, "100")
random.shuffle(obj_list100)#SHUFFLE LIST
obj.shellSort(obj_list100, "100")
obj.shellSort_name(obj_list100, "100")
random.shuffle(obj_list100)#SHUFFLE LIST
obj.bubbleSort(obj_list100, "100")
obj.bubbleSort_name(obj_list100, "100")
random.shuffle(obj_list100)#SHUFFLE LIST
obj.quickSort(obj_list100, 0, 99, "100")
obj.quickSort_name(obj_list100, 0, 99, "100")
random.shuffle(obj_list100)#SHUFFLE LIST
obj.heapSort(obj_list100, "100")
obj.heapSort_name(obj_list100, "100")
# Para listas com 1000 objetos
random.shuffle(obj_list1000)#SHUFFLE LIST
obj.insertionSort(obj_list1000, "1000")
obj.insertionSort_name(obj_list1000, "1000")
random.shuffle(obj_list1000)#SHUFFLE LIST
obj.shellSort(obj_list1000, "1000")
obj.shellSort_name(obj_list1000, "1000")
random.shuffle(obj_list1000)#SHUFFLE LIST
obj.bubbleSort(obj_list1000, "1000")
obj.bubbleSort_name(obj_list1000, "1000")
random.shuffle(obj_list1000)#SHUFFLE LIST
obj.quickSort(obj_list1000, 0, 999, "1000")
obj.quickSort_name(obj_list1000, 0, 999, "1000")
random.shuffle(obj_list1000)#SHUFFLE LIST
obj.heapSort(obj_list1000, "1000")
obj.heapSort_name(obj_list1000, "1000")
# Para listas com 2000 objetos
random.shuffle(obj_list2000)#SHUFFLE LIST
obj.insertionSort(obj_list2000, "2000")
obj.insertionSort_name(obj_list2000, "2000")
random.shuffle(obj_list2000)#SHUFFLE LIST
obj.shellSort(obj_list2000, "2000")
obj.shellSort_name(obj_list2000, "2000")
random.shuffle(obj_list2000)#SHUFFLE LIST
obj.bubbleSort(obj_list2000, "2000")
obj.bubbleSort_name(obj_list2000, "2000")
random.shuffle(obj_list2000)#SHUFFLE LIST
obj.quickSort(obj_list2000, 0, 999, "2000")
obj.quickSort_name(obj_list2000, 0, 999, "2000")
random.shuffle(obj_list2000)#SHUFFLE LIST
obj.heapSort(obj_list2000, "2000")
obj.heapSort_name(obj_list2000, "2000")
# Para listas com 10000 objetos
random.shuffle(obj_list10000)#SHUFFLE LIST
obj.insertionSort(obj_list10000, "10000")
obj.insertionSort_name(obj_list10000, "10000")
random.shuffle(obj_list10000)#SHUFFLE LIST
obj.shellSort(obj_list10000, "10000")
obj.shellSort_name(obj_list10000, "10000")
random.shuffle(obj_list10000)#SHUFFLE LIST
obj.bubbleSort(obj_list10000, "10000")
obj.bubbleSort_name(obj_list10000, "10000")
random.shuffle(obj_list10000)#SHUFFLE LIST
obj.heapSort(obj_list10000, "10000")
obj.heapSort_name(obj_list10000, "10000")
# Para listas com 100000 objetos
random.shuffle(obj_list100000)#SHUFFLE LIST
obj.shellSort(obj_list100000, "100000")
obj.shellSort_name(obj_list100000, "100000")
random.shuffle(obj_list100000)#SHUFFLE LIST
obj.heapSort(obj_list100000, "100000")
obj.heapSort_name(obj_list100000, "100000")