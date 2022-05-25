from Class import Problem

new_instance = Problem('Map.txt')
new_instance.find_solution()

print(f'TRWA ODCZYT...\n')
print(f'Wczytano odcinki: {new_instance.instance}')
print(f'---')
print(f'Rozmiar mapy: {new_instance.map_size()+1}\n')

for solution in new_instance.yield_solutions():
    print('Mozliwe rozwiazanie: ')
    print('------------------------')
    print(solution)
