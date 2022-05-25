from hashlib import algorithms_available
from lib2to3.pgen2.pgen import generate_grammar
from math import sqrt
from math import floor
from threading import local


class Problem:
    def __init__(self, filename):
        self.solutions = []
        with open(filename) as input_file:
            self.instance = [int(x) for x in input_file.readline().split(" ")]

    def yield_solutions(self):
        for solution in self.solutions:
            yield solution

    def map_size(self):
        numA = len(self.instance)
        a = 1
        b = 3
        c = 2-(2*numA)
        delta = (b*b)-(4*a*c)
        delta_root = sqrt(delta)
        x1 = ((-b)-delta_root)/2*a
        x2 = ((-b)+delta_root)/2*a

        if delta < 0:
            print('Delta mniejsza od 0!')
            return 0
        if not (delta_root).is_integer():
            print('Delta nie jest calkowita!')
            return 0
        if (x1 > 0) or (x2 > 0):
            return max(x1, x2)
        return 0

    def find_solution(self):
        k = int(self.map_size())
        if k == 0:
            print('Podane dane sa nieprawidlowe\n')
        else:
            candidates = self.instance.copy()
            max_segment = max(candidates)
            candidates.remove(max_segment)
            second_max = max(candidates)
            first_element = max_segment-second_max
            candidates.remove(second_max)
            candidates.remove(first_element)
            used_elements = [max_segment, second_max, first_element]
            result_map = [first_element]
            self.algorithm(candidates, used_elements,
                           result_map, max_segment, k, 1)

    def generate_cuts(self, result_map, max_segment, candidate):
        reversed_map = result_map.copy()
        reversed_map.reverse()
        local_result = [candidate]
        sum = candidate
        for ints in reversed_map:
            sum += ints
            local_result.append(sum)
        local_result.append(max_segment-sum)
        return local_result

    def delete_elements(self, list1, list2):
        for element in list2:
            list1.remove(element)
        return list1

    def algorithm(self, candidates, used_elements, result_map, max_segment, max_depth, iteration):
        if (len(candidates) == 0) and (iteration == max_depth) and (len(result_map) == max_depth+1):
            self.solutions.append(result_map)
            return
        if (len(result_map) > max_depth+1):
            print('---Rozmiar mapy przekroczony---\n KONIEC PRZESZUKIWANIA!')
            return
        if(len(candidates) == 0):
            print("---Brak elementow do sprawdzenia---\n KONIEC PRZESZUKIWANIA")
            return
        for id in candidates:
            local_candidates = candidates.copy()
            local_used_elements = used_elements.copy()
            found_result = result_map.copy()
            possible_cuts = self.generate_cuts(found_result, max_segment, id)

            if (all(elem in candidates for elem in possible_cuts)):
                found_result.append(id)
                local_used_elements.extend(possible_cuts)
                local_candidates = self.delete_elements(
                    local_candidates, possible_cuts)
                if(len(local_candidates) == 0):
                    found_result.append(max_segment-sum(found_result))
                self.algorithm(local_candidates, local_used_elements,
                               found_result, max_segment, max_depth, iteration+1)
