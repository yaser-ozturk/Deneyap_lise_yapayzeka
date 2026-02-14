import pygad
import numpy

function_inputs = [4,-2,3.5,5,-11,-4.7] 
desired_output = 44 

def fitness_func(ga_instance, solution, solution_idx):

    output = numpy.sum(solution*function_inputs) 


    fitness = 1.0 / numpy.abs(output - desired_output) ##  1 / hata hata azaldıkça 0 fitness gittikçe maksa gidecek
    return fitness

num_genes = len(function_inputs)      # 4x1 – 2x2 + 3,5x3 + 5x4 – 11x5 – 4,7x6 = out   [1, 2 , 3, 4, 5, 6] [4, 2, 3, 5, 1, 7] [1, 2, 3, 4, 5, 6]  [4, 2, 3, 5, 1, 7] ....
                                    #   4  +   -4     10.5   20 -55  -32     =                             C1 [1, 2, 3, 5, 1, 7]  [4, 2, 3, 6, 1, 7] [1, 2, 3, 4, 5, 6]  [4, 2, 3, 5, 1, 7] 


fitness_function = fitness_func

num_generations = 100   

num_parents_mating = 7

sol_per_pop = 50   


last_fitness = 0



def nesil_ozeti(ga_instance):
    global last_fitness
    print("Nesil = {generation}".format(generation=ga_instance.generations_completed))

    print("Fonksiyon Sonucu = {fitness}".format(fitness=ga_instance.best_solution()[1])) 

    print("Degisim = {change}".format(change=ga_instance.best_solution()[1] - last_fitness))

    last_fitness = ga_instance.best_solution()[1]


ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating, 
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop, 
                       num_genes=num_genes,
                       on_generation=nesil_ozeti)

ga_instance.run()


solution, solution_fitness, solution_idx = ga_instance.best_solution() 

print("En uygun cozum degisken degerleri : {solution}".format(solution=solution))
print("En uygun cozumu veren birey indeks no.: {solution_idx}".format(solution_idx=solution_idx))

prediction = numpy.sum(numpy.array(function_inputs)*solution)
print("En uygun cozum ile fonksiyon sonucu : {prediction}".format(prediction=prediction))


if ga_instance.best_solution_generation != -1:
    print("En uygun cozum {best_solution_generation} nesil sonra elde edildi."
          .format(best_solution_generation=ga_instance.best_solution_generation))
