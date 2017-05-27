import genetic_lib as lib

once = True

def main_testepng(individuo_list):
    for i in range(len(individuo_list)):
        for j in range(10):
            individuo_list[i].mutate()
        individuo_list[i].save_png("static/%s.png" %i)
